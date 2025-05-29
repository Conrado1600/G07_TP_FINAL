from Cirujano.cirujano import Cirujano
from Vehiculo.vehiculo import vehiculo
from Persona.donante import Donante
from Persona.receptor import Receptor 


class Centro_salud():
    '''
    La clase Centro de salud se encarga de simular un hospital, es decir que gestiona los cirujanos
    disponibles en el centro para realizar el transplante. Ademas asigna el vehículo apropiado para realizar el trasplante 
    (Si el organo está en otra provincia se usa un avion, si se encuentra en la misma provincia pero diferente ciudad se usa helicoptero, y si
    se encuentran en la misma ciudad el receptor y el donante se usa el vehículo terrestre más rápido)

    '''

    def __init__(self, nombre, direccion, partido, provincia, telefono):
        self.nombre = nombre
        self.direccion = direccion 
        self.partido = partido
        self.provincia = provincia
        self.telefono = telefono 
        
        self.cirujanos : list[Cirujano] = []
        self.vehiculos : list[vehiculo] = []
        self.donantes : list[Donante] = []
        self.Receptor : list[Receptor] = []

    

    def agregar_cirujano (self, Cirujano):
        self.cirujanos.append(Cirujano)

    def agregar_vehiculo (self, vehiculo):
        self.vehiculos.append(vehiculo)

    def asignar_cirujano (self, organo):
        especialistas_disponibles : list [Cirujano]= []
        generales_disponibles : list [Cirujano] =[]
        for cirujano in self.cirujanos:
           if cirujano.disponible():
                tipo = cirujano.tipo_especialidad(organo.tipo)
                if tipo == "especialista":
                   especialistas_disponibles.append(cirujano)
                elif tipo == "general":
                   generales_disponibles.append(cirujano)
        if especialistas_disponibles: 
           return especialistas_disponibles[0]
        elif generales_disponibles:
            return generales_disponibles

    def asignar_vehiculo (self, provincia_destino, partido_destino):

        if self.provincia != provincia_destino:
            for vehic in self.vehiculos:  #creamos una variable "vehic" para no repetir palabra vehiculo.
                if vehic.tipo == "Avion":
                    return vehic
                 
        elif self.partido != partido_destino:
            for vehic in self.vehiculos:
                if vehic.tipo == "Helicoptero":
                    return vehic
        else: 
            Vehiculos_terrestres: list[vehiculo] = []
            for vehic in self.vehiculos: 
                if vehic.tipo == "Terrestre": 
                    Vehiculos_terrestres.append(vehic)
            if len(Vehiculos_terrestres) > 0:

                def obtener_velocidad (vehic):
                    return vehic.velocidad 
                
                Vehiculos_terrestres.sort(key = obtener_velocidad, reverse = True)
                #sort: ordena la lista de vehiculos terrestres teniendo en cuenta el key (atributo por el cual se ordena la lista)
                #reverse: ordena de mayor a menor

                return  Vehiculos_terrestres [0]#devuelve el primer vehiculo de la lista, es decir el mas veloz (por como esta ordenada)
            
            else: 
                raise Exception ("No hay vehiculos terrestre disponibles en este lugar")

    



