from tornado.web import RequestHandler, asynchronous
from tornado.httpclient import AsyncHTTPClient
from tornado import gen

class AsyncProxyHandler(RequestHandler):

    @asynchronous
    @gen.coroutine
    def get(self):
        http_client = AsyncHTTPClient()
        response = yield http_client.fetch("http://example.com")
        self.finish(response.content)
