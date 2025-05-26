from Vehiculo.vehiculo import vehiculo

class Vehiculos_terrestre(vehiculo):


    def __init__(self, velocidad):
        super().__init__("Terrestre", velocidad)

    def calcular_tiempo_viaje(self, distancia, nivel_trafico):
        return distancia / self.velocidad + nivel_trafico #cuenta para calcular tiempo de viaje     
