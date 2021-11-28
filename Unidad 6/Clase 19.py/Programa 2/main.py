"""
###**Ejercicio 6.3**
Crear una clase de Peliculas:
*   Cuyo constructutor debe inicializar los atributos nombre, año, genero, nacionalidad, puntuacion
*   Se deben crear 4 metodos en la clase:
    1.  Presentar la pelicula: La pelicula {nombre} de {genero} del {año} obtuvo una puntuacion de {puntuacion}  
        y fue filmada en {nacionalidad}
    2. Retornar si el año de la pelicula es mayor o igual o menor al pasado por parametro
    3. Cambiar el genero de una pelicula
    4. Modificar puntuacion de la pelicula

El programa debe: gestorDePeliculas
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
import gestorDePeliculas as gp

gestor = gp.GestorDePeliculas()
while True:
    opcion = input(
    """
-----------Menu principal-----------
Por favor ingrese una opcion:
    1. Crear pelicula.
    2. Verificar pelicula.
    3. Imprimir lista.
    4. Pedir listado de peliculas por año.
    5. Presentar una pelicula deseada.
    6. Cambiar genero de la pelicula deseada.
    7. Modificar puntuacion de la pelicula deseada.
    8. Salir
    Opcion: """
    )
    if (opcion=="1"):
        gestor.crear_peliculas()
    elif (opcion=="2"):
        gestor.verificar_pelicula()
    elif (opcion=="3"):
        gestor.imprimir_lista()
    elif (opcion=="4"):
        gestor.pedir_peliculas_por_año()
    elif (opcion=="5"):
        gestor.presentar_pelicula_ingresada()
    elif (opcion=="6"):
        gestor.cambio_de_genero()
    elif (opcion=="7"):
        gestor.modificar_puntaje()
    elif (opcion=="8"):
        break
    else: 
        print("ninguna opcion correcta")