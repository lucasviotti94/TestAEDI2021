def posibles_coches():
    while True:
        try:
            recorrido_ingresado = float(input("Ingrese a continuacion el recorrido en km que desea hacer: "))
        except:
            print("Dato ingresado incorrectamente.")
    if recorrido_ingresado <= 10:
        print("""Para este recorrido uds dispone de los siguientes coches:
        Coche 1 = Nombre de chofer: Juan Fernando
        Coche 2 = Nombre de chofer: Maximiliano
        Coche 3 = Nombre de chofer: Emilio    
        """)
















