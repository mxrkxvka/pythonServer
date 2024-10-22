import socket
from _thread import *

client_socket = socket.socket()
client_socket.connect(('192.168.195.220', 10000))


def input_thread(socket):
    while True:
        output = socket.recv(1024)
        print(output.decode())


while True:
    start_new_thread(input_thread, (client_socket,))
    msg = input()
    if msg:
        client_socket.send(msg.encode())
