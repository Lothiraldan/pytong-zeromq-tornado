from tornado.web import RequestHandler, asynchronous
from tornado import gen
from .utils import get_client

class AsyncProxyHandler(RequestHandler):

    @asynchronous
    @gen.coroutine
    def get(self):
        self.finish((yield gen.Task(call, 'project', 'list')))

@gen.coroutine
def call(service_name, action):
    client = get_client(service_name)
    raise gen.Return((yield gen.Task(client.call, action)))
