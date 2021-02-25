import socket
import sys

HOST, PORT = "192.168.1.11", 13000 

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    data = input("Operacioni (IP_ADDRESS, PORT, COUNT, REVERSE, PALINDROME, TIME, GAME, GCF, CONVERT, HYPOTENUSE, BMI)? ")

    sock.sendto(bytes(data + "\n", "utf-8"), (HOST, PORT))
    received = str(sock.recv(128), "utf-8")
    print("Received: {}".format(received))