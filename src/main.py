from datetime import datetime
from Organos.organo import Organo 
from Persona.donante import Donante
from Persona.receptor import Receptor
from INCUCAI.incucai import INCUCAI
from Centros_de_Salud.Centrosalud import Centro_salud
from Vehiculo.terrestre import Vehiculos_terrestre
from Vehiculo.helicoptero import Helicoptero
from Vehiculo.avion import Avion
from Cirujano.cirujano import Cirujano 

incucai = INCUCAI()


organos_validos = ["corazon", "higado", "pancreas", "hueso", "riñon", "pulmones", "intestino", "piel", "corneas"]
tipos_sangre = ["A+", "A-","B+", "B-","AB+", "AB-","O+", "O-"]#preguntar sobre rh nulo
prioridad_opciones = ["Alta", "Media", "Baja"]
sexo_opciones = ["Masculino", "Femenino"]

def inicializar_centros():
    centro1 = Centro_salud("Hospital Zonal Pergamino", "Liniers 979", "Pergamino", "Buenos Aires", "02477 - 429792")
    centro2 = Centro_salud("Hospital Blas L. Dubarry", "Calle 12 nro 825", "Mercedes", "Buenos Aires", "02324 - 425555")
    centro3 = Centro_salud("Hospital Garrahan", "Brasil 2150", "CABA","Buenos Aires", "0114122-6000")
    centro4 = Centro_salud("Hospital Italiano", "Gascon 450", "CABA", "Buenos Aires", "01149590200")
    centro5 = Centro_salud("Hospital San Martín", "Av. 1 y 70", "La Plata", "Buenos Aires", "02214255500")
    centro6 = Centro_salud("Hospital El Cruce", "Camino Gral Belgrano 5400", "Florencio Varela", "Buenos Aires", "01142105200")

    # Cirujanos para el centro 1
    cirujano_p1 = Cirujano("Dr. Martín Sosa", 30111222, datetime(1978, 3, 15), "Masculino", "1123456789", "cardiovascular")
    cirujano_p2 = Cirujano("Dra. Victoria Rivas", 32333444, datetime(1985, 7, 20), "Femenino", "1134567890", "general")
    cirujano_p3 = Cirujano("Dr. Lucas Díaz", 28999888, datetime(1970, 11, 5), "Masculino", "1145678901", "gastroenterologo")

    # Cirujanos para el centro 2
    cirujano_m1 = Cirujano("Dra. Elena García", 35555666, datetime(1982, 4, 10), "Femenino", "1156789012", "neurocirugia")
    cirujano_m2 = Cirujano("Dr. Andrés Ferrari", 31777888, datetime(1979, 9, 25), "Masculino", "1167890123", "general")

    # Cirujanos para el centro 3
    cirujano_g1 = Cirujano("Dr. Juan Pérez", 25123456, datetime(1965, 1, 1), "Masculino", "1178901234", "pediatra") # Nota: no hay especialidad "pediatra" en tipo_especialidad
    cirujano_g2 = Cirujano("Dra. Sofía Medina", 38987654, datetime(1992, 6, 30), "Femenino", "1189012345", "general")
    cirujano_g3 = Cirujano("Dr. Pablo Castro", 29000111, datetime(1973, 2, 8), "Masculino", "1190123456", "traumatologo")

    # Cirujanos para el centro 4 
    cirujano_i1 = Cirujano("Dr. Fernando Núñez", 27000333, datetime(1968, 10, 12), "Masculino", "1110203040", "gastroenterologo")
    cirujano_i2 = Cirujano("Dra. Carolina Paz", 34567890, datetime(1987, 5, 5), "Femenino", "1120304050", "general")

    # Cirujanos para el centro 5 
    cirujano_s1 = Cirujano("Dr. Javier Torres", 26112233, datetime(1971, 7, 1), "Masculino", "1130405060", "pulmonar")
    cirujano_s2 = Cirujano("Dra. Romina Vidal", 36778899, datetime(1989, 2, 28), "Femenino", "1140506070", "general")

    # Cirujanos para el centro 6 
    cirujano_e1 = Cirujano("Dr. Gustavo Peralta", 24998877, datetime(1960, 12, 1), "Masculino", "1150607080", "cardiovascular")
    cirujano_e2 = Cirujano("Dra. Florencia Luna", 33445566, datetime(1981, 8, 18), "Femenino", "1160708090", "general")

    for centro in [centro1, centro2, centro3, centro4, centro5, centro6]:
        centro.agregar_vehiculo(Vehiculos_terrestre(100))
        centro.agregar_vehiculo(Helicoptero(250))
        centro.agregar_vehiculo(Avion(600))
        incucai.centros_salud.append(centro)
    
    centro1.agregar_cirujano(cirujano_p1)
    centro1.agregar_cirujano(cirujano_p2)
    centro1.agregar_cirujano(cirujano_p3)

    centro2.agregar_cirujano(cirujano_m1)
    centro2.agregar_cirujano(cirujano_m2)

    centro3.agregar_cirujano(cirujano_g1)
    centro3.agregar_cirujano(cirujano_g2)
    centro3.agregar_cirujano(cirujano_g3)

    centro4.agregar_cirujano(cirujano_i1)
    centro4.agregar_cirujano(cirujano_i2)

    centro5.agregar_cirujano(cirujano_s1)
    centro5.agregar_cirujano(cirujano_s2)

    centro6.agregar_cirujano(cirujano_e1)
    centro6.agregar_cirujano(cirujano_e2)

