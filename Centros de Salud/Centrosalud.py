from Cirujano import cirujano


class Centro_salud:


    def __init__(self, nombre, direccion, partido, provincia, telefono):
        self.nombre = nombre
        self.direccion = direccion 
        self.partido = partido
        self.provincia = provincia
        self.telefono = telefono 
        self.cirujanos = []
        self.vehiculos = []

    def agregar_cirujano (self, cirujano):
        self.cirujanos.append(cirujano)

    def agregar_vehiculo (self, vehiculo):
        self.vehiculos.append(vehiculo)

    def asignar_cirujano (self):
       
       for cirujano in  self.cirujanos
       


