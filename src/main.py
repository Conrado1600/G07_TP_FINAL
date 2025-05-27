from datetime import datetime
import re
from Organos.organo import Organo 
from Persona.donante import Donante
from Persona.receptor import Receptor
from INCUCAI.incucai import INCUCAI
from Centros_de_Salud.Centrosalud import Centro_salud
from Vehiculo.terrestre import Vehiculos_terrestre
from Vehiculo.helicoptero import Helicoptero
from Vehiculo.avion import Avion

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
    
    #creo receptores y donantes para probar el main
# Crear órganos para donantes
    organos1 = [Organo("corazón"), Organo("riñon")]
    organos2 = [Organo("hígado"), Organo("córneas")]
    organos3 = [Organo("pulmones"), Organo("piel")]
# Donantes
    d1 = Donante("Carlos Pérez", 12345678, datetime(10,5,1980), "M", "1111111111", "A+", centro1,
                 datetime(1,5,2025,14,30), datetime(1,5,2025,16,0), organos1)
    d2 = Donante("Laura Gómez", 23456789, datetime(22,8,1975), "F", "2222222222", "O-", centro2,
                 datetime(28,4,2025,9,15), datetime(28,4,2025,11,0), organos2)
    d3 = Donante("Miguel Rodríguez", 34567890, datetime(3,3,1990), "M", "3333333333", "B+", centro3,
                 datetime(10,5,2025,18,0), datetime(10,5,2025,19,30), organos3)
#receptores
    r1 = Receptor("Ana Torres", 45678901, datetime(15,1,2000), "F", "4444444444", "A+", centro1, "corazón",
                  datetime(20,5,2025), 1, "Cardiopatía congénita")
    r2 = Receptor("Julián Fernández", 56789012, datetime(30,9,1985), "M", "5555555555", "O-", centro2, "hígado",
                  datetime(10,4,2025), 2, "Hepatitis crónica")
    r3 = Receptor("Camila Soto", 67890123, datetime(5,12,1995), "F", "6666666666", "B+", centro3, "pulmones",
                  datetime(25,3,2025), 3, "Fibrosis quística")
    
    for d in [d1, d2, d3]:
        incucai.Registrar_Paciente(d)
    for r in [r1, r2, r3]:
        incucai.Registrar_Paciente(r)


def seleccionar_opcion(lista, mensaje= "Selecciones una opcion:"): #funcion enumerate para facilitar entrada de usuario
    while True:
        print(mensaje)
        for i, item in enumerate(lista, 1):
            print(f"{i}. {item}")
        print ("Escriba 'menu' para regresar al menu")
        ingreso = input ("Opción: ")  
        if ingreso.lower() == "menu":
            return None
        if ingreso.isdigit() and 1 <= int(ingreso) <= len(lista):
            return lista[int(ingreso) - 1 ]
        print("Opción inválida.")

def seleccionar_multiples_opciones(lista, mensaje = "Seleccione una opción (0 para finalizar):"):#funcion enumerate para opciones multiples
    seleccionados = []
    while True:
        print(mensaje)
        for i, item in enumerate(lista, 1):
            print(f"{i}. {item}")
        print("Escriba 'menu' para volver.")
        ingreso = input("Opción: ")
        if ingreso.lower() == "menu":
            return None
        if ingreso == "0":
            break
        if ingreso.isdigit() and 1 <=int (ingreso) <= len(lista): #isdigit para ver si solo son digitos 
            seleccionados.append(lista[int(ingreso)- 1])
        else: 
            print("Opción inválida.")
    return seleccionados

def ingresar_nombre():
    while True:
        nombre = input("Nombre: ")
        if nombre.lower() == "menu":
            return None
        if nombre.replace(" ","").isalpha():#reemplaza espacios por "" y con isalpha ve si son letras
            return nombre
        print("Ingreso inválido.")

def ingresar_dni():
    while True:
        dni = input("DNI: ")
        if dni.lower() == "menu":
            return None
        if dni.isdigit() and len(dni) <= 8: #isdigit ve si es dígito y el dni tiene q ser menor a 8 dígitos
            return int(dni)
        print("DNI inválido.")

def ingresar_fecha(mensaje = "Fecha (DD/MM/AAAA): "):
    while True:
        ingreso = input(mensaje)
        if ingreso.lower() == "menu":
            return None
        try:
            return datetime.strptime(ingreso, "%d/%m/%Y")
        except:
            print("Ingreso inválido")

def ingresar_fecha_hora(mensaje = "Fecha y hora (DD/MM/AAAA HH:MM): "):
    while True:
        ingreso = input(mensaje)
        if ingreso.lower == "menu":
            return None
        try:
            return datetime.strptime(ingreso, "%d/%m/%Y %H:%M")
        except: 
            print("Ingreso inválido.")

def ingresar_telefono():
    while True:
        telefono = input("Telefono: ")
        if telefono.lower() == "menu":
            return None
        if telefono.isdigit():
            return telefono
        print("Ingreso inválido.")

