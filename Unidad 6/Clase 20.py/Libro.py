"""
*   Contar con una Clase Libro con los atributos (Id(unico), Nombre, Autor y estado (alquilado o no))
*   Contar con dos Clases Hijas que use el constructor de la clase padre pero que tenga un atributo mas:
        - LibroNiños (Atributo: edad_minima (por defecto = 11))
        - LibroIdiomas (Atributo: idioma_libro)
*   Se deben crear 4 metodos para la clase padre Libro (que heredaran las clases hijas):
        1. Presentarse: Que indique el Nombre, autor, año del libro y su estado 
        2. Indicar tipo de libro (tipo de clases heredadas o padre)
        3. Alquilar (Cambiaran el estado del libro a ALQUILADO)
        4. devolver_alquiler (Cambiaran el estado del libro a No alquilado)
"""


class Libro:
    #constructor
    def __init__(self,id,nombre,autor,estado):
        self.id = id #unico
        self.nombre = nombre
        self.autor = autor
        self.estado = estado

    def presentarse(self):
        print(f"Soy un libro, mi nombre es {self.nombre}, mi autor es {self.autor}, fui escrito en el año {self.año} y estado {self.estado}")

    def tipo_de_libro(self):
        print("Soy un libro tipo", type(self).__name__)

    def alquiler(self, nuevo_estado):
        self.estado = nuevo_estado
        print("El libro se alquilo de manera correcta.")

    def devolver_alquiler(self, estado_nuevo):
        self.estado = estado_nuevo
        print("El libro se devolvio de manera correcta.")


class LibroNiños(Libro):

    def __init__(self,id,nombre,autor,estado,edad_minima = 11): #Atributo extra de edad minima (11 por defecto)
        super().__init__(id,nombre,autor,estado)
        self.edad_minima = edad_minima


class LibroIdiomas(Libro):

    def __init__(self,id,nombre,autor,estado,idioma_libro): #Atributo extra de idioma
        super().__init__(id,nombre,autor,estado)
        self.idioma_libro = idioma_libro





