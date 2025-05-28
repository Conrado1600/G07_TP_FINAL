from Vehiculo.vehiculo import vehiculo

class Helicoptero (vehiculo):
    
    def __init__(self, velocidad):
        super().__init__ ("Helicoptero", velocidad)
    
    def calcular_tiempo_viaje(self, distancia, trafico):
        return distancia / self.velocidad  + trafico #cuenta para calcular tiempo de viaje en avion 