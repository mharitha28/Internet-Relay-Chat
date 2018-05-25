"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                            Haritha Munagala, Susham Yerabolu
                                            CS 594 Interne
                                                    Spring 2018
                                                    Homework 2
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# simple illustration client/server pair; client program sends a string
# to server, which echoes it back to the client (in multiple copies),
# and the latter prints to the screen

# this is the client 6
import socket
import sys

# create a socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to server
host = sys.argv[1] # server address
port = int(sys.argv[2]) # server port
s.connect((host, port))

s.sendall(sys.argv[3]) # send test string 19
# read echo
i=0
while(1):
    #get letter
    k = raw_input('Send some message')
    s.send(k)
    if k == '': break
    data = s.recv(1024) # read up to 1024 bytes
    #i += 1
    #if (i < 5):
    #    print data
    #if not data: # if end of data, leave loop
    #    break
    #print 'received', len(data), 'bytes'
    print(data)

# close the connection
s.close()

