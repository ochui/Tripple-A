from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path('ws/cab/<room_name>', consumers.CabConsumer),
]
