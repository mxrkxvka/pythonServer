import socket
from _thread import *

message_size = int(input("Type size: "))
server = socket.socket()
server.bind(('192.168.195.220', 10000))
server.listen(10)

print("Chat server started.")

clients = list()

def client_thread(connection):
    print("Client connected")
    while True:
        try:
            data = connection.recv(message_size)
        except:
            print("No data! Client disconnect initiated")
            connection.close()
            clients.remove(connection)
            break
        if data:
            message = data.decode()
            print(f"Client sent: {message}")
            for client in clients:
                if client == connection:
                    continue
                print("Sending data to client")
                return_message = ('Server Message: ' + message).encode()
                client.send(return_message)  # Corrected this line

while True:
    connection, _ = server.accept()
    clients.append(connection)
    print(f"Number of connected clients: {len(clients)}")
    start_new_thread(client_thread, (connection,))
