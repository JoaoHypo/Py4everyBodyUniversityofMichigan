import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)
# its obligated to have \r b4 \n the combo \r\n is the same as ENTER
while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    #print(data)
    print(data.decode(),end='')

mysock.close()
