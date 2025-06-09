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


organos_validos = ["corazon", "higado", "pancreas", "huesos", "rinion", "pulmones", "intestino", "piel", "corneas"]
tipos_sangre = ["A+", "A-","B+", "B-","AB+", "AB-","O+", "O-"]
prioridad_opciones = ["Alta", "Media", "Baja"]
sexo_opciones = ["Masculino", "Femenino"]

def inicializar_centros():
    centro1 = Centro_salud("Hospital Zonal Pergamino", "Liniers 979", "Pergamino", "Buenos Aires", "02477 - 429792")
    centro2 = Centro_salud("Hospital Blas L. Dubarry", "Calle 12 nro 825", "Mercedes", "Buenos Aires", "02324 - 425555")
    centro3 = Centro_salud("Hospital Garrahan", "Brasil 2150", "CABA","Buenos Aires", "0114122-6000")
    centro4 = Centro_salud("Hospital Italiano", "Gascon 450", "CABA", "Buenos Aires", "01149590200")
    centro5 = Centro_salud("Hospital San Martín", "Av. 1 y 70", "La Plata", "Buenos Aires", "02214255500")
    centro6 = Centro_salud("Hospital El Cruce", "Camino Gral Belgrano 5400", "Florencio Varela", "Buenos Aires", "01142105200")

    # Cirujanos para el centro 1(Pergamino)
    cirujano_p1 = Cirujano("Dr. Facundo Capdevila", 30111222, datetime(1978, 3, 15), "Masculino", "1123456789", "cardiovascular")
    cirujano_p2 = Cirujano("Dra. Luisa De Pascua Ruckauf", 32333444, datetime(1985, 7, 20), "Femenino", "1134567890", "general")
    cirujano_p3 = Cirujano("Dr. Agustin Marino Aguirre", 28999888, datetime(1970, 11, 5), "Masculino", "1145678901", "gastroenterologo")

    # Cirujanos para el centro 2(Mercedes)
    cirujano_m1 = Cirujano("Dra. Olivia Puricelli", 35555666, datetime(1982, 4, 10), "Femenino", "1156789012", "traumatologo")
    cirujano_m2 = Cirujano("Dr. Simón Montero", 31777888, datetime(1979, 9, 25), "Masculino", "1167890123", "general")

    # Cirujanos para el centro 3 (Garrahan)
    cirujano_g1 = Cirujano("Dr. Santino Carbone", 25123456, datetime(1965, 1, 1), "Masculino", "1178901234", "plastico") 
    cirujano_g2 = Cirujano("Dra. Martina Collazo", 38987654, datetime(1992, 6, 30), "Femenino", "1189012345", "general")
    cirujano_g3 = Cirujano("Dr. Nehuen Español ", 29000111, datetime(1973, 2, 8), "Masculino", "1190123456", "traumatologo")

    # Cirujanos para el centro 4 (Italiano)
    cirujano_i1 = Cirujano("Dra. Francisca Marciano", 27000333, datetime(1968, 10, 12), "Femenino", "1110203040", "gastroenterologo")
    cirujano_i2 = Cirujano("Dra. Milena Lettieri", 34567890, datetime(1987, 5, 5), "Femenino", "1120304050", "general")

    # Cirujanos para el centro 5 (San Martin)
    cirujano_s1 = Cirujano("Dr. Rodolfo Abud", 26112233, datetime(1971, 7, 1), "Masculino", "1130405060", "pulmonar")
    cirujano_s2 = Cirujano("Dra. Dorina Trovato", 36778899, datetime(1989, 2, 28), "Femenino", "1140506070", "general")

    # Cirujanos para el centro 6 (El Cruce)
    cirujano_e1 = Cirujano("Dr. Guillermo Klein", 24998877, datetime(1960, 12, 1), "Masculino", "1150607080", "cardiovascular")
    cirujano_e2 = Cirujano("Dra. Victoria Faro", 33445566, datetime(1981, 8, 18), "Femenino", "1160708090", "general")

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

