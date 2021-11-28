"""
##**Ejercicio 5.15 (Base de peliculas)**
El programa debe:
*   Simular una base de datos de peliculas y series con la capacidad de agregar, buscar, eliminar y filtrar peliculas y series.
*   Debe comenzar con las siguientes peliculas y series en un diccionario:

```
base = {
    "peliculas" : ["El hombre araña", "Los vengadores" , "Los vengadores 2"],
    "series" : ["prision break", "la casa de papel" , "los simpsons"]
        }
```

*   Contar con 5 funciones disponibles en el menu:
    1. Mostrar por pantalla en formato vertical la lista de peliculas o series disponibles.
    2. Agregar nuevas peliculas o series (que no esten) en la base.
    3. Eliminar peliculas o series de la base.
    4. Mostrar segun requiera el usuario la lista de peliculas desde un punto a otro (ej el usuario quiere 
    ver de la 2° a la 4° una lista ).
    lista = [1,2,3,4]
    print(lista[])
    5. Buscar peliculas o series que contengan una palabra requerida por el usuario. (ej. input("el"), 
        se liste las peliculas que contengan la palabra "el").
"""
import funciones515 as fn
while True:
    opcion=input(
    """
-----------Menu principal-----------
Por favor ingrese una opcion:
    1. Mostrar bases
    2. Agregar series o peliculas
    3. Elimnar series o peliculas
    4. Mostrar de a a b
    5. Busqueda por palabra
    Opcion: """
    )
    if (opcion=="1"):
        fn.mostrar_bases() 
    elif (opcion=="2"):
        fn.agregar_peliculas_series()
    elif (opcion=="3"):
        fn.eliminar_peliculas_series()
    elif (opcion=="4"):
        fn.mostrar_de_A_B()
    elif (opcion=="5"):
        fn.busqueda_palabra()
    else:
        print("ninguna opcion correcta")




"""
Set
"""
conjunto_1 = set([1,2,3,4,4,2,5])               ##Imprime solo 1, 2 ,3 4, 5 ya que no repite elementos
for i in conjunto_1:
  print (i)
conjunto_1.remove(1)
print(conjunto_1)
print(type(conjunto_1))


"""
Crear una funcion que debe: (usar set)

Pedir al usuario determinados paises y guardarlos en un set
Cuando el usuario escriba "listo", se debe imprimir todos los paises sin repetir, y la cantidad total sin repetir
"""


paises= set([]) #conjunto vacio
while True:
  pais = input("ingrese un pais o 'listo' para terminar: ").capitalize()
  if pais == "Listo":
    break
  paises.add(pais)

for i in paises:
  print (i)
print(f"En total se cargaron {len(paises)} diferentes")
print(type(paises))



"""
Programacion orientada a Objetos

"""

## Clase con un constructor

class Lapiz:
    # El método __init__ es llamado al crear el objeto
    def __init__(self, color, longitud):
        print(f"Creando un lapiz de color {color}, que mide {longitud} cm")
        # Atributos de instancia
        self.color = color
        self.longitud = longitud

lapiz_1 = Lapiz("rojo",25)
print(type(lapiz_1))
#acceder a los atributos
print(lapiz_1.color)





