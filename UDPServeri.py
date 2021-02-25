import socketserver
import socket
import os
from _thread import *
from datetime import datetime
import random
from math import sqrt
import sys

print("Using UDP\n")

def ip_address():
       hostname = socket.gethostname()
       ip_address = socket.gethostbyname(hostname)
       ip = f"IP Address of client is: {ip_address} \n  "
       
       print(ip)
       return ip

def port():
    
    port1 = server.socket.getsockname()[1]
    port2 = f"Client is using port: {port1} \n"
    print(f"{port2}\n")
    return port2

def findVow(string, vowels): 
    vowels = 0
    consonants = 0
    spaces = 0

    for i in string:
        if(i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U'):
            vowels = vowels + 1
        if(i == ' '):
            spaces = spaces + 1
        else:
            continue
    consonants = len(string) - vowels - spaces
    length1 = "Received text has " + str(vowels) + "  vowels and " + str(consonants) + " consonants.\n"
         
    print(length1)
    return length1


def reverse(stringu):
    stringu1 = stringu.strip()
    stringu2 = stringu1 + "\n"
    print(stringu2)
    return stringu2


def reverseS(s): 
    return s[::-1] 
  
def isPalindrome(s): 
    rev = reverseS(s) 

    isP = "True\n"
    isNotP = "False\n"

    if (s == rev): 
        print(isP)
        return isP
    else:
        print(isNotP)
        return isNotP

def time():
    now = datetime.now()
    current_time = now.strftime("%m/%d/%Y, %H:%M:%S\n")
    print(current_time)
    return current_time


def game():
    x1=random.randint(1,35)
    x2=random.randint(1,35)
    x3=random.randint(1,35)
    x4=random.randint(1,35)
    x5=random.randint(1,35)
    x="(" + str(x1) + ", " + str(x2) + ", " + str(x3) + ", " + str(x4) + ", " + str(x5) + ")\n"
    print(x)
    return x

def computeGCF(x, y): 
  
    if x > y: 
        z = y 
    else: 
        z = x 
    for i in range(1, z+1): 
        if((x % i == 0) and (y % i == 0)): 
            gcd = i 
    an = "The result : " + str(gcd)+"\n"  
    print (an)
    return an 

def conversion(option,number):
    if(option == "cmToFeet"):
        feet = 0.0328 * number
        feet1 = round(feet, 2)
        feet2 = "Result: " + str(feet1) + " ft\n"
        print (feet2)
        return feet2
    elif(option == "FeetToCm"):
        cm = 30.48 * number
        cm1 = round(cm, 2)
        cm2 = "Result: " + str(cm1) + " cm\n"
        print (cm2)
        return cm2
    elif(option == "kmToMiles"):
        miles =  number * 0.62137119
        miles1 = round(miles, 2)
        miles2 = "Result: " + str(miles1) + " miles\n"
        print(miles2)
        return miles2
    elif(option == "MilesToKm"):
        km = number / 0.62137119
        km1 = round(km, 2)
        km2 = "Result: " + str(km1) + " km\n"
        print(km2)
        return km2
def hypotenuse(a,b):
    c = sqrt(a**2+b**2)
    c1 = "The hypotenuse of triangle with catetes " + str(a) + " and " + str(b) + " is: " + str(round(c, 2))

    print(c1)
    return c1

def bmi(height,weight):

    bmi = weight / height ** 2
    bmi = round(bmi, 2)
    if (bmi<18.5): 
        a = "A person with a BMI of " + str(bmi) + " is underweight "
        print(a)
        return a
    elif (bmi<24.9):
        b = "A person with a BMI of " + str(bmi) + " is normal weight "
        print(b)
        return b

    else:
        c = "A person with a BMI of " + str(bmi) + " is overweight "
        print(c)
        return c
class MyUDPHandler(socketserver.BaseRequestHandler):
   
   
    
    def handle(self):
        try:
            data = self.request[0].strip().decode('utf-8')
            socket = self.request[1]
            data1 = str(data).split(" ")
            data2 = str(data1[0])
            data3 = str(data).split(" ",1)
            noMethod = "You sent the method " + data.upper() + " but we don't have this method , try the ones we have "
       
            
            if str(data2) == "IP_ADDRESS":
                socket.sendto(ip_address().encode(), self.client_address)
            elif str(data2) == "PORT":
                socket.sendto(port().encode(), self.client_address)
            elif str(data2) == "COUNT":
                if data == "COUNT":
                    socket.sendto(str.encode("You must put a string after COUNT"), self.client_address)
                else:
                    string = data3[1]
                    vowels = 0
                    socket.sendto(findVow(string, vowels).encode(), self.client_address)
            elif data2 == 'REVERSE':
                if data == "REVERSE":
                    socket.sendto(str.encode("You should put a string after REVERSE"), self.client_address)
                else:
                    stringu = str(data3[1])
                    socket.sendto(reverse(stringu).encode(), self.client_address)
            elif data1[0] == 'PALINDROME':
                if data == "PALINDROME":
                    socket.sendto(str.encode("You should put a string after PALINDROME"), self.client_address)
                else:
                    s = str(data1[1])
                    socket.sendto(isPalindrome(s).encode(), self.client_address)
            elif data1[0] == 'TIME':
                socket.sendto(time().encode(), self.client_address)
            elif data1[0] == 'GAME':
                socket.sendto(game().encode(), self.client_address)
            elif data1[0] == 'GCF':
                if data == "GCF":
                    socket.sendto(str.encode("You should put two numbers after GCF"), self.client_address)
                else:
                    x = int(data1[1])
                    y = int(data1[2])
                    socket.sendto(computeGCF(x, y).encode(), self.client_address)
            elif data1[0] == 'CONVERT':
                if data == "CONVERT":
                    socket.sendto(str.encode("You should put a string and a number after CONVERT"), self.client_address)
                else:
                    option = str(data1[1])
                    number = float(data1[2])
                    socket.sendto(conversion(option,number).encode(), self.client_address)
            elif data1[0] == 'HYPOTENUSE':
                if data == "HYPOTENUSE":
                    socket.sendto(str.encode("You should put catetes after HYPOTENUSE"), self.client_address)
                else:
                    a = float(data1[1])
                    b = float(data1[2])
                    socket.sendto(hypotenuse(a,b).encode(), self.client_address)
            elif data1[0] == 'BMI':
                if data == "BMI":
                    socket.sendto(str.encode("You should put your height and weight after BMI"), self.client_address)
                else:
                    height = float(data1[1])
                    weight = float(data1[2])
                    socket.sendto(bmi(height,weight).encode(), self.client_address)
            elif data1[0] == "QUIT":
                sys.exit(1)
            else:
            
                socket.sendto(noMethod.encode(), self.client_address)
        except:
            socket.sendto("Invalid request".encode(), self.client_address)
if __name__ == "__main__":
    HOST, PORT = "192.168.1.11", 13000 
    server = socketserver.UDPServer((HOST, PORT), MyUDPHandler)
    server.serve_forever()
