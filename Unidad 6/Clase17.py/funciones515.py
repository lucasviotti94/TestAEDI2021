base = {
    "peliculas" : ["El hombre araña", "Los vengadores" , "Los vengadores 2"],
    "series" : ["prision break", "la casa de papel" , "los simpsons"]
        }

def mostrar_bases():
    while True:
        base_mostrar = input(
        """
-----------Menu BASES-----------
Ingrese si requiere ver:
1. la lista de peliculas
2. la lista de series
3. Salir
opcion:  """)
        if base_mostrar =="1":
            print(f"---------Peliculas---------")
            for i in range(len(base.get("peliculas"))):
                print(base.get("peliculas")[i])
        elif base_mostrar == "2":
            print(f"---------Series---------")
            for i in range(len(base.get("series"))):
                print(base.get("series")[i])
        elif base_mostrar == "3":
            break
        else:
            print("Opcion incorrecta")

def agregar_peliculas_series():
    while True:
        base_mostrar = input(
        """
-----------Menu AGREGAR-----------
Ingrese que requiere agregar:
1. Peliculas
2. Series
3. Salir
opcion: """)
        if base_mostrar =="1":
            nombre_pelicula = input("Ingrese el nombre de la nueva pelicula: ")
            if nombre_pelicula not in base.get("peliculas"):
                base.get("peliculas").append(nombre_pelicula.capitalize())
            else:
                print("esta pelicula ya s eencuentra en la lista...")
        elif base_mostrar == "2":
            nombre_series = input("Ingrese el nombre de la nueva serie: ")
            if nombre_series not in base.get("series"):
                base.get("series").append(nombre_series.capitalize())
            else:
                print("esta serie ya se encuentra en la lista...")
        elif base_mostrar == "3":
                break
        else:
                print("Opcion incorrecta")

def eliminar_peliculas_series():
    while True:
        base_mostrar = input(
        """
-----------Menu ELIMINAR-----------
Ingrese si requiere eliminar:
1. Peliculas
2. Series
3. Salir
opcion: """)
        if base_mostrar =="1":
            lista_peliculas = base.get("peliculas")
            print(lista_peliculas)
            nombre_pelicula = input("Ingrese el nombre de la pelicula a eliminar: ")
            if nombre_pelicula in lista_peliculas:
                base.get("peliculas").remove(nombre_pelicula)
            else:
                print("ese nombre no existe")
        elif base_mostrar == "2": 
            lista_series = base.get("series")
            print(lista_series)
            nombre_series = input("Ingrese el nombre de la pelicula a eliminar: ")
            if nombre_series in lista_series:
                base.get("series").remove(nombre_series)
            else:
                print("ese nombre no existe")
        elif base_mostrar == "3":
                break
        else:
                print("Opcion incorrecta")

def mostrar_de_A_B():
    while True:
        base_mostrar = input(
        """
-----------Menu MOSTRAR-----------
Ingrese si requiere mostrar:
1. Peliculas
2. Series
3. Salir
opcion:  """)
        if base_mostrar =="1":
            list_peliculas = base.get("peliculas") 
            print(list_peliculas)            
            while True:
                try:
                    primera_posicion = int(input("Ingrese la primera posición: "))
                    segunda_posicion = int(input("Ingrese la ultima posición: "))
                    break
                except:
                    print("Ingreso un dato incorrecto, intente nuevamente.")
            for i in range(primera_posicion-1,segunda_posicion):
                print(list_peliculas[i],end="-")
        elif base_mostrar == "2":
            list_series = base.get("series") 
            print(list_series)
                #falta try excecpt
            primera_posicion =int(input("Ingrese la primera posición: "))
            segunda_posicion = int(input("Ingrese la ultima posición: "))
            for i in list_series[primera_posicion-1,segunda_posicion-1 ]:
                print(i,end="-")
        elif base_mostrar == "3":
                break
        else:
                print("Opcion incorrecta")

"""5. Buscar peliculas o series que contengan una palabra requerida por el usuario. (ej. input("el"), 
        se liste las peliculas que contengan la palabra "el")."""

def busqueda_palabra():
    while True:
        base_mostrar = input(
        """
-----------Menu BUSQUEDA-----------
Ingrese si requiere buscar en:
1. Peliculas
2. Series
3. Salir
opcion:  """)
        if base_mostrar =="1":
            lista_peliculas = base.get("peliculas")    
            palabra_requerida = input("Ingrese la palabra a buscar: ")
            for pelicula in lista_peliculas:
                if palabra_requerida in pelicula:
                    print(f"La palabra {palabra_requerida} esta en {pelicula}")
        elif base_mostrar == "2":
            list_series = base.get("series") 
            palabra_requerida = input("Ingrese la palabra a buscar: ")
            for serie in list_series:
                if palabra_requerida in serie:
                    print(f"La palabra {palabra_requerida} esta en {serie}")
        elif base_mostrar == "3":
                break
        else:
                print("Opcion incorrecta")