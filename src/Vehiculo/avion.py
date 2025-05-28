from Vehiculo.vehiculo import vehiculo

class Avion(vehiculo):

    def __init__(self, velocidad):
        super().__init__ ("Avion", velocidad)

    def calcular_tiempo_viaje(self, distancia, trafico):
        return distancia / self.velocidad + trafico
 