from datetime import datetime
import random


class Cirujano:
    def __init__(self, nombre, dni, fecha_nacimiento, sexo, telefono, especialidad=None):
        self.nombre = nombre
        self.dni = dni
        self.fecha_nacimiento = fecha_nacimiento
        self.sexo = sexo
        self.telefono = telefono
        self.especialidad = especialidad
        self.operaciones_realizadas_hoy = 0


    def disponible(self):
        return self.operaciones_realizadas_hoy == 0
    

    def realizar_operaciones(self,organo):
        self.operaciones_realizadas_hoy += 1
        resultado = random.randint(1, 10)
        if self.especialidad:
            especialidades = ["cardiovascular","corazon"]
            ["pulmonar","pulmones"]
            ["plastico","piel","corneas"]
            ["traumatologo","huesos"]
            ["gastroenterologo","intestino","riñon","higado","pancreas"]
            organos_validos=especialidades.get(self.especialidad,[])#esta parte busca dentro a ver si coicide la especialidad con el organo, sino se encuentre se devuelve una lista vacia []
             #si se devuelve una lista vacia la operacion falla
            if organo.tipo.lower() in organos_validos:
             return resultado >= 3
        return resultado > 5
        