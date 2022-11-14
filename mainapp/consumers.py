import json
from channels.generic.websocket import AsyncJsonWebsocketConsumer
from asgiref.sync import async_to_sync

class AsyncIMGUser(AsyncJsonWebsocketConsumer):
    groups=['IMG']
    async def connect(self):
        await self.channel_layer.group_add(group='IMG', channel=self.channel_name)

        await self.accept()


    async def receive_json(self,text_data,**kwargs):
        print(text_data)
        await self.send_json({
            'data': text_data.get("message"),
        })
    # async def recieve(sef,text_data):
    #     data =  json.loads(text_data)
    #     print(data['message'])
    async def echo_message(self, message):
        await self.send_json({
            'data': message,
        })

    async def disconnect(self , code):
        await self.channel_layer.group_discard(
            group='IMG',
            channel=self.channel_name
        )
        await super().disconnect(code)