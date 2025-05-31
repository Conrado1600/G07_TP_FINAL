from abc import ABC, abstractmethod

class vehiculo (ABC):
    """
    Esta clase abstracta representa un vehiculo utilizado para
    transportar los organos a donar entre los centros de salud.

    """


    def __init__(self, tipo, velocidad):
        """
        Inicializa un vehiculo con su tipo y velocidad como parametros.
        params: lista de los tipos de vehiculo, y un numero que representa
        la velocidad promedio del vehiculo.

        """
        self.tipo = tipo
        self.velocidad = velocidad 
        self.viajes_realizados = []
    
    @abstractmethod


    def calcular_tiempo_viaje(self, distancia, nivel_trafico):
        """
        Este metodo debe ser implementado por cada subclase para calcular el tiempo estimado de viaje.
        params: la distancia que recorre el vehiculo en kilometros, un valor que representa el 
        efecto del trafico sobre el tiempo de viaje.
        retorna el tiempo estimado de viaje en horas.

        """
        pass
