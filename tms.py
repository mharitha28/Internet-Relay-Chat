# simple illustration client/server pair; client program sends a string
# to server, which echoes it back to the client (in multiple copies),
# and the latter prints to the screen

# this is the server 6
import socket
import sys

# create a socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# associate the socket with a port
host = ’’ # can leave this blank on the server side
port = int(sys.argv[1])
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))

# accept "call" from client
s.listen(2)

#initialize v
v =''

#initialize client socket list
client_sockets = []

#determine number of clients, nc
nc = 2

#accept connection from clients
for i in range(nc):
    client, addr = s.accept()
    #set this client socket to non blocking mode
    client.setblocking(0)
    client_sockets.append(client)

#loop through clients, aways accepting input from whoever is ready, if any, until no clients are left
while (len(client_sockets)) > 0:
    #get next client, with effect of a circular queue
    client = client_sockets.pop(0)
    client_sockets.append(client)
    #check if client is alive or closed the connection
    try:
        k = client.recv(1)
            if k =='':
                client.close()
                client_sockets.remove(client)
            v += k
            client.send(v)
    except: pass

# close the connection
conn.close()
