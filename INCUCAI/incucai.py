from datetime import datetime, timedelta #timedelta se usa para demostrar la diferencia entre dos fechas/horas 
import random #te da un nro aleatorio
from Persona.persona import Donante, Receptor
from Centros_de_Salud.Centrosalud import Centro_salud
from Organo.organo import Organo 


class INCUCAI():

    def __init__(self):
        self.donantes: list[Donante] = []
        self.receptores: list[Receptor] = []
        self.centros_salud: list[Centro_salud] = []

    def Registrar_Paciente ()
