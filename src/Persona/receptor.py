from Persona.persona import Persona

class Receptor(Persona):
    
    
    def __init__(self, nombre, dni, fecha_nacimiento, sexo, telefono, tipo_sangre, centro_salud, organo_necesario, fecha_ingreso, prioridad, patologia, estado="Estable"):
        super().__init__(nombre, dni, fecha_nacimiento, sexo, telefono, tipo_sangre, centro_salud)
        self.tipo_sangre = tipo_sangre
        self.centro_salud = centro_salud
        self.organo_necesario = organo_necesario
        self.fecha_ingreso = fecha_ingreso
        self.prioridad = prioridad
        self.patologia = patologia
        self.estado = estado

    def __str__(self):
        return f"Receptor: {self.nombre}, DNI: {self.dni}, Sangre: {self.tipo_sangre}, Órgano: {self.organo_necesario}"