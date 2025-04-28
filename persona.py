from abc import ABC, abstractmethod


class Persona (ABC):

    def __init__(self, nombre, dni, fecha_nacimiento, sexo, telefono ):
        self.nombre = nombre
        self.dni = dni 
        self. fecha_nacimiento = fecha_nacimiento
        self.sexo = sexo
        self.telfeno = telefono 


    @abstractmethod

    def __str__(self):
        pass


#class Donante (Persona):
 #   def __init__(self, nombre, dni, fecha_nacimiento, sexo, telefono, tipo_sangre, centro_salud):
    