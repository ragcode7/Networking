import socket

s = socket.socket()
host = socket.gethostname()
port = 5001

s.connect((host, port))
s.send(bytes("Client 1","utf-8"))

print(s.recv(1024).decode())#prints the inside booking fn

k1=s.recv(1024).decode()
print(k1)#welcome+enter name
i = input()
s.send(bytes(i,"utf-8"))

k1=s.recv(1024).decode()
print(k1)#enter phone number
i = input()
s.send(bytes(i,"utf-8"))

k1=s.recv(1024).decode()
print(k1)#enter door number
i = input()
s.send(bytes(i,"utf-8"))

k1=s.recv(1024).decode()
print(k1)#enter address line 1
i = input()
s.send(bytes(i,"utf-8"))

k1=s.recv(1024).decode()
print(k1)#enter address line 2
i = input()
s.send(bytes(i,"utf-8"))

k1=s.recv(1024).decode()
print(k1)#enter city
i = input()
s.send(bytes(i,"utf-8"))

k1=s.recv(1024).decode()
print(k1)#enter checkin date
i = input()
s.send(bytes(i,"utf-8"))


k1=s.recv(1024).decode()
print(k1)#enter checkout date
i = input()
s.send(bytes(i,"utf-8"))

k1=s.recv(1024).decode()
print(k1)#enter room type
i = input()
s.send(bytes(i,"utf-8"))

k1=s.recv(1024).decode()
print(k1)#no.of days
i = input()
s.send(bytes(i,"utf-8"))

k1=s.recv(15000).decode()
print(k1)