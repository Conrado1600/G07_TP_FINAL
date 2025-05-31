from abc import ABC, abstractmethod
from datetime import datetime 


class Persona (ABC):
    """
    Esta clase representa a una persona dentro del sistema de donaciones y transplantes.
    contiene la información y datos de las personas

    """

    def __init__(self, nombre, dni, fecha_nacimiento, sexo, telefono, tipo_sangre, centro_salud):
        self.nombre = nombre
        self.dni = dni 
        self. fecha_nacimiento = fecha_nacimiento
        self.sexo = sexo
        self.telfeno = telefono
        self.tipo_sangre = tipo_sangre
        self.centro_salud = centro_salud



    @abstractmethod #se usa para indicar q es un metedo abstracto

    def __str__(self):
        """
        Método abstracto que debe ser imlementado por las subclases
        """
        pass


