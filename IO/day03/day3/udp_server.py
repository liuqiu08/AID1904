"""
UDP 套接字服务端
重点代码
"""

from socket import *

# 创建套接字
sockfd = socket(AF_INET, SOCK_DGRAM)

# 绑定地址
server_addr = ('127.0.0.1', 8888)
sockfd.bind(server_addr)

# 收发消息
while True:
  data, addr = sockfd.recvfrom(1024)
  print("收到的消息:", data.decode())
  sockfd.sendto(b'Receive', addr)

# 关闭套接字
sockfd.close()
