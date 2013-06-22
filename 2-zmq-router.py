import zmq
from zmq.eventloop.zmqstream import ZMQStream
context = zmq.Context()
socket = context.socket(zmq.ROUTER)
socket.bind('tcp://0.0.0.0:8080')

def recv_callback(raw_msg):
    sid, msg = raw_msg
    # sid is socket id
    # do stuff with msg
    response = 42
    socket.send_multipart([sid, response])

stream = ZMQStream(socket)
stream.on_recv(recv_callback)