#Crear órganos para donantes
    organos1 = [Organo("corazon")]
    organos2 = [Organo("higado"), Organo("corneas")]
    organos3 = [Organo("pulmones"), Organo("piel")]
    
#Donantes
    d1 = Donante("Carlos Pérez", 12345678, datetime(1980,5,10), "M", "1111111111", "A+", centro1,
                 datetime(2025,5,1,14,30), datetime(2025,5,1,16,0), organos1)
    centro1.donantes.append(d1)
    d2 = Donante("Laura Gómez", 23456789, datetime(1975,8,22), "F", "2222222222", "O-", centro2,
                 datetime(2025,4,28,9,15), datetime(2025,4,28,11,0), organos2)
    centro2.donantes.append(d2)
    d3 = Donante("Miguel Rodríguez", 34567890, datetime(1990,3,3), "M", "3333333333", "B+", centro3,
                 datetime(2025,5,10,18,0), datetime(2025,5,10,19,30), organos3)
    centro3.donantes.append(d3)
#Receptores
    r1 = Receptor("Ana Torres", 45678901, datetime(2000,1,15), "F", "4444444444", "A+", centro1, "corazón",
                  datetime(2025,5,20), 1, "Cardiopatía congénita")
    centro1.Receptor.append(r1)
    r2 = Receptor("Julián Fernández", 56789012, datetime(1985,9,30), "M", "5555555555", "O-", centro2, "hígado",
                  datetime(2025,4,10), 2, "Hepatitis crónica")
    centro2.Receptor.append(r2)
    r3 = Receptor("Camila Soto", 67890123, datetime(1995,12,5), "F", "6666666666", "B+", centro3, "pulmones",
                  datetime(2025,3,25), 3, "Fibrosis quística")
    centro3.Receptor.append(r3)
    
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
    if nombre is None:
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
    sexo = 'M' if sexo_op.__eq__("Masculino") else "F"

    telefono = ingresar_telefono()
    if telefono is None:
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
    centro = incucai.centros_salud[int (index)-1]# porque el enumerate empieza desde 1


    if tipo_persona == "Donante":
        fecha_fallecimiento = ingresar_fecha_hora("Fecha y hora de fallecimiento (DD/MM/AAAA HH:MM): ")
        if fecha_fallecimiento is None:
            return
        
        fecha_ablacion = ingresar_fecha_hora("Fecha y hora de ablación (DD/MM/AAAA HH:MM): ")
        if fecha_ablacion is None:
            return
        
        organos_lista = seleccionar_multiples_opciones(organos_validos, "Seleccione los organos a donar (0 para finalizar): ")
        if organos_lista is None or len(organos_lista) == 0:
            return
        organos = [Organo(o) for o in organos_lista]

        donante = Donante(nombre, dni, fecha_nacimiento, sexo, telefono, tipo_sangre, centro, fecha_fallecimiento, fecha_ablacion, organos)
        incucai.Registrar_Paciente(donante)
        centro.donantes.append(donante)
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
   #limpiar_pantalla()
    print("Lista de donantes: ")
    for d in incucai.donantes:
        organos_donante = []
        for o in d.organos:
            organos_donante.append(o.tipo)
        print(f"{d.nombre} ({d.dni}) _ Organos a donar: {organos_donante}")

def mostrar_receptores():
   #limpiar_pantalla()
    print("Lista de receptores: ")
    for recep in incucai.receptores:
        print(f"{recep.nombre} ({recep.dni}) _ Organos necesarios: {recep.organo_necesario} _ Prioridad: {recep.prioridad} _Estado: {recep.estado}")

