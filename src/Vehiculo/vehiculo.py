from abc import ABC, abstractmethod

class vehiculo (ABC):


    def __init__(self, tipo, velocidad):
        self.tipo = tipo
        self.velocidad = velocidad 
        self.viajes_realizados = []
    
    @abstractmethod


    def calcular_tiempo_viaje(self, distancia, nivel_trafico):
        pass