#órganos para donantes
    organos1 = [Organo("corazon")]
    organos2 = [Organo("higado"), Organo("corneas")]
    organos3 = [Organo("pulmones"), Organo("piel")]
    organos4 = [Organo("huesos")]
    organos5 = [Organo("corazon"), Organo("higado")]
    organos6 = [Organo("pancreas")]
    
#Donantes
    d1 = Donante("Lisandro Romero", 12345678, datetime(1980,5,10), "M", "1111111111", "A+", centro1,
                 datetime(2025,5,1,14,30), datetime(2025,5,1,16,0), organos1)
    centro1.donantes.append(d1)
    d2 = Donante("Manuela Desuque", 23456789, datetime(1975,8,22), "F", "2222222222", "O-", centro2,
                 datetime(2025,4,28,9,15), datetime(2025,4,28,11,0), organos2)
    centro2.donantes.append(d2)
    d3 = Donante("Matias Suarez", 34567890, datetime(1990,3,3), "M", "3333333333", "B+", centro3,
                 datetime(2025,5,10,18,0), datetime(2025,5,10,19,30), organos3)
    centro3.donantes.append(d3)
    d4 = Donante("Zoe Pfiefer", 45612378, datetime(1982, 9, 12), "F", "777777777", "B-", centro4,
             datetime(2025, 5, 5, 12, 0), datetime(2025, 5, 5, 13, 30), organos4)
    centro4.donantes.append(d4)
    d5 = Donante("Valen Perez", 56123987, datetime(1978, 11, 3), "M", "888888888", "AB+", centro5,
             datetime(2025, 5, 7, 9, 15), datetime(2025, 5, 7, 10, 0), organos5)
    centro5.donantes.append(d5)
    d6 = Donante("Ludmila Esposito", 49876543, datetime(1992, 2, 18), "F", "999999999", "A-", centro6,
             datetime(2025, 5, 10, 11, 0), datetime(2025, 5, 10, 12, 0), organos6)
    centro6.donantes.append(d6)


#Receptores
    r1 = Receptor("Miranda Klein", 45678901, datetime(2000,1,15), "F", "4444444444", "A+", centro1, "corazon",
                  datetime(2025,5,20), 1, "Cardiopatía congénita")
    centro1.Receptor.append(r1)
    r2 = Receptor("Conrado Abud", 56789012, datetime(1985,9,30), "M", "5555555555", "O-", centro2, "higado",
                  datetime(2025,4,10), 2, "Hepatitis crónica")
    centro2.Receptor.append(r2)
    r3 = Receptor("Teresa Moraiz", 67890123, datetime(1995,12,5), "F", "6666666666", "B+", centro3, "pulmones",
                  datetime(2025,3,25), 3, "Fibrosis quística")
    centro3.Receptor.append(r3)
    r4 = Receptor("Guido Mocagatta", 41234567, datetime(1990, 8, 9), "M", "101010101", "B-", centro4, "rinion", 
              datetime(2025, 5, 21), 2, "Insuficiencia renal crónica")
    centro4.Receptor.append(r4)
    r5 = Receptor("Juana Larrumbide", 48765432, datetime(1986, 4, 27), "F", "121212121", "AB+", centro5, "higado", 
              datetime(2025, 5, 22), 1, "Hepatitis autoinmune")
    centro5.Receptor.append(r5)
    r6 = Receptor("Katerina Josipovich", 47891236, datetime(1999, 1, 5), "F", "131313131", "A-", centro6, "pancreas", 
              datetime(2025, 5, 23), 3, "Diabetes tipo 1")
    centro6.Receptor.append(r6)

    
    for d in [d1, d2, d3, d4, d5, d6]:
        incucai.Registrar_Paciente(d)
    for r in [r1, r2, r3, r4, r5, r6]:
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
            opcion = lista[int(ingreso)- 1]
            if opcion in seleccionados:
                print(f"'{opcion}' ya fue seleccionado una vez. Ingrese nuevamente")
                continue
            else:
                seleccionados.append(opcion)
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
        if ingreso.lower() == "menu":
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
        if patologia.replace(" ","").isalpha():
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
    sexo = 'M' if sexo_op.__eq__("Masculino") else "F" #metodo magico

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
        while True:
            fecha_fallecimiento = ingresar_fecha_hora("Fecha y hora de fallecimiento (DD/MM/AAAA HH:MM): ")
            if fecha_fallecimiento is None:
                return
        
            fecha_ablacion = ingresar_fecha_hora("Fecha y hora de ablación (DD/MM/AAAA HH:MM): ")
            if fecha_ablacion is None:
                return
        
            if fecha_nacimiento <= fecha_nacimiento:
                print("La fecha de fallecimiento no puede ser anterior o  igual a la fecha de nacimiento.")
                continue

            if fecha_ablacion < fecha_fallecimiento:
                print("La fecha de ablanción no puede ser anterior a la fecha de fallecimiento")
                continue

            if fecha_ablacion <= fecha_nacimiento:
                print("La fecha de ablación no puede ser anterior o igual a la fecha de nacimiento.")
                continue

            break
        
        organos_lista = seleccionar_multiples_opciones(organos_validos, "Seleccione los organos a donar (0 para finalizar): ")
        if organos_lista is None or len(organos_lista) == 0:
            return
        organos = [Organo(o) for o in organos_lista] #convierte cada string de la lista en un objeto de la clase Organo

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
        try:
            incucai.Registrar_Paciente(receptor)
            print("El receptor fue registrado correctamente")
        except Exception as e: 
            print(f"Error al registrar al receptor.")

