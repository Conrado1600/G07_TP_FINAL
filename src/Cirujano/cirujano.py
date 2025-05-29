import random


class Cirujano:
    def __init__(self, nombre, dni, fecha_nacimiento, sexo, telefono, especialidad):
        self.nombre = nombre
        self.dni = dni
        self.fecha_nacimiento = fecha_nacimiento
        self.sexo = sexo
        self.telefono = telefono
        self.especialidad = especialidad.lower()
        self.operaciones_realizadas_hoy = 0


    def disponible(self):
        return self.operaciones_realizadas_hoy == 0 
    
    def tipo_especialidad(self, organo):
        organo = organo.lower()
        especialidades = {
            "cardiovascular": ["corazon"],
            "pulmonar": ["pulmones"],
            "plastico": ["piel","corneas"],
            "traumatologo": ["huesos"],
            "gastroenterologo": ["intestino","riñon","higado","pancreas"]
        }
        if self.especialidad == "general":
            return "general"
        if organo in especialidades.get(self. especialidad, []):
            return "especialista"
        return "otro" #como ultimo recurso si no hay especialista ni general opera un especialista que este disponible

    def realizar_operaciones(self,organo, especialidades):
        self.operaciones_realizadas_hoy += 1
        resultado = random.randint(1, 10)
        tipo = self.tipo_especialidad(organo.tipo)
        if tipo == "especialista":
             return resultado >= 3
        else:
            return resultado > 5
        
    def __str__(self):
        return f"{self.nombre} (DNI: {self.dni}) _ Epecialidad: {self.especialidad}"
        