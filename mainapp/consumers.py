import json
from channels.generic.websocket import AsyncWebsocketConsumer

class AsyncIMGUser(AsyncWebsocketConsumer):
    def connect(self):
        self.accept()

    def receive(self):
        pass

    def disconnect(self):
        pass