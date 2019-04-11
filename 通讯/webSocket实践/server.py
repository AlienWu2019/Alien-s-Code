'''从客户端接收一条消息，将该消息发送回客户端并关闭连接(通过试图返回)'''
from dwebsocket import require_websocket

@require_websocket
def echo(request):
    message = request.websocket.wait() #从客户端接收一条消息
    request.websocket.send(message) #将该消息发送回给客户端，并且关闭连接

'''我们页可以让服务端不自动关闭连接，下面的例程中，服务器端回将客户端发来的消息转为小写发送回去，并且增加了普通Http请求的响应，野做同样的操作返回'''

# from django.http import HttpResponse
# from dwebsocket import accept_websocket
#
# def modify_message(message):
#     return message.lower()
#
# @accept_websocket
# def lower_case(request):
#     if not request.is_websocket(): #普通http请求
#         message = request.GET['message']
#         message = modify_message(message)
#         return HttpResponse(message)
#     else: #websocket请求
#         for message in request.websocket:
#             message = modify_message(message)
#             request.websocket.send(message)