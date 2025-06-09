from datetime import datetime, timedelta #timedelta se usa para demostrar la diferencia entre dos fechas/horas 
import random #te da un nro aleatorio
from Centros_de_Salud.Centrosalud import Centro_salud
from Cirujano.cirujano import Cirujano
from Persona.donante import Donante
from Persona.receptor import Receptor


class INCUCAI:
    """
    Esta clase representa el sistema de coordinacion de transplantes. Se encarga de administrar los donantes, receptores y centros de salud.
    Ademas busca compatibilidades y se encarga de ejecutar el proceso de los transplantes.
    
    """

    def __init__(self):
        
        self.donantes: list[Donante] = []
        self.receptores: list[Receptor] = []
        self.centros_salud: list[Centro_salud] = []

    def Registrar_Paciente (self, persona):
        """
        Se encarga de registrar al paciente ya sea donante o receptor.
        params: objeto de tipo donante o receptor
        
        """
        if any(paciente.dni == persona.dni for paciente in self.receptores + self.donantes): #creamos variable paciente
            raise Exception("El paciente ya esta registrado.")
        if isinstance(persona, Donante):
            self.donantes.append(persona)
        elif isinstance(persona, Receptor):
            self.receptores.append(persona)

    def buscar_receptor_para_donante(self, donante):
        
        """
        Se busca un receptor compatible para cada organo del donante.
        params:un objeto de tipo donante con al menos un organo para donar.
        retorna (donante, receptor, organo) en el caso de que se encuentre una compatibilidad.

        """
        compatibilidades = []
        
        for organo in donante.organos:
            posibles_receptores = [
                recep for recep in self.receptores
                if recep.tipo_sangre == donante.tipo_sangre and recep.organo_necesario.lower() == organo.tipo.lower()
            ] #buscamos si hay al menos un receptor con mismo tipo de sangre y organo a transplantar
            if posibles_receptores:
                posibles_receptores.sort(key=lambda recep: (recep.prioridad, recep.fecha_ingreso, recep.dni)) #se ordena por prioridad/estado, si dos o mas receptores tienen la misma prioridad, se analiza por fecha de ingreso a la lista de receptores, si tambien hay coincidencias en l fecha de ingreso se analiza por edad y el de menor edad sube en la lista. quien tenga todo para ser el primero en la lista queda en la posicion 0 de la lista de posibles receptores y ahi sesabe quien sera el receptor que recibe el organo.
                receptor  = posibles_receptores[0]
                compatibilidades.append((donante, receptor, organo))
        return compatibilidades
    
    def realizar_transplante(self, donante, receptor, organo):
        
        """
        Ejecuta el proceso del transplante cuando se encuentra un donante y receptor compatibles.
        params: el paciente donante, el paciente receptor y el organo a transplantar.
        retorna nada pero actualiza el estado del receptor, y modifica las listas en relacion al resultado.

        """

        centro_donante = donante.centro_salud
        centro_receptor = receptor.centro_salud

        fecha_ablacion = datetime.now()
        organo.set_fecha_ablacion(fecha_ablacion)
        donante.organos.remove(organo)

        vehiculo = centro_donante.asignar_vehiculo(provincia_destino=centro_receptor.provincia, partido_destino=centro_receptor.partido)
        #invento distancias segun el tipo de vehiculo asi tengo en cuenta todos los casos pero con valores inventados de distancia y nivel de trafico

        if vehiculo.tipo == "Avion":
            distancia = random.randint(500, 3000)
            nivel_trafico = 0
        elif vehiculo.tipo == "Helicoptero":
            distancia = random.randint(100, 500)
            nivel_trafico = 0
        else:
            distancia = random.randint(5,100)
            nivel_trafico = random.uniform(0.5, 2.5)#uniform es como un randint pero con float
        
        #calc tiempo de viaje y hora de llegada aprox
        tiempo_viaje = vehiculo.calcular_tiempo_viaje(distancia, nivel_trafico)
        llegada = fecha_ablacion + timedelta(hours=tiempo_viaje)

        cirujano_apto = centro_receptor.asignar_cirujano(organo) #asigno cirujano
        if cirujano_apto is None:
            cirujano_apto = centro_donante.asignar_cirujano(organo)
        if cirujano_apto is None:
            print("No se encontro un cirujano disponible en ningun centro")
            receptor.estado = "Inestable"
            receptor.prioridad = 1
            return False
        
        if llegada - fecha_ablacion > timedelta(hours=20):
            receptor.estado = "Inestable"
            receptor.prioridad = 1
        else:
            exito = cirujano_apto.realizar_operaciones(organo)
            if exito:
                self.receptores.remove(receptor)
            else:
                receptor.estado = "Inestable"
                receptor.prioridad = 1




