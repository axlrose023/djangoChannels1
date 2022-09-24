from channels.routing import ProtocolTypeRouter, URLRouter
from my_chat.routing import websocket_urls
from channels.sessions import SessionMiddlewareStack
from channels.auth import AuthMiddlewareStack

application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(URLRouter(websocket_urls, ))
})

