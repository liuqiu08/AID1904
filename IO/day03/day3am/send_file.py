from socket import *
import time

s = socket()
s.connect(('127.0.0.1',8888))

f = open('img.jpg','rb')

# 读取内容,将其发送
while True:
  data = f.read(1024)
  if not data:
    time.sleep(0.1)
    s.send(b'##')
    break
  s.send(data)

time.sleep(0.1)
s.send("发送完毕".encode())

f.close()
s.close()