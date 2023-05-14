# Nathan Stevenson SMTP Server for CS 4457
# IP Address of Metasploitable is INET addr: 192.168.233.129, email comes in on port 25

#!/usr/bin/env python3

# Include needed libraries. Do _not_ include any libraries not included with
# Python3 (i.e. do not use `pip` use 'pip3' instead of installs).
from socket import *

HOST = "127.0.0.1"
PORT = 25
BUFFER_SIZE = 1024

# Acting as the SMTP client. The email server is always open, we just connecting to it and sending a message
# Establish a TCP connection with the mail server.
s = socket(AF_INET, SOCK_STREAM) #Prepare a sever socket
s.connect((HOST, PORT))

# Read greeting from the server
data = s.recv(BUFFER_SIZE)
response = data.decode('utf-8')

if not response.startswith('220'):
    raise Exception('220 reply not received from server.')

# Send HELO command and get server response.
cmd_HELO = 'HELO alice\r\n'
print(cmd_HELO)
s.send(cmd_HELO.encode())

response = s.recv(4096).decode('utf-8')
print(response)

if not response.startswith('250'):
    raise Exception('250 reply not received from server.')


# Send MAIL FROM command.
cmd_Mail_From = 'MAIL FROM: <nts7bcj@virginia.edu>\r\n'
s.send(cmd_Mail_From.encode())

response = s.recv(4096).decode('utf-8')

if not response.startswith('250'):
    raise Exception('250 reply not received from server.')

# Send RCPT TO command. You will send to <sys> which account on the VM.
cmd_RCPT = 'RCPT TO: <sys>\r\n'
s.send(cmd_RCPT.encode())

response = s.recv(4096).decode('utf-8')

if not response.startswith('250'):
    raise Exception('250 reply not received from server.')

# Send DATA command.
cmd_DATA = 'DATA\r\n'
s.send(cmd_DATA.encode())

response = s.recv(4096).decode('utf-8')

if not response.startswith('354'):
    raise Exception('354 reply not received from server.')

# Send message data.
cmd_message = 'Hi Marques, How is the weather? Nathaniel.\r\n'

# End with line with a single period.
cmd_dot = '.\r\n'
s.send((cmd_message + cmd_dot).encode())

response = s.recv(4096).decode('utf-8')
if not response.startswith('250'):
    raise Exception('250 reply not received from server.')
# Send QUIT command.
cmd_QUIT = 'QUIT\r\n'
s.send(cmd_QUIT.encode())

response = s.recv(4096).decode('utf-8')
if not response.startswith('221'):
    raise Exception('221 reply not received from server.')

# Close the socket when finished.
s.close()
