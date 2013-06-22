import zmq
from zmq.eventloop.zmqstream import ZMQStream

class ZeroMQSubConsumer(object):

    def __init__(self):
        context = zmq.Context()
        self.sub_socket = context.socket(zmq.SUB)
        self.sub_socket.setsockopt(zmq.SUBSCRIBE, '')
        self.stream = ZMQStream(self.sub_socket)
        self.stream.on_recv(self.process_sub)

    def connect_to_endpoint(self, endpoint):
        self.sub_socket.connect(endpoint)

    def process_sub(self, sub_message):
        # Sub_message contains [endpoint, message]
        endpoint, message = sub_message
        for client in WebSocketHandler.clients[endpoint]:
            client.write_message(message)
