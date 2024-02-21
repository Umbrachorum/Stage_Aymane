from map_generator import *
from joueurs import *
import socket
from _thread import *
import copy

class PythonServerTCP:
    def __init__(self):
        self._tableau_joueurs = []
        self._tableau_peer = []
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._host = '127.0.0.1'
        self._port = 80
        self._ThreadCount = 0
        
    def client_handler(self, connection):
        connection.send(str.encode('You are now connected to the replay server... Type exit to stop'))
        while True:
            data = connection.recv(2048)
            peer = connection.getpeername()
            if len(self._tableau_peer) > 0:
                if peer != self._tableau_peer[0]:
                    self._tableau_peer.append(peer)
                    self._tableau_joueurs.append(Joueurs("Player 2"))
            else:
                self._tableau_peer.append(copy.copy(peer))
                self._tableau_joueurs.append(Joueurs("Player 1"))
            message = data.decode('utf-8')
            if message == "exit":
                connection.sendto(str.encode("Closing connection..."), peer)
                connection.close()
            if message == "map_generating":
                connection.sendto(str.encode(" Please enter cordinates to define the size of the map :"), peer)
                if len(self._tableau_peer) > 0:
                    if peer != self._tableau_peer[0]:
                        self.map_conception(connection)
                if len(self._tableau_peer) == 1:
                    self.map_conception(connection)
            if self.sorting_peer(connection) == 2:
                self.game_loop(connection)
            reply = f'Server: {message}'
            connection.sendall(str.encode(reply))
        self.client_handler(connection)
        connection.close()


    def accept_connections(self, ServerSocket):
        Client, address = ServerSocket.accept()
        print('Connected to: ' + address[0] + ':' + str(address[1]))
        start_new_thread(self.client_handler, (Client,))


    def start_server(self):
        ServerSocket = socket.socket()
        try:
            ServerSocket.bind((self._host, self._port))
        except socket.error as e:
            print(str(e))
        print(f'Server is listing on the port {self._port}...')
        ServerSocket.listen()

        while True:
            self.accept_connections(ServerSocket)
    
    def map_conception(self, connection):
        while(10):
            tmp = connection.recv(2048)
            ptmp = connection.getpeername()
            message = tmp.decode('utf-8')
            temp_buffer_without = message[1:]
            temp_buffer_without = temp_buffer_without[:-1]
            data1, data2 = temp_buffer_without.split(',')
            temp_arr = [int(data1), int(data2)]
            if type(temp_arr[0]) is int and type(temp_arr[1]) is int:
                self._tableau_joueurs[0].setCarte(generate_card(temp_arr))
                self._tableau_joueurs[0].insertInCard(indexation(temp_arr[0]))
                connection.sendto(str.encode(str(self._tableau_joueurs[0].getCarte())), ptmp)
            return
                        
                        
    def sorting_peer(self, connection):
        if len(self._tableau_peer) == 0:
            return 0
        if len(self._tableau_peer) == 1:
            connection.sendto(str.encode(str("Veuillez attendre qu'un autre joueur se connecte\n")), self._tableau_peer[0])
            return 1
        if len(self._tableau_peer) == 2:
            connection.sendall(str.encode(str("start")))
            return 2
        if len(self._tableau_peer) > 2:
            return -1
            
    def game_loop(self, connection):
        connection.sendto(str.encode(str("Veuillez initialiser le placement de vos bateaux s\'il vous plait :")), self._tableau_peer[0])
        message = connection.recv(2000)
        self._tableau_joueurs[0].setCarte(placement_bateaux_suite(self._tableau_joueurs[0].getCarte, str(message)))
        connection.sendto(str.encode(str("Veuillez initialiser le placement de vos bateaux s\'il vous plait :")), self._tableau_peer[1])
        message = connection.recv(2000)
        self._tableau_joueurs[1].setCarte(placement_bateaux_suite(self._tableau_joueurs[1].getCarte, str(message)))
        self._tableau_joueurs[0].setCarteAdversaire(self._tableau_joueurs[1].getCarte())
        self._tableau_joueurs[1].setCarteAdversaire(self._tableau_joueurs[0].getCarte())   
        connection.sendto(str.encode(str("Veuillez tirer s\'il vous plaît :")), self._tableau_joueurs[0])
        message = connection.recv(2000)
        
        
if __name__ == "__main__":
    temp = PythonServerTCP()
    if temp.start_server() == 0:
        exit()