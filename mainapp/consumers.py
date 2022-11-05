import json
from channels.generic.websocket import AsyncJsonWebsocketConsumer
from asgiref.sync import async_to_sync

class AsyncIMGUser(AsyncJsonWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add('IMG', self.channel_name)

        await self.accept()


    async def receive_json(self,content,**kwargs):
        print(content)
        await self.send_json({
            'data': content.get("msg"),
        })

    async def disconnect(self , close_code):
        print('conection closed')
        async_to_sync(self.channel_layer.group_discard)(
            'IMG', self.channel_name
        )
