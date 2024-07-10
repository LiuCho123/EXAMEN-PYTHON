import csv, random
from statistics import geometric_mean

trabajadores = ["Juan Perez", "María Garcia", "Carlos Lopez", "Ana Martinez", "Pedro Perez",
                "Laura Gil", "Miguel Sanchez", "Isabel Gomez", "Francisco Diaz", "Elena Cabello"]
sueldos = []
sueldosTrabajador = []
trabajadoresEnPantalla = {}

def simularSueldos(trabajadores):
    for trabajador in trabajadores:
        sueldo = random.randint(300000, 2500000)
        sueldos.append(sueldo)
    
        for sueldo in sueldos:
            descSalud = round(sueldo * 0.07)
            descAFP = round(sueldo * 0.12)
            sueldoLiquido = sueldo - descSalud - descAFP

        sueldosTrabajador.append({"Nombre": trabajador,
                                "Sueldo": sueldo})
        
        trabajadoresEnPantalla[sueldo] = {"Nombre": trabajador,
                                  "Sueldo": sueldo,
                                  "Descuento Salud": descSalud,
                                  "Descuento AFP": descAFP,
                                  "Sueldo Liquido": sueldoLiquido}
        
    print(sueldosTrabajador)

def clasificarSueldos(trabajadores):
    if not sueldos:
        print("-----------------------------------------")
        print("          Sueldos aún no simulados")
        print("-----------------------------------------")
        pass
    else:
        sueldoMenor= 0
        sueldoPromedio = 0
        sueldoMayor = 0
        totalSueldos = 0
        for sueldo in sueldos:
            totalSueldos += sueldo
            if sueldo <800000:
                sueldoMenor += 1
            elif sueldo >=800000 and sueldo <= 2000000:
                sueldoPromedio +=1
            elif sueldo > 2000000:
                sueldoMayor += 1

        print(f"Sueldos menores a $800.000 TOTAL: {sueldoMenor}")

        print(f"Sueldos entre $800.000 y $2.000.000 TOTAL: {sueldoPromedio}")

        print(f"Sueldos superiores a $2.000.000 TOTAL: {sueldoMayor}")

        print(f"TOTAL SUELDOS: {totalSueldos}")

def estadisticasDeSueldos(trabajadores):
    if not sueldos:
        print("-----------------------------------------")
        print("          Sueldos aún no simulados")
        print("-----------------------------------------")
        pass
    else:
        sueldos.sort()
        totalSueldos = 0
        for sueldo in sueldos:
            totalSueldos += sueldo
        promedio = (round(totalSueldos / len(sueldos)))
        geo = round(geometric_mean(sueldos))

        print(f"El sueldo más alto es de ${sueldos[-1]}")
        print(f"El sueldo más bajo es de ${sueldos[0]}")
        print(f"El promedio de sueldos es {promedio}")
        print(f"La media geométrica de sueldos es {geo}")

def reporteDeSueldos(trabajadores):
    if not sueldos:
        print("-----------------------------------------")
        print("          Sueldos aún no simulados")
        print("-----------------------------------------")
        pass
    else:
        print("Nombre Empleado      Sueldo Base         Descuento Salud         Descuento AFP       Sueldo Liquido")
        for trabajador, datos in trabajadoresEnPantalla.items():
                print(f"{datos['Nombre']},\t {datos['Sueldo']},\t\t {datos['Descuento Salud']},\t\t\t {datos['Descuento AFP']},\t\t {datos['Sueldo Liquido']}")

        with open("trabajadoresSueldos.csv", "w", newline="") as archivoCSV:
            escritor = csv.writer(archivoCSV, delimiter=",")
            escritor.writerow(["Nombre", "Sueldo", "Descuento Salud", "Descuento AFP", "Sueldo Liquido"])
            for trabajador, datos in trabajadoresEnPantalla.items():
                nombre = datos["Nombre"]
                sueldo = datos["Sueldo"]
                descuentoSalud = datos["Descuento Salud"]
                descuentoAFP = datos["Descuento AFP"]
                sueldoLiquido = datos["Sueldo Liquido"]
                escritor.writerow([nombre, sueldo, descuentoSalud, descuentoAFP, sueldoLiquido])
            print("Se ha generado ´trabajadoresSueldos.csv' éxitosamente")
            
while True:
    print("Bienvenido al sistema de simulación de sueldos")
    print("-----------------------------------------")
    print("¿Qué desea hacer?")
    print("1. Asignar sueldos aleatorios")
    print("2. Clasificar sueldos")
    print("3. Ver estadísticas")
    print("4. Reporte de sueldos")
    print("5. Salir del programa")
    print("-----------------------------------------")

    try:
        menu = int(input("Seleccione una opción: "))
    except ValueError:
        print("Ingrese un número, no una letra")
        continue

    if menu == 1:
        simularSueldos(trabajadores)

    elif menu == 2:
        clasificarSueldos(trabajadores)
    
    elif menu == 3:
        estadisticasDeSueldos(trabajadores)

    elif menu == 4:
        reporteDeSueldos(trabajadores)

    elif menu == 5:
        print("Finalizando programa...")
        print("Desarrollado por Luis Cabello")
        print("RUT 22.072.892-7")
        break

    elif menu == "":
        print("Seleccione una opción")

