from django.http import HttpResponse
from channels.handler import AsgiHandler
from channels import Group

def ws_connect(message):
    # ASGI WebSocket packet-received and send-packet message types
    # both have a "text" key for their textual data.
    message.reply_channel.send({"accept": True})
    code = message.content['path'].strip("/")
    print code
    Group(code).add(message.reply_channel)

def ws_disconnect(message):
    Group("chat").discard(message.reply_channel)
