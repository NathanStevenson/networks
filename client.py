# client created for HW #0 with help from https://realpython.com/python-sockets/

import socket, sys

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 54321  # The port used by the server

number = sys.argv[1]
name = "Client of Nathan Stevenson "

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    message = name + "," + number
    s.sendall(message.encode())
    data = s.recv(1024)

print("Sum of Values: " + data.decode())