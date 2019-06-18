from socket import *
from select import select
import sys
class HttpServer:
    def __init__(self,host,port,dir):
        self.host = host
        self.port = port
        self.address = (host,port)
        self.dir = dir
        self.get_socket()
        self.bind()
        self.rlist = []
        self.wlist = []
        self.xlist = []
    def get_socket(self):
        self.sockfd = socket()
        self.sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    def bind(self):
        self.sockfd.bind(self.address)
    def start(self):
        self.sockfd.listen(3)
        self.rlist.append(self.sockfd)
        while True:
            rs,ws,xs  = select(self.rlist,self.wlist,self.xlist)
            for r in rs:
                if r ==self.sockfd:
                    c,addr = self.sockfd.accept()
                    self.rlist.append(c)
                else:
                    self.handle(r)
    def handle(self,c):
        data = c.recv(1024)
        if not data:
            self.rlist.remove(c)
            c.close()
            return
        filename = data.splitlines()[0]
        info = filename.decode().split(" ")[1]
        if info =="/" or info[-5:]==".html":
            self.get_html(info,c)
        else:
            self.get_out(info,c)
    def get_html(self,info,c):
        if info =="/":
            filename = self.dir +"/index.html"
        else:
            filename = self.dir + info
        try:
            f = open(filename)
        except KeyboardInterrupt:
            sys.exit("服务器退出")
        except Exception:

            data = "HTTP1.0 404 sorry\r\n"
            data += "\r\n"
            data += "sorry"
        else:
            data = "HTTP1.0 200 OK\r\n"
            data += "\r\n"
            data += f.read()
        finally:
            c.send(data.encode())

    def get_out(self,info,c):
        filename = self.dir + info

        try:
            f = open(filename)
        except KeyboardInterrupt:
            sys.exit("服务器退出")
        except Exception :

            data = "HTTP1.0 404 sorry\r\n"
            data += "\r\n"
            data += "sorry"
        else:
            data = "HTTP1.0 200 OK\r\n"
            data += "\r\n"
            data += f.read()
        finally:
            c.send(data.encode())
















if __name__  =="__main__":
    HOST = "0.0.0.0"
    PORT = 8888
    DIR = "./static"
    httpserver = HttpServer(HOST,PORT,DIR)
    httpserver.start()








