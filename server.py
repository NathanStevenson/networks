# Server created for HW #0 with help from https://realpython.com/python-sockets/
# Not hard coded anymore uses commas and .split()

import socket, random

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 54321  # Port to listen on (non-privileged ports are > 1023)

name = "Server of Nathan Stevenson"
# DESKTOP-HPAPB47 is my laptops hostname
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            # decode the message if the number is > 100 then stop the program and cleanup socket
            message = data.decode()
            message = message.split(",")

            clientName = message[0]
            clientNumber = int(message[1])
            serverNumber = random.randint(1,100)
            sum = clientNumber + serverNumber
            print(name + " is connecting to the " + clientName)
            print("Server value is: " + str(serverNumber))
            
            conn.sendall(str(sum).encode())