"""El programa debe: gestorDePeliculas
*   Tener un menu con 7 opciones:
    1. Crear una pelicula y guardar su nombre (instancia) en una lista de peliculas.
    2. Verificar si la pelicula deseada existe en la lista de peliculas.
    3. Pedir a la lista de peliculas, todas las de un año.
    4. Presentar una pelicula de la lista
    5. Cambiar el genero de una pelicula
    6. Verificar el año de la pelicula
    7  Modificar puntuacion de la pelicula (entre 1 y 10)
    """
import Pelicula as pl
lista_peliculas = [] #empieza vacia
lista_generos = ["Terror", "Comedia", "Thriller", "Musical", "Suspenso", "Romantica"]

class GestorDePeliculas:
    def __init__(self):
        pass

    def imprimir_lista(self):
        for peliculas in lista_peliculas:
            print(peliculas.nombre)
            
    def crear_peliculas(self):
        #Nombre
        while True:
            nombre = input("Ingrese el nombre de la pelicula: ").capitalize()
            if(self.verificar_pelicula(nombre) == False):
                break
        #Año
        while True:
            try:
                año_ingresado = int(input("Ingrese el año de la pelicula: "))
                if año_ingresado > 0 and año_ingresado <= 2021:
                    print(f"Año ingresado correctamente: {año_ingresado}")
                    break
                else:
                    print("Ingrese un numero mayor a cero y menor a 2022")
            except:
                print("Por favor ingrese solo numeros enteros...")
        #Genero
        while True:
            genero_ingresado = input("A continuacion ingrese el genero de la pelicula: ").capitalize()
            if genero_ingresado in lista_generos:
                print(f"Genero ingresado de manera correcta: {genero_ingresado}.")
                break
            else:
                print("Por favor ingrese uno de los generos de la lista: ")
                print(lista_generos)
        #Nacionalidad
        while True:
            nacionalidad_ingresada = input("Ingrese a continuacion la nacionalidad de la pelicula: ").capitalize()
            if nacionalidad_ingresada.isalpha():
                print(f"Nacionalidad ingresada correctamente: {nacionalidad_ingresada}")
                break
            else:
                print("No existen nacionalidades con simbolos o numeros, intente nuevamente...")
        #Puntuacion
        while True:
            try:
                puntuacion_ingresada = int(input("Ingrese a continuacion la puntuacion de la pelicula: "))
                if puntuacion_ingresada >0 and puntuacion_ingresada <= 10:
                    print(f"Puntuacion ingresada correctamente: {puntuacion_ingresada}")
                    break
                else:
                    print("Ingrese una puntuacion mayor a cero y menor a 11.")
            except:
                print("Ingrese solamente numeros...") 

        nombre_intancia = nombre
        nombre_intancia = pl.Pelicula(nombre,año_ingresado,genero_ingresado,nacionalidad_ingresada,puntuacion_ingresada)
        lista_peliculas.append(nombre_intancia)            

    def verificar_pelicula(self,nombre_pelicula = "null"):
        while True:
            if (nombre_pelicula == "null"):
                nombre_pelicula = input("Ingrese el nombre de la pelicula a verificar: ").capitalize()

            for peliculas in lista_peliculas:
                if nombre_pelicula == peliculas.nombre:
                    print("Esta pelicula ya existe")
                    return True

            print("Esta pelicula no existe")
            return False

    def pedir_peliculas_por_año(self):
        while True:
            try:
                año_pedido = int(input("Ingrese a continuacion el año de las peliculas que desea encontrar: "))
                for peliculas in lista_peliculas:
                    if año_pedido == peliculas.año:
                        print(peliculas.nombre)
                return
            except:
                print("Ingrese unicamente numeros enteros...")

    def presentar_pelicula_ingresada(self):
        while True:
            pelicula_elegida = input("Ingrese a continuacion la pelicula que desea presentar: ").capitalize()
            for peliculas in lista_peliculas:
                if pelicula_elegida == peliculas.nombre:
                    peliculas.presentar_pelicula()
                    return
                else:
                    print("Ingrese una pelicula de la lista...")
                    print(peliculas.nombre)
    
    def cambio_de_genero(self):
        while True:
            peli_elegida = input("Ingrese a continuacion la pelicula a la que desea cambiarle el genero: ").capitalize()           
            for peliculas in lista_peliculas:
                if peli_elegida == peliculas.nombre:
                    while True:
                        genero_nuevo = input(f"Ingrese a continuacion el nuevo genero de la pelicula {peli_elegida}: ")
                        if genero_nuevo in lista_generos and genero_nuevo != peliculas.genero:
                            peliculas.cambiar_genero(genero_nuevo)
                            print(f"Se cambio el genero de la pelicula {peli_elegida} a {genero_nuevo} de manera correcta.")
                            return
                        else:
                            print("Por favor ingrese un genero de la lista...")
                            print(lista_generos)
                else:
                    print("Por favor ingrese una pelicula de la lista...")
                    print(peliculas.nombre)
    def modificar_puntaje(self):
        while True:
            pelicula_elegida = input("Ingrese a continuacion la pelicula a la cual desea cambiarle el puntaje: ").capitalize()
            for peliculas in lista_peliculas:
                if pelicula_elegida == peliculas.nombre:
                    while True:
                        try:
                            puntaje_nuevo = int(input(f"Ingrese a continuacion el nuevo puntaje de la pelicula {pelicula_elegida}"))
                            if puntaje_nuevo >0 and puntaje_nuevo <11:
                                peliculas.modificar_puntuacion(puntaje_nuevo)
                                return
                            else:
                                print("Ingrese un numero mayor a cero y menor a once..")
                        except:
                            print("Ingrese solo numeros enteros.")
                else:
                    print("Ingrese una pelicula de la lista...")
                    print(peliculas.nombre)            













