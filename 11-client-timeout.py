import zmq
from zmq.eventloop.zmqstream import ZMQStream
from zmq.eventloop import ioloop

class ZMQClient(object):

    def __init__(self, endpoint):
        self.endpoint = endpoint

    def call(self, message, callback):
        context = zmq.Context()
        socket = context.socket(zmq.DEALER)
        socket.connect(self.endpoint)
        stream = ZMQStream(socket)
        loop = ioloop.IOLoop.instance()

        def timeout_callback():
            stream.stop_on_recv()
            stream.close()
            raise TimeoutError('Call timeout for message', message)
        timeout = loop.add_timeout(timedelta(seconds=5), timeout_callback)

        def recv_callback(msg):
            loop.remove_timeout(timeout)
            stream.stop_on_recv()
            stream.close()
            callback(msg)
        stream.on_recv(callback)

        socket.send(message)
