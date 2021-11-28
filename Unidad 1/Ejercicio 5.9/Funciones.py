Taxis=[["Coche1","Coche2","Coche3"],["Federico","Nicolas","Manuel"],[10,30,50]]


def posibles_choferes():    
    while True:
        global Taxis
        try:
            tramo_ingresado = float(input("Ingrese a continiacion los kilometros del tramo que desea recorrer: "))
            if tramo_ingresado > 0:
                if tramo_ingresado <= 10:
                    print(f"""
                    Para este tramo uds puede utilizar: 
                    Coche: {Taxis [0] [0]} Chofer: {Taxis [1] [0]}
                    """)
                    break
                elif tramo_ingresado > 10 and tramo_ingresado <= 30:
                    print(f"""
                    Para este tramo uds puede utilizar: 
                    Coche: {Taxis [0] [0]}  Chofer: {Taxis [1] [0]}
                    Coche: {Taxis [0] [1]}  Chofer: {Taxis [1] [1]}
                    """)
                    break
                elif tramo_ingresado > 30:
                    print(f"""
                    Para este tramo uds puede utilizar: 
                    Coche: {Taxis [0] [0]}  Chofer: {Taxis [1] [0]}
                    Coche: {Taxis [0] [1]}  Chofer: {Taxis [1] [1]}
                    Coche: {Taxis [0] [2]}  Chofer: {Taxis [1] [2]}
                    """)
                    break
            else:
                print("Ingrese un numero mayor a 0.")
        except:
            print("Dato incorrecto, intente nuevamente.")

def modificar_nombre_chofer():    
    while True:
        global Taxis
        coche_elegido = input("Ingrese a continuacion el nombre del auto del cual desea cambiar el nombre de su respectivo chofer: ")
        if coche_elegido == "Coche1":
            while True:
                try:
                    nuevo_nombre0 = str(input("Ingrese el nuevo nombre del chofer."))
                    Taxis [1] [0] = nuevo_nombre0
                    break
                except:
                    print("Dato incorrecto.")
            print(f"El cambio se efectuo de manera correcta.")
            break
        elif coche_elegido == "Coche2":
            while True:
                try:
                    nuevo_nombre1 = str(input("Ingrese el nuevo nombre del chofer."))
                    Taxis [1] [1] = nuevo_nombre1
                    break
                except:
                    print("Dato incorrecto.")
            print(f"El cambio se efectuo de manera correcta.")
            break
        elif coche_elegido == "Coche3":
            while True:
                try:
                    nuevo_nombre2 = str(input("Ingrese el nuevo nombre del chofer."))
                    Taxis [1] [2] = nuevo_nombre2
                    break
                except:
                    print("Dato incorrecto.")   
            print(f"El cambio se efectuo de manera correcta.")
            break     
        else:
            print("No existe ningun coche con ese nombre intente nuevamente.")    

def modificar_recorrido():
    while True:
        global Taxis
        coche_elegido = input("Ingrese a continuacion el nombre del auto del cual desea cambiar el recorrido: ")
        if coche_elegido == "Coche1":
            while True:
                try:
                    nuevo_recorrido0 = int(input("Ingrese el nuevo nombre del chofer: "))
                    if nuevo_recorrido0 > 0:
                        Taxis [2] [0] = nuevo_recorrido0
                        break
                except:
                    print("Dato incorrecto.")
            print(f"El cambio se efectuo de manera correcta.")
            break
        elif coche_elegido == "Coche2":
            while True:
                try:
                    nuevo_recorrido1 = int(input("Ingrese el nuevo recorrido: "))
                    Taxis [2] [1] = nuevo_recorrido1
                    break
                except:
                    print("Dato incorrecto.")
            print(f"El cambio se efectuo de manera correcta.")
            break
        elif coche_elegido == "Coche3":
            while True:
                try:
                    nuevo_recorrido2 = str(input("Ingrese el nuevo recorrido: "))
                    Taxis [2] [2] = nuevo_recorrido2
                    break
                except:
                    print("Dato incorrecto.")   
            print(f"El cambio se efectuo de manera correcta.")
            break
        else:
            print("No existe ningun coche con ese nombre intente nuevamente.")    

def agregar_nuevo_coche():
    while True:
        global Taxis
        nombre_coche = input("Ingrese a continuacion el nombre del coche nuevo: ")
        if nombre_coche != " " and nombre_coche.isalnum():
            Taxis[0].append(nombre_coche)
            nombre_chofer = input("Ingrese a continuacion el nombre del nuevo chofer: ")
            if nombre_chofer.isalpha():
                Taxis[1].append(nombre_chofer)
                recorrido = input("Ingrese el recorrido maximo del nuevo coche: ")
                if int(recorrido) > 0 and recorrido.isdigit():
                    Taxis[2].append(recorrido)
                    break

def taxis_disponibles(): 
  print(f"\n-AUTO-   -CHOFER-   -DISTANCIA-")
  for i in range(len(taxis)): 
    print(f" {taxis[0][i]}   {taxis[1][i]}   {taxis[2][i]}")

def informacion_chofer():
    while True:
        global Taxis
        nombre = input("Ingrese el nombre del chofer que desea investigar: ")
        if nombre in Taxis [1]:
            posicion = Taxis[1].index(nombre)
            print(
        f"""
        Coche :     {Taxis [0] [posicion]}
        Chofer:     {Taxis [1] [posicion]}
        Recorrido:  {Taxis [2] [posicion]}
        """)
            break
        else:
            print("No existe ese chofer en nuestro sistema. Intente nuevamente...")

















