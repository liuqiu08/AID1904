from socket import *

s = socket()
s.bind(('0.0.0.0',8888))
s.listen(3)

c,addr = s.accept()
print("Connect from",addr)

# 以二进制写入
f = open('mm.jpg','wb')

#循环接收内容,写入文件
while True:
  data = c.recv(1024)
  if data == b'##':
    break
  f.write(data)

data = c.recv(1024)
print(data.decode())

f.close()
c.close()
s.close()
