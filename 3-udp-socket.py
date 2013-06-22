import socket
from zmq.eventloop import ioloop

# Create udp socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sock.bind(('0.0.0.0', 5556))

# UDP Socket callback
def process_udp_socket(fd, events):
    data = sock.recv_from(1024)
    # do stuff with data

# Connect udp socket to ioloop
ioloop.IOLoop.instance().add_handler(sock.fileno(),
                                     process_udp_socket,
                                     ioloop.IOLoop.READ)
