from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path('ws/cab/<socket_id>', consumers.CabConsumer),
]
