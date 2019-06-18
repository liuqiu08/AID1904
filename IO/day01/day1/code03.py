from socket import *
import os
import signal
HOST = "0.0.0.0"
PORT =8888
ADDR = (HOST,PORT)
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(ADDR)
s.listen(3)
signal.signal(signal.SIGCHLD,signal.SIG_IGN)
def handle(c):
    while True:
        data = c.recv(1024)
        if not data:
            break
        print(data.decode())
        c.send(b"OK")
    c.close()

while True:
    try:
        c,addr = s.accept()
    except KeyboardInterrupt:
        print("服务器退出")
        os._exit(0)
    except Exception as e:
        print(e)
    pid = os.fork()
    if pid ==0:
        s.close()
        handle(c)
        os._exit(0)
    c.close()










