from Persona.persona import Persona

class Receptor(Persona):
    """
    Esta clase representa a un receptor (hijo) de órganos, heredando los atributos 
    de la clase padre Persona y ademas sumando información sobre necesidad médica 
    (como es el caso de la patología o su estado).
    """
    
    
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
        """
        devuelve la representación de un receptor, incluyendo nombre, DNI,
        tipo de sangre y el órgano que necesita
        """
        return f"Receptor: {self.nombre}, DNI: {self.dni}, Sangre: {self.tipo_sangre}, Órgano: {self.organo_necesario}"