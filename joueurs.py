
import map_generator
class Joueurs:
    def __init__(self, name):
        self._nom : str= name
        self._carte : list= []
        self._carte_adversaire : list = []
    
    def setName(self, name : str):
        self._nom = name
    
    def getName(self) -> str:
        return self._nom
    
    def insertInCard(self, lign: list):
        self._carte.insert(0, lign)
        
    def setCarte(self, liste : list):
        self._carte = liste
        
    def getCarte(self) -> list:
        return self._carte
    
    def setCarteAdversaire(self, liste : list):
        self._carte_adversaire = liste
        
    def getCarteAdversaire(self) -> list:
        return self._carte_adversaire
    
    
        