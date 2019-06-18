"""
套接字属性演示
"""

from socket import *

# 创建套接字
s = socket()

# 设置套接字端口立即重用
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)

s.bind(('172.40.91.150',8888))
s.listen(3)
c,addr = s.accept()

print("地址类型:",s.family)
print("套接字类型:",s.type)
print("绑定的地址:",s.getsockname())
print("获取文件描述符:",s.fileno())
print("获取连接的客户端地址:",c.getpeername())
print("获取选项值:",
      s.getsockopt(SOL_SOCKET,SO_REUSEADDR))

c.recv(1024)