import zmq
from zmq.eventloop.zmqstream import ZMQStream

class ZMQClient(object):

    def __init__(self, endpoint):
        self.endpoint = endpoint

    def call(self, message, callback):
        context = zmq.Context()
        socket = context.socket(zmq.DEALER)
        socket.connect(self.endpoint)
        stream = ZMQStream(socket)
        stream.on_recv(callback)

        socket.send(message)
