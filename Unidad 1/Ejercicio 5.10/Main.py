from Funciones import mostrar_alfabeto_a, mostrar_alfabeto_b, modificar_letra, conversion_a_to_b
"""
##**Ejercicio 5.10 (Conversión de alfabeto)**
El programa debe:
*   Simular la conversion de un alfabeto a otro: Por ejemplo el moorse 
    (NO ES ESTRICTAMENTE NECESARIO USAR ESTE ALFABETO, PUEDE SER INVENTADO)
```
 alfabeto_a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
 alfabeto_b = ['.-' ,'-...' , '-.-.' ,'-..' ,'.', '..-.','--.', '....','..' ,'.---' , '-.-', '.-..','--' ,'-.' ,'---' ,'.--.','--.-' , '.-.' ,'...' ,'-','..-' ,'...-','.--','-..-' , '-.--' , '--..' ]
```

*   Contar con 6 funciones disponibles en el menu:
    1. Mostrar el alfabeto A
    2. Mostrar el alfabeto B
    3. Modificar una letra del Alfabeto A y el alfabeto B (debe ser la misma)
    4. Conversion de alfabeto A a alfabeto B: ejemplo **abc --> .--...-.-.**
    5. Conversion de alfabeto B a alfabeto A: ejemplo **.--...-.-. --> abc**
    6. Verificacion de existencia de una letra del alfabeto (debe seleccionar A o B)

*   Gestionar posibles errores
*   Estructurar el programa a criterio propio
    """


while True:                                  #Este es el menu donde pido que ingrese una condicion para saber que desea hacer el usuario
    condicion = input(""" 
    Bienvenido al Conervsor, a continuacion ingrese lo que desee hacer:
    1. Mostrar el alfabeto A
    2. Mostrar el alfabeto B
    3. Modificar una letra del Alfabeto A y el alfabeto B (debe ser la misma)
    4. Conversion de alfabeto A a alfabeto B: ejemplo **abc --> .--...-.-.**
    5. Conversion de alfabeto B a alfabeto A: ejemplo **.--...-.-. --> abc**
    6. Verificacion de existencia de una letra del alfabeto (debe seleccionar A o B)
    """)

    if condicion == "1":
        mostrar_alfabeto_a()
    elif condicion == "2":
        mostrar_alfabeto_b()        
    elif condicion == "3":
        modificar_letra()   
    elif condicion == "4":
        conversion_a_to_b()      
    elif condicion == "5":
        pass
    else:
        print("Opcion ingresada incorrectamente.")














