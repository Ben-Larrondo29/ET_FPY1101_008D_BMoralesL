#Funciones para PROGRAMA PRINCIPAL
import statistics
import random
import csv
from math import prod

trabajadores = ["Juan Pérez","Maria García","Carlos López","Ana Martínez","Pedro Rodríguez","Laura Hernández","Miguel Sánchez","Isabel Gómez","Francisco Díaz","Elena Fernández"]
sueldos=[]
def menu(lista):
    print('========================================')
    print('MENU')
    print('========================================')
    while True:
        i = 1
        for elem in lista:
            print(i, '.-', elem)
            i += 1
        print(i, '.- Salir')
        opc = input('Ingrese Opción: ')
        if opc.isdigit():
            opc_int = int(opc)
            if opc_int >= 1 and opc_int <= i:
                return opc_int
            else:
                print('Debe Ingresar un Número entre 1 y', i)
        else:
            print('Ingrese Sólo Números')

def sueldos_aleatorios():
    sueldos = {}
    for trabajador in trabajadores:
        sueldo = random.randint(300000,2500000)
        sueldos[trabajador] = sueldo
    return sueldos
    
def rango_sueldos(sueldos):
    if not sueldos:
        print("Aún se asignando los sueldos de los trabajadores")
    sueldos_bajo_800mil=[]
    sueldos_800mil_a_2millones=[]
    sueldos_mayor_a_2millones=[]
    for trabajador, sueldo in sueldos.items():
        if sueldo<800000:
            sueldos_bajo_800mil.append((trabajador,sueldo))
        elif sueldo>=800000 and sueldo<=2000000:
            sueldos_800mil_a_2millones.append((trabajador,sueldo))
        else:
            sueldos_mayor_a_2millones.append((trabajador,sueldos))
    print(f"Trabajadores con sueldo bajo 800.000:  {len(sueldos_bajo_800mil)}")
    for trabajador,sueldo in sueldos_bajo_800mil:
        print(f"{trabajador} : {sueldo}")
    print(f"Trabajadores con sueldo entre 800.000 a 2.000.000: {len(sueldos_800mil_a_2millones)}")
    for trabajador,sueldo in sueldos_bajo_800mil:
        print(f"{trabajador} : {sueldo}")
    print(f"Trabajadores con sueldo mayor a 2.000.000: {len(sueldos_mayor_a_2millones)}")
    for trabajador,sueldo in sueldos_bajo_800mil:
        print(f"{trabajador} : {sueldo}")


def estadisticas(sueldos):
    lista_de_sueldos=list(sueldos.values())
    sueldo_alto=max(lista_de_sueldos)
    sueldo_bajo=min(lista_de_sueldos)
    promedio_de_sueldos=statistics.mean(lista_de_sueldos)
    return sueldo_alto,sueldo_bajo,promedio_de_sueldos
def reporte_sueldo(sueldos):
    descuentos_salud={}
    descuentos_afp={}
    sueldos_liquidos={}
    for nombre,sueldo in sueldos.items():
        descuento_salud=sueldo*0.07
        descuentos_salud[nombre]=descuento_salud
        descuento_afp=sueldo*0.12
        descuentos_afp[nombre]=descuento_afp
        sueldo_liquido=sueldo-descuento_salud-descuento_afp
        sueldos_liquidos[nombre]=sueldo_liquido

def crear_reportecsv(sueldos):
    with open("reporte_de_sueldos.csv","w", encoding="utf-8") as archivo:
        creador=csv.writer(archivo)
        creador.writerow(['Nombre','Sueldo'])
        for nombre, sueldo in sueldos.items():
            creador.writerow([nombre,sueldo])




