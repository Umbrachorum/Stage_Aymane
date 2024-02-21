import map_generator
import joueurs
import clients
import socket

class PythonServerTCP:
    def __init__(self):
        self._tableau_joueurs = []
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
    def connexion(self) -> int:
        self._socket.bind(("127.0.0.1", 1234))
        self._socket.listen(1)
        client, adresse = self._socket.accept()
        while 42:
            buffer : str = input()
            if buffer == "exit":
                return 0
            elif buffer == "joueur :":
                print(buffer)
                """tmpjoueur = Joueurs()
                tmpjoueur.setName(name)
                self._tableau_joueurs.append(tmpjoueur)"""
        
if __name__ == "__main__":
    temp = PythonServerTCP()
    if temp.connexion() == 0:
        exit()