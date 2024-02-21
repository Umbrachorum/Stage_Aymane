import socket
from map_generator import simple_print
import ast

class Client:
    def __init__(self):
        self._host = '127.0.0.1'
        self._port = 80
        self._ClientSocket = socket.socket()
        self._state_init = True
        self._state_game = False
        
    def boucle_client(self):
        print('Waiting for connection')
        try:
            self._ClientSocket.connect((self._host, self._port))
        except socket.error as e:
            print(str(e))
        Response = self._ClientSocket.recv(2048)
        print(Response)
        while True:
            if self._state_init == True and self._state_game == False:
                Input = input('Your message: ')
                self._ClientSocket.send(str.encode(Input))
            Response = self._ClientSocket.recv(100000)
            response = Response.decode('utf-8')
            response = response.strip()
            if(len(response) > 0):
                if response[0] == "[":
                    tmp = ast.literal_eval(response)
                    simple_print(tmp)
                    self._state_init = False
                    self._state_game = True
            if response == "start":
                self._state_init = True
            if (len(response) > 0):
                #print(Response.decode('utf-8'))
                if response == "Veuillez attendre qu'un autre joueur se connecte":
                    self._state_init = False
                    print(response)
            #print(Response.decode('utf-8'))
            
    def client_close(self):
        self._ClientSocket.close()
        
    def parser(carte : str) -> list:
        pass

if __name__ == "__main__":
    temp = Client()
    temp.boucle_client()