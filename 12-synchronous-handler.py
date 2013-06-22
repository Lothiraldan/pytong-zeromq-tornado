import tornado.ioloop
from tornado.web import RequestHandler
from models import User

class MainHandler(RequestHandler):
    def get(self):
        user = User.find_one(id='Toto')
        self.write("Hello %s" % user.name)
