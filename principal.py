import os
import pickle

from registro import *

# MENU DE OPCIONES
def menu():
    menu = "=================================MENU DE OPCIONES====================================\n " \
           "===================================================================================\n " \
           "1. Crear archivo binario.  \n " \
           "2. Cargar datos de un ticket manualmente. \n " \
           "3. Mostrar datos de archivo binario. \n " \
           "4. Buscar patentes en el archivo. \n " \
           "5. Buscar registro por codigo de ticket. \n " \
           "6. Mostrar cantidad de vehiculos por tipo y pais de cabina.  \n " \
           "7. Cantidad total de vehiculos por tipo y por pais de cabina separados. \n " \
           "8. Tickets mayores a km promedio, de menor a mayor. \n " \
           "0. Salir\n " \
           "------------------------------------------------------------------------------------- \n " \
           "Elegir una opcion: "

    return int(input(menu))

#VALIDAR VALORES INGRESADOS POR TECLADO
def validar_entre(minimo, maximo, mensaje):
    num = int(input(mensaje))
    while minimo > num or num > maximo:
        print(f"Error, el numero debe estar entre {minimo} y {maximo}.")
        num = int(input(mensaje))
    return num

def validar_mayor(minimo, mensaje):
    num = int(input(mensaje))
    while num <= minimo:
        print(f"El numero debe ser mayor a {minimo}.")
        num = int(input(mensaje))
    return num

#CREAR ARCHIVO BINARIO
def leer_archivo(fd, archivo):
    if not os.path.exists(fd):
        print('El archivo', fd, 'no existe')
    else:
        m = open(fd, 'rt')
        b = open(archivo, "wb")
        size = os.path.getsize(fd)
        primera_linea = 0
        for linea in m:
            if primera_linea < 2:
                primera_linea += 1
                continue
            ticket = crear_alquiler(linea)
            pickle.dump(ticket, b)
        m.close()
        b.close()


# CARGA MANUAL DEL ARCHIVO BINARIO
def carga_manual(fd):
    ident = validar_mayor(0, "Ingrese el codigo de identificacion del vehiculo: \n")
    patente = input("Ingrese la patente del vehiculo en MAYUSCULAS: \n")
    tipo = validar_entre(0, 2, "Ingrese el tipo de vehiculo (0: motocicleta, 1: automóvil, 2: camión): \n")
    pago = validar_entre(1, 2, "Ingrese tipo de pago (1: manual, 2 telepeaje): \n")
    pais = validar_entre(0, 4, "Ingrese el país de la cabina (0: Argentina - 1: Bolivia - 2: Brasil - 3: Paraguay - 4: Uruguay): \n")
    km = validar_mayor(0, "Ingrese la distancia recorrida desde la cabina anterior: ")
    ticket = Ticket(ident, patente, tipo, pago, pais, km)
    m = open(fd, "ab")
    pickle.dump(ticket, m)
    m.close()

#MOSTRAR ARCHIVO BINARIO
def mostrar_archivo(arch):
    m = open(arch, "rb")
    size = os.path.getsize(arch)
    while m.tell() < size:
        tickets = pickle.load(m)
        print(tickets)
    m.close()



#MOSTRAR REGISTROS SEGUN PATENTE ELEGIDA
def mostrar_registro_pat(pat, arch):
    m = open(arch, "rb")
    size = os.path.getsize(arch)
    cpats = 0
    while m.tell() < size:
        tickets = pickle.load(m)
        if tickets.patente == pat:
            print(tickets)
            cpats += 1
    m.close()
    if cpats != 0:
        print(f"La cantidad de patentes que se encontraron fue de {cpats}. ")
    else:
        print("La patente no se pudo encontrar. ")

#MOSTRAR REGISTRO SEGUN CODIGO DE TICKET
def mostrar_registro_cod(id, arch):
    m = open(arch, "rb")
    size = os.path.getsize(arch)
    encontrado = False
    while m.tell() < size:
        tickets = pickle.load(m)
        if tickets.identidad == id:
            print(tickets)
            encontrado = True
            break
    m.close()
    if not encontrado:
        print("No se pudo encontrar un registro con ese codigo. ")

#MATRIZ DE CONTEO
def generar_conteo(arch):
    m = open(arch, "rb")
    size = os.path.getsize(arch)
    cant = [[0] * 5 for _ in range(3)]
    while m.tell() < size:
        tickets = pickle.load(m)
        t = tickets.tipo
        c = tickets.pais
        cant[t][c] += 1
    m.close()
    return cant