def buscar_receptores_por_centro():
   #limpiar_pantalla()
    nombre = input("Ingrese el nombre del centro de salud en el que se encuentra o 'menu' para volver: ").strip().lower()
    if nombre == "menu":
        return
    encontrados = []
    for recep in incucai.receptores:
        if nombre in recep.centro_salud.nombre.lower():
            encontrados.append(recep)
    if encontrados:
        print("Receptores encontrados:")
        for recep in encontrados:
            print(f"{recep.nombre} ({recep.dni}) _ {recep.organo_necesario} _ Prioridad: {recep.prioridad}")
    else:
        print("No se encontraron receptores en ese centro")

def ver_prioridad_paciente():
    while True:
        dni = input("Ingrese DNI del receptor o 'menu' para volver:")
        if dni.lower() == "menu":
            return
        if dni.isdigit() and 1 <= len(dni) <= 8:
            dni = int(dni)
            break
        else: 
            print("DNI inválido.")
    for recep in incucai.receptores:
        if recep.dni == dni:
            print(f"Prioridad: {recep.prioridad} _ Estado: {recep.estado} ")
            return
    print("Receptor no encontrado.")
    
def volver_al_menu():
    while True:
        respuesta = input("\n¿Desea volver al menú? (s/n): ").lower()
        if respuesta == "n":
            print("¡Gracias por usar el sistema de gestión de donación de órganos!")
            return False
        elif respuesta == "s":
            return True
        else:
            print("Ingreso inválido. Por vafor 's' para volver al menú o 'n' para salir.")

def mostrar_titulo():
    print("=" * 100)
    print("     🩺 BIENVENIDO AL SISTEMA DE GESTIÓN DE DONACIÓN DE ÓRGANOS  🩺 ")
    print("=" * 100)

def mostrar_centros():
    
    print("Lista de centros de salud:")
    for c in incucai.centros_salud: 
        organos_centro = []
        for d in c.donantes:
            for o in d.organos:
                organos_centro.append(o.tipo)
        
        if organos_centro:
            print(f"{c.nombre} ({c.direccion}) - Órganos disponibles: {organos_centro}")
        else:
            print(f"{c.nombre} ({c.direccion}) - No hay órganos disponibles en este centro")

def mostrar_vehiculos():

    print("Lista de vehículos: ")
    for c in incucai.centros_salud:
        for v in c.vehiculos:
            print(f"{v.tipo} - Centro: {c.nombre}")

def mostrar_cirujanos_por_centro():
    print ("Lista de cirujanos en centros: ")
    for centro in incucai.centros_salud:
        print (f"\nCirujanos en {centro.nombre}:")
        if centro.cirujanos:
            for cirujano in centro.cirujanos:
                print(f"- {cirujano.nombre} (DNI: {cirujano.dni} - Especialidad: {cirujano.especialidad})")
        else:
            print("Ningun cirujano asignado")



def menu ():
    while True:
        mostrar_titulo()
        print("1️⃣. Registrar nuevo paciente")
        print("2️⃣. Ver lista de donantes")
        print("3️⃣. Ver lista de receptores")
        print("4️⃣ .Ver lista de centros de salud")
        print("5️⃣. Ver lista de vehículos")
        print("6️⃣. Buscar receptores por centro de salud")
        print("7️⃣. Ver prioridad del receptor" )
        print("8️⃣. Ver lista de cirujanos por Centro")
        print("9️⃣. Salir")
        print("-" * 100)

        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            registrar_paciente()
            if not volver_al_menu():
                break
        elif opcion == "2":
            mostrar_donantes()
            if not volver_al_menu():
                break
        elif opcion == "3":
            mostrar_receptores()
            if not volver_al_menu():
                break
        elif opcion == "4":
            mostrar_centros()
            if not volver_al_menu():
                break
        elif opcion == "5":
            mostrar_vehiculos()
            if not volver_al_menu():
                break
        elif opcion == "6":
            buscar_receptores_por_centro()
            if not volver_al_menu():
                break
        elif opcion == "7":
            ver_prioridad_paciente()
            if not volver_al_menu():
                break
        elif opcion == "8":
            mostrar_cirujanos_por_centro()
            if not volver_al_menu():
                break
        elif opcion == "9":
            print("Saliendo del sistema.")
            break
        else: 
            print("Opcion inválida.")
        

inicializar_centros()

if __name__ == "__main__":
    menu()
        
