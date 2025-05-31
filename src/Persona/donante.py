from Persona.persona import Persona

class Donante (Persona):
    """
    Esta clase respresenta a un Donante de órgano (persona fallecida), heredado de la
    clase Persona e incluyendo información sobre el órgano a donar.
    """
    
    organos_validos = ["corazon", "higado", "pancreas", "huesos","rinion", "pulmones", "intestino", "piel", "corneas"]
    
    def __init__(self, nombre, dni, fecha_nacimiento, sexo, telefono,tipo_sangre, centro_salud, fecha_hora_fallecimiento, fecha_hora_ablacion, organos):
        super().__init__(nombre, dni, fecha_nacimiento, sexo, telefono ,tipo_sangre, centro_salud)
        self.fecha_hora_fallecimiento = fecha_hora_fallecimiento
        self.fecha_hora_ablacion = fecha_hora_ablacion
        self.organos = organos

        for organo in organos:
            if organo.tipo.lower() not in self.organos_validos:
                raise ValueError(f"Este organo no es parte de la lista de organos validos:{organo.tipo}")

    def __str__(self):
        """
        Devuelve una representación de un donante, mostrando nombre, DNI
        tipo de sangre y los órganos a donar.
        """
        return f"Donante: {self.nombre}, DNI: {self.dni}, Sangre: {self.tipo_sangre}"