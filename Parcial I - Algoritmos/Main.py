from Funciones import consultar_lista, agregar_alumno, editar_edad, consultar_materias, agregar_materias

'''
************************************************************
 MATERIA: Algoritmos y Estructuras de Datos 1
 EXAMEN: 1° Examen
 APELLIDO Y NOMBRE: VIOTTI LUCAS
 DNI: 37575660
 CARRERA: ANALISTA EN SISTEMAS
 AÑO: 2021 
 Se envia mail con asunto: "[AYEDI 2021 - Apellido, Nombre - 1°Examen]"
 ************************************************************
 Items a evaluar:
 1. Requerimientos y comprension de consignas
 2. Estructura (modularización), legibilidad y comentarios del codigo.

¡Cualquier duda con el enunciado consultar al docente!
************************************************************
ENUNCIADO: "Programa de Gestión de alumnos y Materias"

Introduccion: 
    El siguiente programa consiste en un software de gestion de alumnos y gestion de materias
    de una institucion educativa.
    El programa debe permitir agregar y quitar alumnos al sistema junto con su informacion personal: 
    Nombre, Edad y mail.
    El programa debe permitir agregar Materias al sistema.

Requerimientos:
El programa debe:
*   Contar con un menu donde permita al usuario elegir entre las siguientes funciones:
    1. Ver lista de alumnos (Formato: nombre_usuario - Edad - Mail)
    2. Permitir al usuario del programa agregar un nuevo alumno (Indicando: nombre_usuario - Edad - Mail)
       Verificando: Que el nombre_usuario no exista previamente, la edad entre 10 y 18 años y que el mail cuente con un @.
       (Ayuda: metodo in de list sirve tambien para strings)
    3. Editar la edad de un alumno verificando que este entre 10 y 18 años, se edita mediante el nombre.
    4. Ver lista de materias (Formato: Materias)
    5. Agregar materias al sistema (verificando que no exista previamente)
*   Gestionar posibles errores
*   Estructurar el programa a criterio propio
'''

while True:                                  
    condicion = input(""" 
    Bienvenido, a continuacion ingrese lo que desee hacer:
    1. Ver lista de alumnos.
    2. Agregar un nuevo alumno.
    3. Editar edad de alumno.
    4. Ver lista de materias.
    5. Agregar materias al sistema.
    6. Salir
    """)

    if condicion == "1":
        consultar_lista()
    elif condicion == "2":
        agregar_alumno()      
    elif condicion == "3":
        editar_edad()
    elif condicion == "4":
        consultar_materias()  
    elif condicion == "5":
        agregar_materias()  
    elif condicion == "6":
        break    
    else:
        print("Opcion ingresada incorrectamente. Intente nuevamente..")
















