from datetime import datetime
from src.Organos.organo import Organo 
from src.persona import Donante, Receptor
from src.INCUCAI.incucai import INCUCAI
from src.Centros_de_Salud.Centrosalud import Centro_salud
from src.Vehiculo.vehiculo import Vehiculos_terrestre, Helicoptero, Avion

incucai = INCUCAI()

organos_validos = ["corazón", "hígado", "pancreas", "hueso", "riñon", "pulmones", "intestino", "piel", "córneas"]
tipos_sangre = ["A+", "A-","B+", "B-","AB+", "AB-","O+", "O-"]#preguntar sobre rh nulo
prioridad_opciones = ["Alta", "Media", "Baja"]
sexo_opciones = ["Masculino", "Femenino"]

def inicializar_centros():
    centro1 = Centro_salud("Hospital Zonal Pergamino", "Liniers 979", "Pergamino", "Buenos Aires", "02477 - 429792")
    centro2 = Centro_salud("Hospital Blas L. Dubarry", "Calle 12 nro 825", "Mercedes", "Buenos Aires", "02324 - 425555")
    centro3 = Centro_salud("Hospital Garrahan", "Brasil 2150", "CABA","Buenos Aires", "0114122-6000")

    for centro in [centro1, centro2, centro3]:
        centro.agregar_vehiculo(Vehiculos_terrestre(100))
        centro.agregar_vehiculo(Helicoptero(250))
        centro.agregar_vehiculo(Avion(600))
        incucai.centros_salud.append(centro)


def seleccionar_opcion(lista, mensaje= "Selecciones una opcion:"): #funcion enumerate para facilitar entrada de usuario
    while True:
        print(mensaje)
        for i, item in enumerate(lista, 1):
            print(f"{i}. {item}")
        try:
            opcion = int(input("Opcion: "))
            if 1 <= opcion <= len(lista):
                return lista[opcion - 1]
            else:
                print ("Opcion inválida.")
        except ValueError:
            print("Entrada inválida. Ingrese un número.")

def seleccionar_multiples_opciones(lista, mensaje = "Seleccione una opción (0 para finalizar):"):#funcion enumerate para opciones multiples
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
                print("Opción inválida.")
        except ValueError:
            print("Respuesta incorrecta.")
    return seleccionados


def registrar_paciente():

    tipo_persona = seleccionar_opcion(["Donante", "Receptor"], "Seleccione el tipo de paciente: ")
    tipo = "D" if tipo_persona == "Donante" else "R"
    try:
        nombre = input("Nombre: ")
        dni = int(input("DNI: ")) #es un nro entero
        fecha_nacimiento = datetime.strptime(input("Fecha de nacimiento (DD-MM-AAAA): "), "%d-%m-%A")
        sexo_lista = seleccionar_opcion (sexo_opciones, "Seleccione sexo.")
        if sexo_lista == "Masculino" :
            sexo = "M"
        else:
            sexo= "F"
        telefono = input("Teléfono: ")
        tipo_sangre = seleccionar_opcion(tipos_sangre, "Seleccione tipo de sangre: ")

        print("Centros disponibles:")
        for i, c in enumerate (incucai.centros_salud):
            print(f"{i + 1}. {c.nombre} ({c.partido}, {c.provincia})")
        index =  int(input("Seleccione centro (número): "))-1
        if not 0 <= index < len(incucai.centros_salud):
            print ("El centro de salud ingresado es incorrecto")
            return 
        centro = incucai.centros_salud[index]


        if tipo == "D":
            fecha_fallecimiento = datetime.strptime(input("Fecha y hora de fallecimiento (DD-MM-AAAA HH:MM): "), "%d-%m-%A %H:%M")
            fecha_ablacion = datetime.strptime(input ("Fecha y hora de ablacio (DD-MM-AAAA HH:MM): "), "%d-%m-%A %H:%M")
            organos_lista = seleccionar_multiples_opciones(organos_validos, "Seleccione los organos a donar (0 para finalizar): ")
            if not organos_lista:
                print("No son validos los organos ingresados")
                return
            organos = [Organo(o) for o in organos_lista]
            donante = Donante(nombre, dni, fecha_nacimiento, sexo, telefono, tipo_sangre, centro, fecha_fallecimiento, fecha_ablacion, organos)
            incucai.registrar_paciente(donante)
            print("El donante fue registrado correctamente")
        else:
            organo_necesario = seleccionar_opcion(organos_validos, "Seleccione el organo que necesita: ")
            fecha_ingreso = datetime.strptime(input("Fecha de ingreso a la lista de receptores(DD-MM-AAAA): "), "%d-%m-%A" )
            prioridad_lista= seleccionar_opcion(prioridad_opciones, "Seleccioneel nivel de prioridad: ")
            prioridad = prioridad_opciones.index(prioridad_lista) + 1
            patologia = input("Patología: ")
            receptor = Receptor(nombre, dni, fecha_nacimiento, sexo, telefono, tipo_sangre, centro, organo_necesario, fecha_ingreso, prioridad, patologia)
            incucai.Registrar_Paciente(receptor)
            print("El receptor fue registrado correctamente")
    except Exception as e:
        print ("Huboun error al registrar al paciente")

def mostrar_donantes():
    print("\Lista de donantes: ")
    for d in incucai.donantes:
        organos_donante = []
        for o in d.organos:
            organos_donante.append(o.tipo)
        print(f"{d.nombre} ({d.dni}) _ Organos a donar: {organos_donante}")

def mostrar_receptores():
    print("\Lista de receptores: ")
    for r in incucai.receptores:
        print(f"{r.nombre} ({r.dni}) _ Organos necesarios: {r.organo_necesario} _ Prioridad: {r.prioridad} _Estado: {r.estado}")

def buscar_receptores_por_centro():
    nombre = input("Ingrese el nombre del centro de salud en el que se encuentra: ").lower()
    encontrados = []
    for r in incucai.receptores:
        if nombre in r.contro_salud.nombre.lower():
            encontrados.append(r)
    if encontrados:
        for r in encontrados:
            print(f"{r.nombre} _ {r.organo_necesario} _ Prioridad: {r.prioridad}")
    else:
        print("No se encontraron receptores en ese centro")

def ver_prioridad_por_dni():
    try: 
        dni = int(input("Ingrese DNI del receptor: "))
        for r in incucai.receptores:
            if r.dni == dni:
                print(f"Prioridad: {r.prioridad}, Estado: {r.estado}")
                return
        print ("Receptor no encontrado.")
    except ValueError: 
        print("DNI inválido.")


def menu ():
    while True: 
        print("\\n ---- 🫀  Sistema de Donanción y Transplante  🫀  ----")
        print("1️⃣. Registrar nuevo paciente")
        print("2️⃣. Ver lista de donantes")
        print("3️⃣. Ver lista de receptores")
        print("4️⃣. Buscar receptores por centro de salud")
        print("5️⃣. Ver prioridad de un receptor por DNI")
        print("6️⃣. Salir")
        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            registrar_paciente()
        elif opcion == "2":
            mostrar_donantes()
        elif opcion == "3":
            mostrar_receptores()
        elif opcion == "4":
            buscar_receptores_por_centro()
        elif opcion == "5":
            ver_prioridad_por_dni()
        elif opcion == "6":
            print("Saliendo del sistema.")
            break
        else: 
            print("Opcion inválida.")

if __name__ == "__main__":
    menu()
        
