"""
tcp粘包问题
"""

import socket

sockfd = socket.socket(socket.AF_INET,
                       socket.SOCK_STREAM)
sockfd.bind(('0.0.0.0', 8888))

sockfd.listen(3)

while True:
  print("Waiting for connect ...")
  connfd, addr = sockfd.accept()
  print("Connect from", addr)

  n = 0
  while n < 10:
    n += 1
    data = connfd.recv(5)
    print(data)

  connfd.close()  # 断开连接

#　关闭套接字
sockfd.close()
