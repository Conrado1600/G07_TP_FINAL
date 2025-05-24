from abc import ABC, abstractmethod
from datetime import datetime 


class Persona (ABC):

    def __init__(self, nombre, dni, fecha_nacimiento, sexo, telefono, tipo_sangre, centro_salud):
        self.nombre = nombre
        self.dni = dni 
        self. fecha_nacimiento = fecha_nacimiento
        self.sexo = sexo
        self.telfeno = telefono



    @abstractmethod #se usa para indicar q es un metedo abstracto

    def __str__(self):
        return f"{self.nombre}({self.dni})"


class Donante (Persona):
    
    organos_validos = ["corazon", "higado", "pancreas", "huesos","rinion", "pulmones", "intestino", "piel", "corneas"]
    
    def __init__(self, nombre, dni, fecha_nacimiento, sexo, telefono, tipo_sangre, centro_salud, fecha_hora_fallecimiento, fecha_hora_ablacion, organos):
        super().__init__(nombre, dni, fecha_nacimiento, sexo, telefono)
        self.tipo_sangre = tipo_sangre
        self.centro_salud = centro_salud
        self.fecha_hora_fallecimiento = fecha_hora_fallecimiento
        self.fecha_hora_ablacion = fecha_hora_ablacion
        self.organos = organos

        for organo in organos:
            if organo.tipo.lower() not in self.organos_validos:
                raise ValueError(f"Este organo no es parte de la lista de organos validos:{organo.tipo}")


class Receptor(Persona):
    
    
    def __init__(self, nombre, dni, fecha_nacimiento, sexo, telefono, tipo_sangre, centro_salud, organo_necesario, fecha_ingreso, prioridad, patologia, estado="Estable"):
        super().__init__(nombre, dni, fecha_nacimiento, sexo, telefono)
        self.tipo_sangre = tipo_sangre
        self.centro_salud = centro_salud
        self.organo_necesario = organo_necesario
        self.fecha_ingreso = fecha_ingreso
        self.prioridad = prioridad
        self.patologia = patologia
        self.estado = estado



