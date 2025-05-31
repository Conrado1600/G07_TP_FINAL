from Vehiculo.vehiculo import vehiculo

class Vehiculos_terrestre(vehiculo):
    """
    Representa un vehiculo de tipo terrestre, utilizado para el transporte 
    de organos a corta distancia, heredada de vehiculo

    """


    def __init__(self, velocidad):
        super().__init__("Terrestre", velocidad)

    def calcular_tiempo_viaje(self, distancia, nivel_trafico):
        
        """
        Calcula el tiempo estimado del viaje en relacion con la distancia y el nivel de trafico.
        params: la distancia a recorrer, un valor que representa el nivel de trafico en el timepo total de viaje.
        retorna un valor float que representa el tiempo estimado de viaje en horas.

        """

        return distancia / self.velocidad + nivel_trafico #cuenta para calcular tiempo de viaje     
