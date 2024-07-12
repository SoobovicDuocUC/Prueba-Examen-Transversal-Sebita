import random
import csv

nombres = [
    "Garcia Gonzalez",
    "Juan Perez",
    "Ana Lopez",
    "Carlos Sanchez",
    "Laura Fernandez",
    "Luis Rodriguez",
    "Elena Martinez",
    "Pedro Garcia",
    "Carmen Jimenez",
    "Miguel Hernandez"
]

sueldo_trabajadores = []

with open("sueldos_trabajadores.csv", "w") as archivo:
    archivo.write("NOMBRE COMPLETOP -  SUELDO BASE -  DESCUENTO SALUD -  DESCUENTO AFP -  SUELDO LIQUIDO\n")
def sueldos_aleatorios():
    sueldo_trabajadores.clear()
    for numero in range(len(nombres)):
        sueldo_trabajadores.append({"nombre": nombres[numero], "sueldo": random.randint(300000, 2500000)})
    return "Finalizado"

def estadisticas():
    print("")
    total = sum(trabajador["sueldo"] for trabajador in sueldo_trabajadores)
    max_sueldo = max(sueldo_trabajadores, key=lambda x: x["sueldo"])
    min_sueldo = min(sueldo_trabajadores, key=lambda x: x["sueldo"])
    promedio = total / len(nombres)
    

    print("El Sueldo Mas alto es:", max_sueldo)
    print("El Sueldo mas bajo es:", min_sueldo)
    print("Los promedios de sueldo se muestran a continuacion:", promedio)

def clasificar_sueldos():
    print("")
    menores_800 = [trabajador for trabajador in sueldo_trabajadores if trabajador["sueldo"] < 800000]
    entre_800_y_2M = [trabajador for trabajador in sueldo_trabajadores if 800000 <= trabajador["sueldo"] <= 2000000]
    mayores_2M = [trabajador for trabajador in sueldo_trabajadores if trabajador["sueldo"] > 2000000]

    print("---SUELDOS BAJO $800.000---")
    print(f"En Total hay: {len(menores_800)}")
    for trabajador in menores_800:
        print(f'{trabajador["nombre"]} -> ${trabajador["sueldo"]}')
    print()

    print("---SUELDOS ENTRE $800.000 y $2.000.000---")
    print(f"En Total hay: {len(entre_800_y_2M)}")
    for trabajador in entre_800_y_2M:
        print(f'{trabajador["nombre"]} -> ${trabajador["sueldo"]}')
    print()

    print("---SUELDOS ARRIBA DE $2.000.000---")
    print(f"En Total hay: {len(mayores_2M)}")
    for trabajador in mayores_2M:
        print(f'{trabajador["nombre"]} -> ${trabajador["sueldo"]}')
    print()

    total_sueldos = sum(trabajador["sueldo"] for trabajador in sueldo_trabajadores)
    print(f"EL TOTAL DE LOS SUELDOS SE PRESENTA A CONTINUACION: ${total_sueldos}")


def reporte_de_sueldos():
    with open("sueldos_trabajadores.csv", "a") as archivo:
        for sueldos in sueldo_trabajadores:
            descuento= 0.07 * sueldos["sueldo"]
            descuento= descuento.__trunc__()
            afp= 0.12 * sueldos["sueldo"]
            afp= afp.__trunc__()
            sueldo_liquido = sueldos["sueldo"] - descuento - afp
            archivo.write(f'{sueldos["nombre"]}, - {sueldos["sueldo"]}, - {descuento}, - {afp}, - {sueldo_liquido}\n')

while True:
    print("")
    print("1) Generar Sueldos Aleatorios")
    print("2) Clasificar sueldos")
    print("3) Ver estadísticas")
    print("4) Generar CSV")
    print("5) Salir del programa")
    print("")
    try:
        menu = int(input("Seleccione una opción: "))
    except ValueError:
        print("----POR FAVOR SELECCIONE UNA OPCION DESTACADA----")
    else:
        match menu:
            case 1:
                sueldos_aleatorios()
                print("")
                print("-----El Proceso aleatorio ya fue generado-----")
            case 2:
                clasificar_sueldos()
                print("")
                print("---Los Datos han sido generados---")
            case 3:
                estadisticas()
                print("")
                print("---Los Datos han sido generados---")
            case 4: 
                reporte_de_sueldos()
                print("")
                print("-----El Archivo fue creado exitosamente-----")
            case 5:
                print("")
                print("------ Cerrando Programa ------")
                print("------ DESARROLLADO POR -------")
                print("--- Sebastian Araya Romanini ---")
                print("-------- 21.173.058-7 -------- ")
                break
                exit
