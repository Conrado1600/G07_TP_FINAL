from datetime import datetime
from Organo.organo import Organo 
from Persona.persona import Donante, Receptor
from INCUCAI.incucai import INCUCAI
from Centros_de_Salud.Centrosalud import Centro_salud
from Vehiculo.vehiculo import Vehiculos_terrestre, Helicoptero, Avion

incucai = INCUCAI()

centro1 = Centro_salud("Hospital Pergamino", "Liniers 979", "Pergamino", "Buenos Aires", "02477 – 429792")
centro2 = Centro_salud("Hospital Blas L. Dubarry", "Calle 12 nro 825", "Mercedes", "Buenos Aires", "02324 - 425555")

centro1.agregar_vehiculo(Vehiculos_terrestre(100))
centro1.agregar_vehiculo(Helicoptero(250))
centro1.agregar_cirujano(Avion(600))

centro2.agregar_vehiculo(Vehiculos_terrestre(90))
centro2.agregar_vehiculo(Helicoptero(230))
centro2.agregar_vehiculo(Avion(580))

incucai.centros_salud.append(centro1)
incucai.centros_salud.append(centro2)

ORGANOS_VALIDOS = ["corazón", "hígado", "pancreas", "hueso", "riñon", "pulmones", "intestino", "piel", "córneas"]
TIPOS_SANGRE = ["A+", "A-","B+", "B-","AB+", "AB-","O+", "O-"]#preguntar sobre rh nulo
#PRIORIDAD = ["Alta", "Media", "Baja"]

def seleccionar_opcion(lista, mensaje= "Selecciones una opcion:"): #funcion enumerate para facilitar entrada de usuario
    while True:
        print(mensaje)
        for i, item in enumerate(lista, 1):
            print(f"{i}. {item}")
        try:
            opcion = int(input("Opcion: 1"))
            if 1 <= opcion <= len(lista):
                return lista[opcion - 1]
            else:
                print ("Opcion fuera de rango")
        except ValueError:
            print("Entrada inválida. Ingrese un número.")

def seleccionar_multiples_opciones(lista, mensaje = "Seleccione elementos (0 para terminar):"):
    seleccionados = []
    while True:
        print(mensaje)
        for i, item in enumerate(lista, 1):
            print(f"{i}. {item}")
        try:
            opcion = int (input("Opción: "))
            if opcion == 0:
                break
            if 1 <= opcion <= len(lista):
                seleccionados.append(lista[opcion - 1])
            else: 
                print("Opción fuera de rango.")
        except ValueError:
            print("Entrada incorrecta.")
    return seleccionados

def manu ():
    while True: 
        print("\\n ----🦾🫀Sistema de Donanción y Transplante🫀🦾----")
        print("1️⃣. Registrar nuevo paciente")
        print("2️⃣. Ver lista de donantes")
        print("3️⃣. Ver lista de receptores")
        print("4️⃣. Buscar receptores por centro de salud")
        print("5️⃣. Ver prioridad de un receptor por DNI")
        print("6️⃣. Salir")
        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            registrar_paciente()
        
def registrar_paciente():

    tipo = input("¿Es Donante (D) o Receptor (R)?").upper()
    if tipo not in ["D", "R"]:
        print("Opcion incorrecta.")
        return
    try:
        nombre = input("Nombre: ")
        dni = int(input("DNI: ")) #es un nro entero
        fecha_nacimiento = datetime.strptime(input("Fecha de nacimiento (DD-MM-AAAA): "), "%d-%m-%A" )
        sexo = input("Sexo: (M/F):").upper()
        telefono = input("Teléfono: ")
        tipo_sangre = seleccionar_opcion(TIPOS_SANGRE, "Seleccione tipo de sangre: ")

    print("Centros disponibles:")
    for i, c in enumerate (incucai.centros_salud):
        print(f"{i + 1}. {c.nombre} ({c.partido}, {c.provincia})")
    centro = incucai.centros_salud[int(input("Seleccione centro (numero): ")) - 1]


    if tipo == "D":
        fecha_fallecimiento = datetime.strptime(input("Fecha y hora de fallecimiento (DD-MM-AAAA HH:MM)"), "%d-%m-%A %H:%M")
        fecha_ablacion = datetime.strptime (input ("Fecha y hora de fallecimiento "))




            
            
