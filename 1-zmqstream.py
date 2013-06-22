import zmq
from zmq.eventloop.zmqstream import ZMQStream
context = zmq.Context()
socket = context.socket(zmq.DEALER)

def recv_callback(msg):
    # do stuff with msg
    pass

stream = ZMQStream(socket)
stream.on_recv(recv_callback)
