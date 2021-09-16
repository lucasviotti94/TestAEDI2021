"""
El programa debe :
*    Pedir al usuario un string
*    Determinar si una cadena esta en minusculas o mayusculas
"""


try:
    string_pedido = str(input("Ingrese por favor una palabra: "))
    if string_pedido.islower():
        print("La palabra esta en minusculas..")
    else:
        print("La palabra esta en mayusculas..")
except:
    print("Ingresaste datos erroneos.")

"""""
El programa debe :
*   Almacenar una variable `contraseña` con una contraseña
*   Preguntar al usuario por la contraseña e imprimir por pantalla si la contraseña introducida por el usuario
coincide o no con la variable
*IMPORTANTE**: sin tener en cuenta mayúsculas y minúsculas.(metodos string)
*   no debe generar errores
"""""

contra = "messi"
try:
    contraseña_ingresada = str(input("ingrese la contraseña: "))
    if contraseña_ingresada.lower() == contra:
        print("Las contraseñas coinciden")
    else:
        print("No coinciden.")
except:
    print("Datos erroneos ingresados.")



















