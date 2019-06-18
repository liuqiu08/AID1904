# 发送广播

from socket import *
from time import sleep

# 广播地址
dest = ('172.40.91.255',9900)

s = socket(AF_INET,SOCK_DGRAM)

s.setsockopt(SOL_SOCKET,SO_BROADCAST,1)

data = """
  **********************
    6.3  北京   晴
    望冬雪 赏夏花
    执子之手,不负韶华
  **********************
"""

while True:
  sleep(1)
  s.sendto(data.encode(),dest)

s.close()