from datetime import datetime, timedelta #timedelta se usa para demostrar la diferencia entre dos fechas/horas 
import random #te da un nro aleatorio
from Persona.persona import Donante, Receptor
from Centros_de_Salud.Centrosalud import Centro_salud
from Organo.organo import Organo



class INCUCAI:


    def __init__(self):
        self.donantes: list[Donante] = []
        self.receptores: list[Receptor] = []
        self.centros_salud: list[Centro_salud] = []

    def Registrar_Paciente (self, persona):
        if any(paciente.dni == persona.dni for paciente in self.receptores + self.donantes): #creamos variable paciente
            raise Exception("El paciente ya esta registrado.")
        if isinstance(persona, Donante):
            self.donantes.append(persona)
            self.buscar_donante_para_receptor(persona)
        elif isinstance(persona, Receptor):
            self.receptores.append(persona)
            self.buscar_donante_para_receptor(persona)

    def buscar_receptor_para_donante(self, donante):
        for organo in donante.organos:
            posibles_receptores = [
                recep for recep in self.receptores
                if recep.tipo_sangre == donante.tipo_sangre and recep.organo_necesario.lower() == organo.tipo.lower()
            ] #buscamos si hay al menos un receptor con mismo tipo de sangre y organo a transplantar
            if posibles_receptores:
                posibles_receptores.sort(key=lambda recep: (recep.prioridad, recep.fecha_ingreso))
                receptor = posibles_receptores[0]
                self.realizar_transplante(donante, receptor, organo)
            #ordenamos la lista de posibles receptores en funcion de lambda para que se ordene primero por la prioridad y en caso de que sea igual, se ordenaria por fecha de ingreso
    
    def buscar_donante_para_receptor(self, receptor):
        for donante in self.donantes:
            for organo in donante.organos:
                if organo.tipo.lower() == receptor.organo_necesario.lower() and donante.tipo_sangre == receptor.tipo_sangre:
                    self.realizar_transplante(donante, receptor, organo)
                    return
    
    def realizar_transplante(self, donante, receptor, organo):
        centro_donante = donante.centro_salud
        centro_receptor = receptor.centro_salud

        fecha_ablacion = datetime.now()
        organo.set_fecha_ablacion(fecha_ablacion)
        donante.organos.remove(organo)

        vehiculo = centro_donante.asignar_vehiculo(provincia_destino=centro_receptor, partido_destino=centro_receptor)
        #invento distancias segun el tipo de vehiculo asi tengo en cuenta todos los casos pero con valores inventados de distancia y nivel de trafico

        if vehiculo.tipo == "Avion":
            distancia = random.randint(500, 3000)
            nivel_trafico = 0
        elif vehiculo.tipo == "Helicoptero":
            distancia = random.randint(100, 500)
            nivel_trafico = 0
        else:
            distancia = random.randint(5,100)
            nivel_trafico = random.randint(0.5, 2.5)
        
        #calc tiempo de viaje y hora de llegada aprox
        tiempo_viaje = vehiculo.calcular_tiempo_viaje(distancia, nivel_trafico)
        llegada = fecha_ablacion + timedelta(hours=tiempo_viaje)

        cirujano = centro_receptor.asignar_cirujano(organo) #asigno cirujano

        if llegada - fecha_ablacion > timedelta(hours=20):
            receptor.estado = "Inestable"
            receptor.prioridad = 1
        else:
            exito = cirujano.realizar_operacion(organo)
            if exito:
                self.receptores.remove(receptor)
            else:
                receptor.estado = "Inestable"
                receptor.prioridad = 1




