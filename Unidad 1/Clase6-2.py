cond = True
while cond:
    try:
        cantidadInvertida = float(input("Ingrese por favor la cantidad que desea invertir: "))
        interesDeseado = float(input("Ingrese a continuacion el numero de interes que desea ganar por año: "))
        añosDeseados = int(input("Ingrese el numero de años que desea invertir el dinero: "))
        
        for i in range(1, añosDeseados+1, 1):
            beneficioGanado = cantidadInvertida*interesDeseado/100
            cantidadInvertida = cantidadInvertida+beneficioGanado
            print(f"Udsted gana {cantidadInvertida} de beneficio el {i} año.")
            cond = False
            
    except:
        print("Usdetd ignreso un dato incorrecto.")





















