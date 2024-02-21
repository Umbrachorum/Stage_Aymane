
import map_generator
class Joueurs:
    def __init__(self):
        self._nom : str= ""
        self._carte : list= []
        self._carte_adversaire : list = []
    
    def setName(self, name : str):
        self._nom = name
    
    def getName(self) -> str:
        return self._nom
    
    def setCarte(self, liste : list):
        self._carte = liste
        
    def getCarte(self) -> list:
        return self._carte
    
    def setCarteAdversaire(self, liste : list):
        self._carte_adversaire = liste
        
    def getCarteAdversaire(self) -> list:
        return self._carte_adversaire
    
    
        