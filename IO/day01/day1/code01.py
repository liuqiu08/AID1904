from socket import *
import sys
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(("0.0.0.0",8888))
s.listen(3)
while True:
    try:
        c,addr = s.accept()
    except KeyboardInterrupt:
        sys.exit("服务器退出")
    except Exception as e:
        print(e)
    while True:
        data= c.recv(1024)
        if not data:
            break
        c.send(b"OK")




















