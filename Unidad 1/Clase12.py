
"""

Crear una funcion que debe:
Tener almacenado el abcedario en una lista
Pedir al usuario un numero (2 o 3) - VERIFICAR que el num ingresado sea 2 o 3
Elimina de la lista las letras que ocupen posiciones múltiplos de ese numero
Mostrar por pantalla la lista resultante.
No deben aparecer y se deben tener en cuenta todos los posibles errores

"""

def eliminar_multiplos():
    abecedario_original = "abcdefghijklmnñopqsrtuvwxyz"
    abecedario_lista = list(abecedario_original)

    while True:        
            numero_ingresado = input("Ingrese a continuacion un numero (2 o 3): ")
            if numero_ingresado == "2" or numero_ingresado == "3":
                break
    
    if numero_ingresado == "2":
        for i in range(int(numero_ingresado),len(abecedario_original),int(numero_ingresado)):
            print(abecedario_lista[i-1])
    else:
        for i in range(int(numero_ingresado),len(abecedario_original),int(numero_ingresado)):
            print(abecedario_lista[i-1])    





eliminar_multiplos()











def pedir_numero():
    while True:
        try:
            numero_ingresado = int(input("Ingrese a continuacion el numero 2 o el numero 3: "))
            if numero_ingresado == 2 or numero_ingresado == 3:
                return numero_ingresado                    
        except:
            print("Dato incorrecto.")














