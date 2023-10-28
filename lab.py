import re
import time
import socket
import requests
from urllib.parse import urlparse
import _thread
import ssl
import numpy as np

#解析请求
def getinformation(conn,fishi,addr):
    header = b''
    try:
        while True:
            data = conn.recv(4096)
            header = b"%s%s" % (header, data)
            if header.endswith(b'\r\n\r\n') or (not data):
                break
    except:
        pass
    #解析
    header=header.decode()
    while True:
        header += data.decode(errors="ignore")
        index=header.find('\n')
        if index >0:
            break
    firstLine=header[:index]
    a,b,c=firstLine.split()
    b=b.split(':443')
    d=b[0]
    #判断请求是https还是http
    if d[0:7]=='http://':
        dhost=urlparse(d).hostname
        dpath=urlparse(d).path
        if dpath == '/':
            d=dhost
        else:
            d=dhost
        port=80
    else :
        port=443
    #index = header.find('User-Age')
    #header = header[:index] + 'If-Modified-Since: Wed, 07 Dec 2023 12:18:20 GMT\r\n' + header[index:]
    #print(header)
    header=header.encode()

    if (d in blacklist) and(fishi==True):
             print('在黑名单！！：', d)
             header = b'GET http://www.hit.edu.cn/ HTTP/1.1\r\nHost: www.hit.edu.cn\r\nUser-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8\r\nAccept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2\r\nAccept-Encoding: gzip, deflate\r\nConnection: keep-alive\r\nUpgrade-Insecure-Requests: 1\r\n\r\nGET http://www.hit.edu.cn/ HTTP/1.1\r\nHost: www.hit.edu.cn\r\nUser-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8\r\nAccept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2\r\nAccept-Encoding: gzip, deflate\r\nConnection: keep-alive\r\nUpgrade-Insecure-Requests: 1\r\n\r\n'
             a = 'GET'
             port = 80
             d = 'www.hit.edu.cn'

    return header,a,d,c,port,b[0]

def switchdata(sock1,sock2):
    try:
        while True:
            data = sock1.recv(1024)

            if not data:
                return
            sock2.sendall(data)
    except:
        pass
def switchdata2(sock1,sock2,url):
    cont=b''
    try:

        while True:
            data = sock1.recv(1024)
            if not data:
                return
            sock2.sendall(data)
            cont += data

    finally:
        #print(cont)
        catchlist[url] = (cont, time.time())
        #json_dict = json.dumps(catchlist)
        #print(catchlist[url], end="okok")
        f = open("catch.npy", 'wb')
        np.save('catch.npy',catchlist)
        f.close()





def chuli(client,fishi,addr):
    timeout = 60
    client.settimeout(timeout)
    header,method,host,prot,port,url = getinformation(client,fishi,addr)
    asd=url
    if not header:
        client.close()
        return
    print('处理结果：', method, host, port, prot, url)
    #如果该请求已有缓存
    if url in catchlist:
        try:
          print('已有缓存！')
          data,_=catchlist[url]
          client.sendall(data)
        except:
            client.close()
    #如果该请求没有缓存
    if url not in catchlist:
        hostandport=(host,port)

        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            server.connect(hostandport)
            server.settimeout(timeout)
            if port==443 :
                data = b"HTTP/1.0 200 Connection Established\r\n\r\n"#https协议要先给客户机发送该内容才能正常完成请求
                client.sendall(data)
                _thread.start_new_thread(switchdata, (client, server))

            if port==80 :
                server.sendall(header)
            switchdata2(server, client,url)
        except:
            server.close()
            client.close()


def fishing():
    a=input('是否启用钓鱼？Y/N')
    if a=='Y':
       return True
    return False


catchlist={}

S = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
S.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
S.bind(('127.0.0.1', 8000))
S.listen(10)
fishi = fishing()
blacklist=['agefans.top','szsj.hit.edu.cn','tieba.baidu.com','www.programmercarl.com']
adbl=['127.0.0.1']
print('启动代理')
while True:

    conn, addr = S.accept()
    #print(addr[0])
    if addr[0]  in adbl:
        print('用户',addr[0],'禁止访问')
        S.close()
        break
    else:
     _thread.start_new_thread(chuli, (conn,fishi,addr[0]))











