from tornado.web import RequestHandler, asynchronous
from tornado import gen

from client import ZMQClient
client = ZMQClient('tcp://127.0.0.1:5555')

class GenAsyncHandler(RequestHandler):

    @asynchronous
    @gen.coroutine
    def get(self):
        response = yield gen.Task(client.call, "ping")
        self.finish(response)