def mostrar_conteo(cant):
    for t in range(len(cant)):
        for c in range(len(cant[t])):
            if cant[t][c] != 0:
                print(f"Tipo: {t}  |  Pais de cabina: {c} ------> Cantidad de vehiculos: {cant[t][c]}")


#TOTALIZAR FILAS Y COLUMNAS
def totalizar_filas_columnas(cant):
    sumas_filas = []
    sumas_columnas = [0] * 5

    # Recorrer cada fila de la matriz y calcular la suma manualmente
    for fila in cant:
        suma_fila = 0
        for elemento in fila:
            suma_fila += elemento
        sumas_filas.append(suma_fila)


    for fila in cant:
        for i in range(5):
            sumas_columnas[i] += fila[i]

    # Ahora, sumas_filas contiene las sumas de las filas de la matriz
    for i in range(len(sumas_filas)):
        print(f"Tipo de vehiculo: {i} ---- Cantidad de vehiculos: {sumas_filas[i]}")

    for i in range(len(sumas_columnas)):
        print(f"Pais de cabina: {i} ---- Cantidad de vehiculos: {sumas_columnas[i]}")


#CALCULAR DISTANCIA PROMEDIO
def distancia_promedio(arch):
    m = open(arch, "rb")
    size = os.path.getsize(arch)
    suma, cant, prom = 0, 0, 0
    while m.tell() < size:
        tickets = pickle.load(m)
        suma += tickets.kilometro
        cant += 1
    if cant > 0:
        prom = suma / cant
    return prom


def cargar_arreglo(fd, prom):
    v = []
    if not os.path.exists(fd):
        print('El archivo', fd, 'no existe')
    else:
        m = open(fd, 'rb')
        size = os.path.getsize(fd)
        while m.tell() < size:
            tickets = pickle.load(m)
            if tickets.kilometro > prom:
                x = tickets
                add_in_order(v, x)
        m.close()
    return v

def add_in_order(v, x):
    n = len(v)
    izq, der, pos = 0, n-1, n
    while izq <= der:
        c = (izq + der) // 2
        if v[c].kilometro == x.kilometro:
            pos = c
            break
        if x.kilometro < v[c].kilometro:
            der = c - 1
        else:
            izq = c + 1
    if izq > der:
        pos = izq
    v[pos:pos] = [x]

def mostrar_vector(v):
    for ticket in v:
        print(ticket)


#PRINCIPAL
def principal():
    opc = -1
    size = 0
    while opc != 0:
        opc = menu()
        if os.path.exists("tickets.dat"):
            size = os.path.getsize("tickets.dat")

        if opc == 0:
            print("Gracias por usar el programa.")
        elif opc == 1:
            if not os.path.exists("tickets.dat"):
                leer_archivo("peajes-tp4.csv", "tickets.dat")
            else:
                dec = validar_entre(1, 2, "El archivo ya fue creado, quiere crearlo de nuevo desde cero? (1 (Si), 2 (No)): ")
                if dec == 1:
                    print("Se creo el archivo binario de nuevo. ")
                    leer_archivo("peajes-tp4.csv", "tickets.dat")
                else:
                    print("Se cancelo la operacion. ")
        elif opc == 2:
            if size == 0:
                print("El archivo no fue creado. ")
            else:
                carga_manual("tickets.dat")
        elif opc == 3:
            if size == 0:
                print("El archivo no fue creado. ")
            else:
                mostrar_archivo("tickets.dat")
        elif opc == 4:
            if size == 0:
                print("El archivo no fue creado. ")
            else:
                pat = input("Ingrese la patente que quiere buscar: ")
                mostrar_registro_pat(pat, "tickets.dat")
        elif opc == 5:
            if size == 0:
                print("El archivo no fue creado. ")
            else:
                id = validar_mayor(0, "Ingrese el codigo de ticket que quiere buscar: ")
                mostrar_registro_cod(id, "tickets.dat")
        elif opc == 6:
            if size == 0:
                print("El archivo no fue creado. ")
            else:
                conteo = generar_conteo("tickets.dat")
                mostrar_conteo(conteo)
        elif opc == 7:
            if size == 0:
                print("El archivo no fue creado. ")
            else:
                cant = generar_conteo("tickets.dat")
                totalizar_filas_columnas(cant)
        elif opc == 8:
            if size == 0:
                print("El archivo no fue creado. ")
            else:
                promedio = distancia_promedio("tickets.dat")
                v = cargar_arreglo("tickets.dat", promedio)
                mostrar_vector(v)
                print()
                print(f"Promedio: {promedio} km")
        else:
            print("Opcion incorrecta.")


if __name__ == '__main__':
    principal()
