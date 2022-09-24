from django.urls import re_path

from my_chat.consumers import GroupChatConsumer, ChatConsumer, MyMiddlewareConsumer

websocket_urls = [
    re_path(r'^ws/groups/$', GroupChatConsumer),
    re_path(r'^ws/chat/(?P<group_id>\d+)/$', ChatConsumer),
    re_path(r'^ws/middleware/$', MyMiddlewareConsumer),
]
