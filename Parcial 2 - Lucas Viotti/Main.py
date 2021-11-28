'''
************************************************************
 MATERIA: Algoritmos y Estructuras de Datos 1
 EXAMEN: Recuperatorio 2° Examen
 APELLIDO Y NOMBRE: Viotti Lucas
 DNI: 37575660
 CARRERA: Analista de Sistemas
 AÑO: 2021 
 Se envía mail con asunto: "[AYEDI 2021 - Apellido, Nombre - 2°Examen Recuperatorio]" COMPRMIIR EN CARPETA [Apellido,Nombre 2_examen_rec]
 ************************************************************
 Ítems a evaluar:
 1. Contenidos de la materia
 2. Requerimientos y comprensión de consignas
 3. Estructura (modularización), legibilidad y comentarios del código.

¡Cualquier duda con el enunciado consultar al docente!
************************************************************
ENUNCIADO: "Programa de gestion de hoteles"

Introducción: 
    El siguiente programa consiste en un software que simule una programa para gestionar las habitatociones de un hotel.
    El programa debe permitir agregar y quitar habitaciones al sistema, como también gestionar datos del estas (numero, max_personas, precio).

Requerimientos:
El programa debe:
*   Contar con una Clase Habitacion con los atributos (numero (único), max_pesonas (int), precio (float))
*   Contar con dos Clases Hijas que use el constructor de la clase padre pero que tenga un atributo más:
        - HabitacionClasica (Atributo: cant_televisores (int))
        - HabitacionPremium (Atributo: Jacuzzi "True o False" (por defecto = True))
        
*   Se deben crear los siguientes métodos para la clase padre Evento (que heredaran las clases hijas):
        1. Mostrar información: Que indique el numero, max_personas y precio
           -  Este metodo debe ser creado en la clase padre y las hijas, ya que las clases hijas deben mostrar tambien sus atributos
        2. Setear y obtener max_personas
        3. Setear y obtener precio
        4. Obtener tipo de clase

*   Se debe crear una clase GestorHabitaciones que cuente con las siguientes funciones para un menu:

    1.  Crear instancias de una habitacion y guárdalos en una lista de habitaciones. 
        1.1) Se debe verificar que tipo de instancia de evento a crear y los parámetros. IMPORTANTE!: clase hijas verificar y pedir parámetros
             - numero: debe ser único
             - max_personas: verificar que sea un numero entero y este entre 2 y 6 inclusives.
             - precio: se debe pedir en pesos pero se debe guardar en dolares (1 dolar -> 200 pesos)
        1.2) Clases hijas:
             - cant_televisores: verificar que sea entero entre 0 y 3 incluses
             - Jacuzzi: verificar que sea True o False (boolean)
        1.3) Al crear una Habitacion es necesario logearlo (Escribir en una línea nueva: numero,max_personas,precio,tipo_de_clase)) 
             en un archivo llamado historial_habitaciones.csv (Crear función en el mismo gestor). IMPORTANTE!: verificar permisos y extension
    2.   Cambiar precio de habitacion, seleccionando su numero: Se debe cambiar el precio de la habitacion dependiendo de la cant max de 
         personas que contenga y el tipo de habitacion:
         - Se debe leer el diccionario por el tipo de habitacion y multiplicar ese precio por la cantidad de personas.
         Ej. Precio hab clasica = 400 (CL)* max_personas = 400 * 5 = 2000 IMPORANTE! solo se le pide el numero de habitacion al usuario
    3.   Pedir al 1usuario un numero y listar esa cantidad de habitaciones de la lista, verificando que hayan esa cantidad de habitaciones
    
*   Se deben crear los métodos correspondientes para las funciones del menú en las clases correspondientes
*   Gestionar posibles errores
*   Estructurar el programa a criterio propio
'''

import gestor as gs
import Clases as cl
gestor = gs.GestorHabitaciones()

while True:
    opcion = input(
    """
-----------Programa de Gestión de Habitaciones-----------
Por favor ingrese una opcion:
    1. Crear Habitacion.    
    2. Cambiar precio.
    3. Listar habitaciones.
    4. Salir
    Opcion: """
    )
    if (opcion=="1"):
        gestor.crear_habitacion()
    elif (opcion=="2"):
        gestor.cambiar_precio()
    elif (opcion=="3"):
        gestor.listar_habitaciones()
    elif (opcion=="4"):
        break
    else: 
        print("ninguna opcion correcta")
