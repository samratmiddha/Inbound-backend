import json
from channels.generic.websocket import AsyncJsonWebsocketConsumer
from mainapp.serializers import ChatsDefaultSerializer
from asgiref.sync import sync_to_async
import datetime
from channels.db import database_sync_to_async
@database_sync_to_async
def return_validated_serializer(data):
    print('kklllllllll')
    print(data)
    serializer= ChatsDefaultSerializer(data=data)
    if serializer.is_valid():
        serializer.save()

class AsyncIMGUser(AsyncJsonWebsocketConsumer):
    groups=['IMG']
    async def connect(self):
        await self.channel_layer.group_add(group='IMG', channel=self.channel_name)

        await self.accept()


    async def receive_json(self,text_data,**kwargs):
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

class AsyncChatUser(AsyncJsonWebsocketConsumer):
    groups=["Chat"]

    
    async def connect(self):
        await self.channel_layer.group_add(group='Chat',channel=self.channel_name)
        await self.accept()

    async def receive_json(self,text_data,**kwargs):
        print('llllll')
        text_data['time']=datetime.datetime.now()
        await return_validated_serializer(text_data)
        

    async def echo_message(self,message):
        await self.send_json({
            'data':message
        })
    async def disconnect(self ,code):
        await self.channel_layer.group_discard(
            group="Chat",
            channel=self.channel_name
        )
        await super().disconnect(code)