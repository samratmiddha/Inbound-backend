import json
from channels.generic.websocket import AsyncJsonWebsocketConsumer
from mainapp.serializers import ChatsDefaultSerializer
from asgiref.sync import sync_to_async
import datetime
from channels.db import database_sync_to_async
from mainapp.models import User
from mainapp.serializers import UserNameSerializer
@database_sync_to_async
def return_validated_serializer(data):
    print('kklllllllll')
    print(data)
    print("hii13")
    serializer= ChatsDefaultSerializer(data=data)
    print("hii5")
    if serializer.is_valid():
        print("hii6")
        serializer.save()
        print("hii7")

@database_sync_to_async
def return_sender_object(data):
    print("hii11")
    sender=User.objects.get(pk=data['sender'])
    serializer= UserNameSerializer(sender)
    return serializer.data
   


class AsyncIMGUser(AsyncJsonWebsocketConsumer):
    groups=['IMG']
    async def connect(self):
        await self.channel_layer.group_add(group='IMG', channel=self.channel_name)

        await self.accept()


    async def receive_json(self,text_data,**kwargs):
        await self.send_json({
            'data': text_data.get("message"),
        })
 
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
        if self.scope["url_route"]["kwargs"]["room_name"]!= 0:
            self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
            self.room_group_name = "chat_%s" % self.room_name
        else:
            self.room_name="Chat"
            self.room_group_name="Chat"
        await self.channel_layer.group_add(group=self.room_group_name,channel=self.channel_name)
        await self.accept()


    async def echo_message(self,message):
        await self.send_json({
            'data':message
                
        })
    async def receive_json(self,data,**kwargs):
        print( data)
        data['time']=datetime.datetime.now()
        print("hii0")
        await return_validated_serializer(data)
        print("hii9")
        sender = await return_sender_object(data)
        print("hii10")
        data['sender']=json.dumps(sender)
        print()
        print("hii12")
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "echo_message",
                "message": json.dumps(data, indent=4, sort_keys=True, default=str),
            },
        )
        

   
    async def disconnect(self ,code):
        await self.channel_layer.group_discard(
            group="Chat",
            channel=self.channel_name
        )
        await super().disconnect(code)

class AsyncIMGPanelUser(AsyncJsonWebsocketConsumer):
    groups=['Panel']
    async def connect(self):
        await self.channel_layer.group_add(group='Panel', channel=self.channel_name)

        await self.accept()


    async def receive_json(self,text_data,**kwargs):
        await self.send_json({
            'data': text_data.get("message"),
        })
 
    async def echo_message(self, message):
        await self.send_json({
            'data': message,
        })

    async def disconnect(self , code):
        await self.channel_layer.group_discard(
            group='Panel',
            channel=self.channel_name
        )
        await super().disconnect(code)
