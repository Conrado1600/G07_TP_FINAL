from Vehiculo.vehiculo import vehiculo

class Helicoptero (vehiculo):
    """
    Representa un vehiculo de tipo helicoptero utilizado para el transporte
    de organos a distancias medias, es heredada de vehiculo.

    """
    
    def __init__(self, velocidad):
        super().__init__ ("Helicoptero", velocidad)
    
    def calcular_tiempo_viaje(self, distancia, trafico):
        
        """
        Calcula el tiempo estimado de viaje en relacion con la distancia y el trafico (al ser aereo es 0)
        params: distancia total a recorrer, un valor que representa el nivel de trafico sobre el tiempo total.
        retorna un float que representa el tiempo estimado de viaje en horas.

        """

        return (distancia / self.velocidad).__add__(trafico) #cuenta para calcular tiempo de viaje en avion 