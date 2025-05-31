from Vehiculo.vehiculo import vehiculo

class Avion(vehiculo):
    """
    Representa un vehiculo de tipo avion, para transportar organos a largas distancias.
    Heredada de vahiculo

    """

    def __init__(self, velocidad):
        super().__init__ ("Avion", velocidad)

    def calcular_tiempo_viaje(self, distancia, trafico):
        """
        Calcula el tiempo estimado de viaje en relacion con la distancia y el trafico (al ser vehiculo aereo es 0)
        params: distancia total a recorrer, un valor que representa el nivel de trafico sobre el tiempo de viaje.
        retorna un float que representa el tiempo estimado de viaje en horas
        
        """
        return distancia / self.velocidad + trafico
 