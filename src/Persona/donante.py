from Persona.persona import Persona

class Donante (Persona):
    
    organos_validos = ["corazon", "higado", "pancreas", "huesos","rinion", "pulmones", "intestino", "piel", "corneas"]
    
    def __init__(self, nombre, dni, fecha_nacimiento, sexo, telefono,tipo_sangre, centro_salud, fecha_hora_fallecimiento, fecha_hora_ablacion, organos):
        super().__init__(nombre, dni, fecha_nacimiento, sexo, telefono ,tipo_sangre, centro_salud)
        self.fecha_hora_fallecimiento = fecha_hora_fallecimiento
        self.fecha_hora_ablacion = fecha_hora_ablacion
        self.organos = organos

        for organo in organos:
            if organo.tipo.lower() not in self.organos_validos:
                raise ValueError(f"Este organo no es parte de la lista de organos validos:{organo.tipo}")