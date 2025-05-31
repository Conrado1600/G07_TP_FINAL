
class Organo:
    """
    Representa un organo que esta disponible para transplantar.
    
    """
    
    def __init__(self, tipo):
        self.tipo = tipo
        self.fecha_hora_ablacion = None


    def set_fecha_ablacion(self, fecha_hora):
        """
        Establece la fecha y hora de ablacion del organo a transplantar.
        params: in objeto datetime que dice cuando se realizo la ablacion del organo.

        """
        self.fecha_hora_ablacion = fecha_hora


    def __str__(self):
        """
        Devuelve un texto sobre el organo.
        retorna el tipo de organo a transplantar.

        """
        return f"Organo: {self.tipo}"