#PROGRAMA PRINCIPAL
import os
os.system('cls')
from funcioneset import menu,sueldos_aleatorios,rango_sueldos,estadisticas,reporte_sueldo,crear_reportecsv
sueldos={}
tipo_opc=["Asignar sueldos aleatorios", "Clasificar sueldos", "Ver estadisticas", "Reporte de sueldos"]
#Menu de interacción
while True:
    opc=menu(tipo_opc)
#Llamar opciones
    if opc==1:
        sueldos=sueldos_aleatorios()
        for nombre,sueldo in sueldos.items():
            print(f"{nombre} : {sueldo}")
    elif opc==2:
        rango_sueldos(sueldos)
    elif opc==3:
        sueldo_alto,sueldo_bajo,promedio_de_sueldos=estadisticas(sueldos)
        print(" ")
        print(f"Sueldo más alto: {sueldo_alto}")
        print(" ")
        print(f"Sueldo más bajo: {sueldo_bajo}")
        print(" ")
        print(f"Promedio de sueldos: {promedio_de_sueldos}")
        print(" ")
    elif opc==4:
        reporte_sueldo(sueldos)
        crear_reportecsv(sueldos)
    elif opc==5:
        print('Desarrollado por Benjamín Ignacio Morales Larrondo')
        print('RUT 21.949.603-6')
        break

