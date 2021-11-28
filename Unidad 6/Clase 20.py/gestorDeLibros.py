"""
    Se debe crear una clase GestorBiblioteca que cuente con las siguientes funciones para un menu:

    1.  Crear instancias de libros y guardalos en una lista de libros. 
        1.1) Se debe verificar que tipo de instancia de libro crear y los parametros
             - Id debe ser unico, se comienza del 1
             - Nombre y autor no es necesario
             - estado debe comenzar "No alquilado"
        1.2) Al crear un libro es necesario logearlo (Escribir en una linea nueva: id-nombre-autor) 
             en un archivo llamado libros.txt (Crear funcion en el mismo gestor)
        1.3) En caso que la instancia del libro sea LibroIdiomas.
             - El usuario  debe elegir a travez de una clave (mostradas por el programa) desde un diccionario de idiomas.
             - En caso que no exista el idioma deseado debe ser en idioma "español" (AYUDA: Funcion get de diccionarios)
    2.   Listar libros disponibles (recorrer la lista, no el archivo)
    3.   Cambiar el estado (Alquilar o devolver) de un libro, seleccionando su id. (Hacer check correspondientes)
"""

import Libro as lb
lista_libros = [] #empieza vacia
idiomas = {
"IN":"ingles", 
"AL": "aleman",
"CH":  "chino"
}

class gestorDeLibros:
    def __init__(self):
        pass

    def crear_libro(self):
        while True:
            tipo_instancia = input(
"""Ingrese a continuacion que tipo de libro desea crear: 
1 - LibroNiños
2 - LibroIdiomas
""")
            if tipo_instancia == "1" or tipo_instancia == "2":
                break
            else:
                print("Opcion incorrecta...")
        #ID
        while True:
            try:
                id_nuevo = int(input("Ingrese a continuacion el id del libro nuevo: ")) 
                for libros in lista_libros:
                    if id_nuevo != libros.id:
                        print(f"ID ingresado de manera correcta: {id_nuevo}")
                        break
                    else:
                        print("Este id ya existe, intente nuevamente..")    
                break            
            except:
                print("Ingrese por favor solo numeros enteros, empezando por el 1 en adelante.")
        #Nombre
        while True:
            nombre_nuevo = input("Ingrese a continuacion el nombre del libro nuevo: ")
            for libros in lista_libros:
                if nombre_nuevo == libros.nombre:
                    print("Este nombre ya existe, por fvor ingrese otro nombre..")
                else:
                    print(f"El nombre del libro nuevo se agrego de manera correcta: {nombre_nuevo}")
                    break
            break            
        #Autor
        while True:            
            autor_nuevo = input("Ingrese a continuacion el autor del libro nuevo, si lo conoce: ")
            print(f"El autor del libro nuevo se agrego de manera correcta: {autor_nuevo}")
            break
        #Estado
        estado_por_defecto  = "No alquilado"    
        #Instancia Libro Idioma
        if tipo_instancia == "1":
            nombre_instancia = lb.LibroNiños(id_nuevo, nombre_nuevo, autor_nuevo, estado_por_defecto)
        else:
            while True:
                opcion_idioma = input(
"""Ingrese a continuacion la opcion deseada: 
1- Elegir uno de los siguientes idiomas para el libro nuevo: Ingles, Aleman, Chino.
2- No elegir ninguno de estos idiomas.
""")
                if opcion_idioma == "1":
                    for i, j in idiomas.items():
                        print(f"Clave: {i} - Idioma: {j}")  #Muestro los posibles idiomas
                    clave_elegida = input("Ingrese a continuacion la clave del idioma del nuevo libro:")
                    for i in idiomas:
                        if clave_elegida == i:
                            idioma_libro_nuevo = idiomas.get(clave_elegida)
                            nombre_instancia = lb.LibroIdiomas(id_nuevo, nombre_nuevo, autor_nuevo, estado_por_defecto, idioma_libro_nuevo)
                            break
                elif opcion_idioma == "2":
                    idioma_libro_nuevo = "español"
                    break                                
                else:
                    print("Opcion incorrecta, intente nuevamente")


        
    def lista_libros_disponbles(self):
        while True:
            print(
    """ --------- Libros Disponibles --------- """)
            for libros in lista_libros:
                if libros.estado == "No alquilado":
                    print(libros.nombre)

    def cambiar_estado_libro(self):
        while True:
            opcion_1 = input(
"""Ingrese a continuacion que desea realizar: 
1 - Alquilar
2 - Devolver
""")
            if (opcion_1 == "1"):
                id_libro_elegido = input("Ingrese a continuacion el id del libro a alquilar: ")                
                for libros in lista_libros:
                    if (id_libro_elegido == libros.id):
                        nuevo_estado = "Alquilado"
                        libros.alquiler(nuevo_estado)
                        break
                    else:
                        print("No existe ningun libro con ese ID en nuestro sistema.")
            elif (opcion_1 == "2"):
                id_libro_elegido = input("Ingrese a continuacion el id del libro a devolver: ")                
                for libros in lista_libros:
                    if id_libro_elegido == libros.id:
                        nuevo_estado = "No alquilado"
                        libros.devolver_alquiler(nuevo_estado)
                        break
                    else:
                        print("No existe ningun libro con ese ID en nuestro sistema.")
            else:
                print("Opcion incorrecta...")

    def logeador_libros(self,datos): #Funcion para CREAR un .txt y almacenar la info
            try:
                with open(path+ f"\libros.txt","a+") as fichero: 
                    for i in datos:
                        fichero.write(i+" - ")
                    fichero.write("\n")

            except:
                print("Error")


            


                    
                    



















