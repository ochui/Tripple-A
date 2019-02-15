import json
import redis
from asgiref.sync import async_to_sync
from channels.generic.websocket import AsyncJsonWebsocketConsumer
from django.conf import settings
from .exceptions import ClientError

r = redis.StrictRedis(host=settings.REDIS_DEFAULT_HOST, db=1)


class CabConsumer(AsyncJsonWebsocketConsumer):
    """
    This chat consumer handles websocket connections for chat clients.
    It uses AsyncJsonWebsocketConsumer, which means all the handling functions
    must be async functions, and any sync work (like ORM access) has to be
    behind database_sync_to_async or sync_to_async. For more, read
    http://channels.readthedocs.io/en/latest/topics/consumers.html
    """
    async def connect(self):

        """
        Called when the websocket is handshaking as part of initial connection.
        """
        self.diver_socket_id = self.scope['url_route']['kwargs']['socket_id']
        self.room_group_name = 'dirver_%s' % self.diver_socket_id

        # Are they logged in?
        if self.scope["user"].is_anonymous:
            # Reject the connection
            await self.accept()

        else:

            await self.accept()

    async def disconnect(self, close_code):
        """
        Called when the WebSocket closes for any reason.
        """

        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive_json(self, content):
        """
        Called when we get a text frame. Channels will JSON-decode the payload
        for us and pass it as the first argument.
        """
        # Messages will have a "command" key we can switch on
        command = content.get("command", None)

        try:
            if command == "join":
                # join the room
                await self.join_room()
            elif command == "leave":
                # Leave the room
                await self.leave_room(content["room"])
            elif command == "send":
                await self.send_room(content["location"])
        except ClientError as e:
            # Catch any errors and send it back
            await self.send_json({"error": e.code})

    async def join_room(self):
        """
        Called by receive_json when passenger sent a join command.
        """
        # The logged-in user is in our scope thanks to the authentication ASGI middleware

        # Send a join message
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "driver.join",
                "username": self.scope["user"].username,
            }
        )

        # Add them to the group so they get room messages
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name,
        )
        # Instruct their client to finish opening the room
        await self.send_json({
            "join": str(self.diver_socket_id),
        })

    async def leave_room(self, room_id):
        """
        Called by receive_json when someone sent a leave command.
        """

        # Remove them from the group so they no longer get room messages
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name,
        )
        # Instruct their client to finish closing the room
        await self.send_json({
            "leave": str(self.diver_socket_id),
        })

    async def send_room(self, location):
        """
        Called by receive_json when someone sends a message to a room.
        """
        # Check they are in this room

        # Get the room and send to the group about it
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "update.location",
                "message": location,
            }
        )

    async def driver_join(self, event):
        # Instruct driver app to send location
        await self.send_json({
            "connected": str(self.diver_socket_id),
        })