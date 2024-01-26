GNU nano 5.2                    ali.py
import os
os. system ('clear')
import socket
import sys
print ("Welcome back as Capitano")
#إستخراج ip الموقع
print("Enter The host name : ")
hostname = input()
ip = socket.gethostbyname(hostname)
print('Host Name Is : ' , hostname,  '\n'  'Target Ip Is : ', ip)
