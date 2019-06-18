"""
tcp 粘包
"""

from socket import *


sockfd = socket()

server_addr = ("127.0.0.1",8989)
sockfd.connect(server_addr)

while True:
  sockfd.send(b'hello')

sockfd.close()


