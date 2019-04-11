import uuid
import json
import tornado.ioloop
import tornado.web
import tornado.websocket

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')

class ChatHandler(tornado.websocket.WebSocketHandler):
    #用户存储当前聊天室用户
    waiters = set()
    #用于存储历史消息
    messages = []

    def open(self):
        """
        客户端连接成功时，自动执行
        :return:
        """
        ChatHandler.waiters.add(self)
        uid = str(uuid.uuid4())
        self.write_message(uid)

        for msg in ChatHandler.messages:
            content = self.render_string('message.html',**msg)
            self.write_message(content)

    def on_message(self, message):
        """
        客户端发送消息时，自动执行
        :param message:
        :return:
        """
        msg = json.loads(message)
        ChatHandler.messages.append(message)
        for client in ChatHandler.waiters:
            content = client.render_string('message.html',**msg)
            client.write_message(content)

    def on_close(self):
        """
        客户端关闭连接时，自动执行
        :return:
        """
        ChatHandler.waiters.remove(self)

def run():
    settings={
        'template_path':'templates',
        'static_path':'static',
    }
    application = tornado.web.Application([
        (r"/",IndexHandler),
        (r"/chat",ChatHandler),
    ],**settings)
    application.listen(8003)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    run()
