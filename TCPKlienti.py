import socket
import sys
ClientSocket = socket.socket()
host = '192.168.1.11'
port = 13000

print('Waiting for connection..')
try:
    ClientSocket.connect((host, port))
except socket.error as e:
    print(str(e))

Response = ClientSocket.recv(128)
while True:
    Input = input("Operacioni (IP_ADDRESS, PORT, COUNT, REVERSE, PALINDROME, TIME, GAME, GCF, CONVERT, HYPOTENUSE, BMI)? ")
    ClientSocket.send(str.encode(Input))
    Response = ClientSocket.recv(1024)
    print(Response.decode('utf-8'))

ClientSocket.close()