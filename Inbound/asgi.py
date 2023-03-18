"""
ASGI config for Inbound project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Inbound.settings')

django.setup()

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator
from django.urls import re_path
from mainapp.consumers import AsyncIMGUser,AsyncChatUser,AsyncIMGPanelUser


application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter([
                re_path(r"ws/anchor", AsyncIMGUser.as_asgi()),
                re_path(r"ws/chat/(?P<room_name>\w+)/$",AsyncChatUser.as_asgi()),
                re_path(r"ws/panelws/",AsyncIMGPanelUser.as_asgi()),
            ])
        )
    ),
})

