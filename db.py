from pymongo import MongoClient
import socket
# Includes database operations
class DB:


    # db initializations
    def __init__(self):
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client['p2p-chat']
        self.tcpClientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        

    # checks if an account with the username exists
    def is_account_exist(self, username):
        if self.db.accounts.count_documents({'username': username}) > 0:
            return True
        else:
            return False
    

    # registers a user
    def register(self, username, password):
        account = {
            "username": username,
            "password": password
        }
        self.db.accounts.insert_one(account)


    # retrieves the password for a given username
    def get_password(self, username):
        return self.db.accounts.find_one({"username": username})["password"]


    # checks if an account with the username online
    def is_account_online(self, username):
        if self.db.online_peers.count_documents({"username": username}) > 0:
            return True
        else:
            return False

    
    # logs in the user
    def user_login(self, username, ip, port):
        online_peer = {
            "username": username,
            "ip": ip,
            "port": port
        }
        self.db.online_peers.insert_one(online_peer)
    

    # logs out the user 
    def user_logout(self, username):
        self.db.online_peers.delete_one({"username": username})
    

    # retrieves the ip address and the port number of the username
    def get_peer_ip_port(self, username):
        res = self.db.online_peers.find_one({"username": username})
        return (res["ip"], res["port"])
    def is_room_exist(self, room_name):
        return self.db.chat_rooms.count_documents({'room_name': room_name}) > 0

    def create_room(self, room_name):
        room = {
            "room_name": room_name,
            "users": []
        }
        self.db.chat_rooms.insert_one(room)

    def add_user_to_room(self, username, room_name):
        self.db.chat_rooms.update_one({"room_name": room_name}, {"$push": {"users": username}})

    def remove_user_from_room(self, username, room_name):
        self.db.chat_rooms.update_one({"room_name": room_name}, {"$pull": {"users": username}})
        
    def connect_tcp(self, ip, port):
        self.tcpClientSocket.connect((ip, port))
    def send_data(self, data):
        # Sending data to the database using TCP
        self.tcpClientSocket.send(data.encode())

    def receive_data(self):
        # Receiving data from the database using TCP
        received_data = self.tcpClientSocket.recv(1024)
        return received_data.decode()

    def close_connection(self):
        self.tcpClientSocket.close()
    
