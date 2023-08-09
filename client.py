from base64 import encode
from email import message
from logging.handlers import SocketHandler
from re import L
import socket
import socketserver
import threading
import random

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.bind(("localhost", random.randint(8000, 9000)))

name = input("nickname: ")

def receive():
    while True:
        try:
            message, _ = client .recvfrom(1024)
            print(message.decode())
        except:
            pass

t = threading.Thread(target = receive)
t.start()

client.sendto(f"SIGNUP_TAB: {name}".encode(), ("localhost", 9999))

while True:
    message = input("")
    if message == "!q":
        exit()
    else:
        client.sendto(f"{name}: {message}".encode(), ("localhost", 9999))
