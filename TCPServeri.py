import socket
import os
from _thread import *
from datetime import datetime
import random
from math import sqrt
import sys


ServerSocket = socket.socket()
host = '192.168.1.11'
port = 13000
ThreadCount = 0
try:
    ServerSocket.bind((host, port))
except socket.error as e:
    print(str(e))

print("Using TCP \n")
print('Waitiing for clients to connect..')
ServerSocket.listen(5)


def threaded_client(connection):
    connection.sendall(str.encode('Welcome to the Server\n'))
    try:
        while True:

            data = connection.recv(128)
        
            data2 = data.decode('utf-8')
            data1 = data2.split()
            data3 = str(data2).split(" ",1)
            noMethod = "You sent the method " + data2.upper() + " but we don't have this method , try the ones we have "
            if not data:
                break
            if data1[0] == 'IP_ADDRESS':
            
                connection.sendall(str(ip_address()).encode())

            elif data1[0] == 'PORT':
                connection.sendall(str(port()).encode())
            elif data1[0] == 'COUNT':
                if data2 == 'COUNT':
                        connection.sendall(str.encode("You must put a string after COUNT"))
                else:
                    string = data3[1]
                    vowels = 0
                    connection.sendall(str(findVow(string, vowels)).encode())
       
            elif data1[0] == 'REVERSE':
                if data2 == 'REVERSE':
                        connection.sendall(str.encode("You must put a string after REVERSE"))
                else:
                        stringu = str(data3[1])
                        connection.sendall(str(reverse(stringu)).encode())
            
            elif data1[0] == 'PALINDROME':
                if data2 == 'PALINDROME':
                        connection.sendall(str.encode("You must put a string after PALINDROME"))
                else:
                        s = str(data1[1])
                        connection.sendall(str(isPalindrome(s)).encode())
            
            elif data1[0] == 'TIME':
                connection.sendall(str(time()).encode())
            
            elif data1[0] == 'GAME':
                connection.sendall(str(game()).encode())
      
            elif data1[0] == 'GCF':
                if data2 == 'GCF':
                        connection.sendall(str.encode("You must put two numbers after GCF"))
                else:
                    x = int(data1[1])
                    y = int(data1[2])
                    connection.sendall(str(computeGCF(x, y)).encode())
            
            elif data1[0] == 'CONVERT':
                if data2 == 'CONVERT':
                        connection.sendall(str.encode("You must put a string and a number after CONVERT"))
                else:
                    option = str(data1[1])
                    number = float(data1[2])
                    connection.sendall(str(conversion(option,number)).encode())
            elif data1[0] == 'HYPOTENUSE':
                if data2 == 'HYPOTENUSE':
                    connection.sendall(str.encode("You must put catetes after HYPOTENUSE"))
                else:
                    a = float(data1[1])
                    b = float(data1[2])
                    connection.sendall(str(hypotenuse(a,b)).encode())
            elif data1[0] == 'BMI':
                if data2 == 'BMI':
                    connection.sendall(str.encode("You must put your height and weight after BMI"))
                else:
                    height = float(data1[1])
                    weight = float(data1[2])
                    connection.sendall(str(bmi(height,weight)).encode())
            elif data1[0] == 'QUIT':
                sys.exit(1)
            else:
                connection.sendall(noMethod.encode()) 
    except:
        connection.sendall("Invalid request".encode("ASCII"))

    connection.close()
        



def ip_address():
  
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    ip = f"IP Address of client is: {ip_address} \n  "
    if ip is None:
        return "Message should NOT contain null char\n"
        threaded_client
    else:
        print(ip)
        return ip
    
def port():
    port1 = ServerSocket.getsockname()[1]
    port2 = f"Client is using port: {port1} \n"
    
    if port2 is None:
        return "Message should NOT contain null char\n"
        threaded_client
    else:
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
    
    if current_time is None:
       return "Message should NOT contain null char\n"
       threaded_client
    else:
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
    c1 = "The hypotenuse of triangle with catetes" + str(a) + " and " + str(b) + " is: " + str(round(c, 2)) 

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

while True:
    Client, address = ServerSocket.accept()
    
    print('\n\nConnected to: ' + address[0] + ':' + str(address[1]))
    start_new_thread(threaded_client, (Client, ))
    ThreadCount += 1

    print('\n\n Client Number: ' + str(ThreadCount)+'\n')
ServerSocket.close()
