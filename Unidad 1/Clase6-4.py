def viajes():
    lista = [ ]
    acumulador_duracion = 0
    while True:
        try:
            tramos = int(input("Ingresar la cantidad de tramos: "))
            if tramos <= 0:
                print("Error, ingrese un numero mayor a 0.")                
            else:  
                break
        except:
            print("Error.")
    while True:
        for i in range(tramos):
            duracion_tramo = input(f"Ingrese la duracion del {i+1} tramo, en minutos.")
            if duracion_tramo.isdigit():            
                duracion_tramo.append(lista)
                acumulador_duracion += duracion_tramo
            else:
                print("Error")



viajes()    