def mostrar_donantes():
   
    print("Lista de donantes: ")
    for d in incucai.donantes:
        organos_donante = []
        for o in d.organos:
            organos_donante.append(o.tipo)
        print(f"{d.nombre} ({d.dni}) _ Organos a donar: {organos_donante}")

def mostrar_receptores():
   
    print("Lista de receptores: ")
    for recep in incucai.receptores:
        print(f"{recep.nombre} ({recep.dni}) _ Organos necesarios: {recep.organo_necesario} _ Prioridad: {recep.prioridad} _Estado: {recep.estado}")

def buscar_receptores_por_centro():

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

def inicializar_proceso_transplante():
    hubo_compatibilidad = False #si hay almenos uno transplante (en los ejemplos hay varios)
    for donante_obj in incucai.donantes:
        if not donante_obj.organos: #esto hace que saltee a los donantes que ya no tienen organospara donar
            continue
        
        compatibilidades = incucai.buscar_receptor_para_donante(donante_obj)

        if compatibilidades:
            for donante, receptor, organo in compatibilidades:
                print("\n---------------------------------")
                print(f"Compatibilidad encontrada:")
                print(f"- Donante: {donante.nombre}")
                print(f"- Receptor: {receptor.nombre}")
                print(f"- Órgano a donar/recibir: {organo.tipo}.")
                incucai.realizar_transplante(donante, receptor, organo)

                if receptor not in incucai.receptores:
                    print(f"Trasnplante de {organo.tipo} realizado con éxito para {receptor.nombre}.")
                    print("El paciente fue removido de la lista de receptores.")
                elif receptor.estado == "Inestable" and receptor.prioridad == 1:
                    print(f"Transplante de {organo.tipo} para {receptor.nombre} no fue exitoso.")
                    print("El paciente se encuentra en estado inestable con alta prioridad")
                else: 
                    print(f"Transplante de {organo.tipo} para {receptor.nombre} se llevó a cabo.")
                    print("Estado actual del paciente: {receptor.estado}")

                hubo_compatibilidad= True  
    if not hubo_compatibilidad:            
        print("\nNo se pudo encontrar un donante y receptor compatibles para el transplante en este momento.")

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
        print("9️⃣. Proceso de transplante")
        print("🔟. Salir")
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
            inicializar_proceso_transplante()
            if not volver_al_menu():
                break
        elif opcion == "10":
            print("Saliendo del sistema.")
            break
        else: 
            print("Opcion inválida.")
        

inicializar_centros()

if __name__ == "__main__":
    menu()
        
