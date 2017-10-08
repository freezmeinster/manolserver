from channels.routing import route
channel_routing = [
    route("websocket.connect", "deploy.consumers.ws_connect"),
    route("websocket.disconnect", "deploy.consumers.ws_disconnect"),
]