class Client:

    def __init__(self,id,name,ip_address,port_number,token=None):
        self.id=id
        self.name=name
        self.ip_address=ip_address
        self.port_number= port_number
        self.token=token

class ChatRoom:

    def __init__(self,id,name,ip_address,token=None):
        self.room_id=id
        self.room_name=name
        self.clients=[]

    #get the list of members of the chat room only for one of the members of the chat room
    def getMembers(self, client_Id):
        pass
    #add Member to the chat room.
    def addMember(self, client_Id):
        pass
    #remove member from the chat room.
    def removeMember(self, client_Id):
        pass