def ingresar_patologia():
    while True:
        patologia = input("Patología: ")
        if patologia.lower() =="menu":
            return None
        if patologia.replace("","").isalpha:
            return patologia
        print("Ingreso inválido.")

def registrar_paciente():

    tipo_persona = seleccionar_opcion(["Donante", "Receptor"], "Seleccione el tipo de paciente: ")
    if tipo_persona is None: 
        return

    nombre = ingresar_nombre()
    if nombre in None:
        return
    
    dni = ingresar_dni()
    if dni is None:
        return
    
    fecha_nacimiento = ingresar_fecha("Fecha de nacimiento(DD/MM/AAAA): ")
    if fecha_nacimiento is None:
        return

    sexo_op = seleccionar_opcion (sexo_opciones, "Seleccione sexo.")
    if sexo_op is None:
        return
    sexo = 'M' if sexo_op =="Masculino" else "F"

    telefono = ingresar_telefono()
    if telefono in None:
        return
    
    tipo_sangre = seleccionar_opcion(tipos_sangre, "Seleccione tipo de sangre: ")
    if tipo_sangre is None:
        return

    print("Centros disponibles:")
    for i, c in enumerate (incucai.centros_salud, 1):
        print(f"{i}. {c.nombre} ({c.partido}, {c.provincia})")
    index =  input("Seleccione centro (número) o 'menu'para salir: ")
    if index.lower()== "menu":
        return
    if not index.isdigit() or not (1<= int(index)<= len(incucai.centros_salud)):
        print ("Ingreso inválido.")
        return 
    centro = incucai.centros_salud[index]


    if tipo_persona == "Donante":
        fecha_fallecimiento = ingresar_fecha_hora("Fecha y hora de fallecimiento (DD-MM-AAAA HH:MM): "):
        if fecha_fallecimiento is None:
            return
        
        fecha_ablacion = ingresar_fecha_hora("Fecha y hora de ablacio (DD-MM-AAAA HH:MM): ")
        if fecha_ablacion is None:
            return
        
        organos_lista = seleccionar_multiples_opciones(organos_validos, "Seleccione los organos a donar (0 para finalizar): ")
        if organos_lista is None or len(organos_lista) == 0:
            return
        organos = [Organo(o) for o in organos_lista]

        donante = Donante(nombre, dni, fecha_nacimiento, sexo, telefono, tipo_sangre, centro, fecha_fallecimiento, fecha_ablacion, organos)
        incucai.Registrar_Paciente(donante)
        print("El donante fue registrado correctamente")
    else:
        organo_necesario = seleccionar_opcion(organos_validos, "Seleccione el organo que necesita: ")
        if organo_necesario is None:
            return
        
        fecha_ingreso = ingresar_fecha("Fecha de ingreso a la lista de receptores(DD-MM-AAAA): ")
        if fecha_ingreso is None:
            return
        
        prioridad_lista= seleccionar_opcion(prioridad_opciones, "Seleccioneel nivel de prioridad: ")
        if prioridad_lista is None:
            return
        prioridad = prioridad_opciones.index(prioridad_lista) + 1 #convierte la prioridad en numeros. 1 : Alta (la mas urgente, su estado es inestable), 2: Media y 3: Baja (menos urgente, su estado es estable)
        
        patologia = ingresar_patologia()
        if patologia is None:
            return
        
        receptor = Receptor(nombre, dni, fecha_nacimiento, sexo, telefono, tipo_sangre, centro, organo_necesario, fecha_ingreso, prioridad, patologia)
        incucai.Registrar_Paciente(receptor)
        print("El receptor fue registrado correctamente")

def mostrar_donantes():
    print("\Lista de donantes: ")
    for d in incucai.donantes:
        organos_donante = []
        for o in d.organos:
            organos_donante.append(o.tipo)
        print(f"{d.nombre} ({d.dni}) _ Organos a donar: {organos_donante}")

def mostrar_receptores():
    print("\Lista de receptores: ")
    for recep in incucai.receptores:
        print(f"{recep.nombre} ({recep.dni}) _ Organos necesarios: {recep.organo_necesario} _ Prioridad: {recep.prioridad} _Estado: {recep.estado}")

def buscar_receptores_por_centro():
    nombre = input("Ingrese el nombre del centro de salud en el que se encuentra o 'menu' para volver: ").lower()
    encontrados = []
    for recep in incucai.receptores:
        if nombre in recep.centro_salud.nombre.lower():
            encontrados.append(recep)
    if encontrados:
        for recep in encontrados:
            print(f"{recep.nombre} _ {recep.organo_necesario} _ Prioridad: {recep.prioridad}")
    else:
        print("No se encontraron receptores en ese centro")

def ver_prioridad_por_dni():
    try: 
        dni = int(input("Ingrese DNI del receptor: "))
        for recep in incucai.receptores:
            if recep.dni == dni:
                print(f"Prioridad: {recep.prioridad}, Estado: {recep.estado}")
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
        
