from audioop import add
from email import message
from http import client, server
from re import S
import socket
import threading
import queue

msg = queue.Queue()
clients = []

server =  socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(("localhost",  9999))

def receive():
    while True:
        try:
            message, addr = server.recvfrom(1024)
            msg.put((message, addr))
        except:     
            pass

def broadcast():
    while True:
        while not msg.empty():
            message, addr = msg.get()
            print(message.decode())
            if addr not in clients:
                clients.append(addr)
            for client in clients:
                try:
                    if message.decode().startswith("SIGNUP_TAG: "):
                        name = message.decode()[message.decode().index(":")+1]
                        server.sendto(f"{name} joined".encode(), client)
                    else:
                        server.sendto(message, client)
                except:
                    clients.remove(client)

t1 = threading.Thread(target = receive)
t2 = threading.Thread(target = broadcast)

t1.start()
t2.start()

