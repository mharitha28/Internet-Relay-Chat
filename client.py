####################################################################################################################################
#                                            Haritha Munagala, Susham Yerabolu                                                     #
#                                            CS 594 Internetworking Protocols                                                      #
#                                                     Spring 2018                                                                  #
#                                            Internet Relay Chat Group Project                                                     #
####################################################################################################################################
import socket
import sys
import select
import CONSTANTS
import json
import os

class IRCClient():
    def __init__(self,name):
        self.name = name
        # connect to server
        self.server_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_connection.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_connection.connect((CONSTANTS.HOST, CONSTANTS.PORT))
        
        #Register the client with the provided name
        serverMsg = {}
        serverMsg["command"] = "NICKNAME"
        serverMsg["name"] = self.name
        self.server_connection.send(json.dumps(serverMsg).encode())
        print("You are now connected to Server!!")
    #end __init__
    
    # Prompt format for the client to enter their commands
    def prompt(self):
        print("<" + self.name + ">", "end = ''", "flush=False")
    #end prompt
    
    # Create a room on the IRC server as requested by client
    def createRoom(self, roomName):
        serverMsg = {}
        serverMsg["command"] = "CREATEROOM"
        serverMsg["roomName"] = roomName
    #end
    
    # Client requests a list of rooms from server
    def listRooms(self):
        serverMsg = {}
        serverMsg["command"] = "LISTROOMS"
        self.server_connection.send(json.dumps(serverMsg))
    #end
    
    # Client requests to join a room
    def joinRoom(self, roomName):
        serverMsg = {}
        serverMsg["command"] = "JOINROOM"
        serverMsg["roomName"] = roomName
        self.server_connection.send(json.dumps(serverMsg))
    #end
    
    # Client requests to leave a room
    def leaveRoom(self, roomName):
        serverMsg = {}
        serverMsg["command"] = "LEAVEROOM"
        serverMsg["roomName"] = roomName
        self.server_connection.send(json.dumps(serverMsg))
    #end
    
    # Client requests to list members of a room
    def listRoomClients(self, roomName):
        serverMsg = {}
        serverMsg["command"] = "LISTROOMCLIENTS"
        serverMsg["roomName"] = roomName
        self.server_connection.send(json.dumps(serverMsg))
    
    #Client requests to send messages to a room
    def msgRoom(self, roomName):
        serverMsg = {}
        serverMsg["command"] = "MSGROOM"
        serverMsg["roomName"] = roomName
        self.server_connection.send(json.dumps(serverMsg))
    #end
    
    def run(self):
        # simple illustration client/server pair; client program sends a string
        # to server, which echoes it back to the client (in multiple copies),
        # and the latter prints to the screen

        # this is the client 6
        
        socket_list = [sys.stdin, self.server_connection]
        
        #Prompt the client for their command
        self.prompt()
        
        #File transfer parameters
        FILE_TRANSFER_MODE = False
        FILE_NAME = None
        FILE_SIZE = None
        
        while True:
            read, write, error = select.select(socket_list, [], [])
            for s in read:
                #Incoming server response
                if s in self.server_connection:
                    #Get server response and display
                    message = s.recv(1024).decode()
    
                    #No message indicates the server is down
                    if not message:
                        print("Server is down!!")
                        sys.exit(1)
                    
                    # Print response from server and ask for client input
                    else:
                        print("\n" + message)
                        self.prompt()
                elif s in sys.stdin:
                    #Client sends a command to server, parse it and run the appropriate code for that respective command
                    message = sys.stdin.readline().replace("\n","")
                    try:
                        command = message.split(" ", 1)[0]
                            
                        # Client wants to create a room
                        if command == "CREATEROOM":
                            roomName = message.split(" ", 1)[1]
                            self.createRoom(roomName)

                        # Client wants a list of rooms
                        elif command == "LISTROOMS":
                            self.listRooms()
                        
                        # Client wants to join a room
                        elif command == "JOINROOM":
                            roomName = message.split(" ", 1)[1]
                            self.joinRoom(roomName)
                        
                        # Client wants to leave a room
                        elif command == "LEAVEROOM":
                            roomName = message.split(" ", 1)[1]
                            self.leaveRoom(roomName)
                                
                        # Client wants a list of members in a room
                        elif command == "LISTROOMCLIENTS":
                            roomName = message.split(" ", 1)[1]
                            self.listRoomClients(roomName)
                        
                        
                        # Client wants to send a message to a room
                        elif command == "MSGROOM":
                            parse = message.split(" " ,2)
                            self.msgRoom(parse[1], parse[2])
                        
                        # Client wants to terminate the program
                        elif command == "EXIT":
                            print("Exiting from Chat")
                            self.server_connection.close()
                            sys.exit(0)

                        # Invalid Command
                        else:
                            print("Invalid command! Please try again with a valid command.")
                            self.promt()
                        
                # Few arguments were given in the command
                    except IndexError as ie:
                        print("Command received too few arguments! Please try again!")
                        self.prompt()
                        continue
        

    #end run
#end IRCClient

def main():
    name = input("Please enter your name: ")
    client = IRCClient(name)
    client.run()
#end main
    
if __name__ == "__main__":
    main()
