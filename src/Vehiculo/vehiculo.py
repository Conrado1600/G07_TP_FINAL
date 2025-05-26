from abc import ABC, abstractmethod

class vehiculo (ABC):


    def __init__(self, tipo, velocidad):
        self.tipo = tipo
        self.velocidad = velocidad 
        self.viajes_realizados = []
    
    @abstractmethod


    def calcular_tiempo_viaje(self, distancia, nivel_trafico):
        pass


class Vehiculos_terrestre(vehiculo):


    def __init__(self, velocidad):
        super().__init__("Terrestre", velocidad)

    def calcular_tiempo_viaje(self, distancia, nivel_trafico):
        return distancia / self.velocidad + nivel_trafico #cuenta para calcular tiempo de viaje     

class Helicoptero (vehiculo):
    
    def __init__(self, velocidad):
        super().__init__ ("Helicoptero", velocidad)
    
    def calcular_tiempo_viaje(self, distancia):
        return distancia / self.velocidad  #cuenta para calcular tiempo de viaje en avion 
    
class Avion(vehiculo):

    def __init__(self, velocidad):
        super().__init__ ("Avion", velocidad)

    def calcular_tiempo_viaje(self, distancia):
        return distancia / self.velocidad 
 
