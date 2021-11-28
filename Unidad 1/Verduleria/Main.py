from Funciones import agregar_al_stock, consultar_stock, eliminar_del_stock

"""

Crear un prgrama que debe:
*    Contar con un stock de frutas y otro de verduras (El stock indica si venden o no esa fruta o verdura, no la cantidad) - dos listas que inician vacias
*    Contar con un menu y 3 funciones

      1. Agregar frutas o verduras al correspondiente stock (verificando que que sean nuevas)
      2. Consultar el stock de frutas o verduras
      3. Eliminar un elemento del stock 

"""

while True:                                  #Este es el menu donde pido que ingrese una condicion para saber que desea hacer el usuario
    condicion = input(""" 
    Bienvenido a verdulerias Nefastopolis, a continuacion ingrese lo que desee hacer:
    1. Agregar frutas o verduras
    2. Consutar el stock de frutas o verduras
    3. Eliminar una verdura o fruta del stock
    """)

    if condicion == "1":
        agregar_al_stock()
    elif condicion == "2":
        consultar_stock()        
    elif condicion == "3":
        eliminar_del_stock()
    else:
        print("Opcion ingresada incorrectamente.")












     
    




































