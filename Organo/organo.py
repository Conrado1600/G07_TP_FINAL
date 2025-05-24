
class Organo:
    
    
    def __init__(self, tipo):
        self.tipo = tipo
        self.fecha_hora_ablacion = None


    def set_fecha_ablacion(self, fecha_hora):
        self.fecha_hora_ablacion = fecha_hora


    def __str__(self):
        return f"Organo: {self.tipo}"