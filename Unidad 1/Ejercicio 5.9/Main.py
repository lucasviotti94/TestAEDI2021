from Funciones import posibles_choferes, modificar_nombre_chofer, modificar_recorrido, agregar_nuevo_coche, taxis_disponibles, informacion_chofer
'''
##**Ejercicio 5.9 (Empresa de Taxis)**
El programa debe:
*   Simular una empresa de taxis que cuente con tres Autos con sus respectivos cheferes
```
Taxis=[["auto_1","auto_2","auto_3"],["chofer_1","chofer_2","chofer_3"],[45,50,30]]
```
    *  Cada auto cuenta con un chofer y no hace recorridos mayores a lo q se le indica
*   Contar con 6 funciones disponibles en el menu:
    1. Preguntar al usuario el recorrido del viaje e indicar posibles autos y choferes
    2. Modificar nombre chofer segun el nombre del auto.
        auto_1 -> "federico"
    3. Modificar el recorrido segun el nombre del auto.
        auto_1 -> 60
    4. Agregar nuevo auto a la empresa de Taxis, indicando auto, nombre chofer y recorrido maximo -> ULTIMO
    5. Observar una lista de autos choferes y recorrido maximo con el siguiente formato:
    6. Observar informacion de un chofer, verificando su existencia previamente

```
AUTO    -    CHOFER    -   RECORRIDO
auto_1  -   chofer_1   -   45
auto_2  -   chofer_1   -   50
```
    
*   Gestionar posibles errores
*   Estructurar el programa a criterio propio
'''


while True:                                  #Este es el menu donde pido que ingrese una condicion para saber que desea hacer el usuario
    condicion = input(""" 
    Bienvenido a Taxilandia, a continuacion ingrese lo que desee hacer:
    1. Preguntar recorrido y choferes posibles.
    2. Modificar nombre chofer segun el nombre del auto.
    3. Modificar el recorrido segun el nombre del auto.
    4. Agregar nuevo auto a la empresa.
    5. Observar una lista de autos choferes y recorrido maximo.
    6. Observar informacion de un chofer, verificando su existencia previamente.
    7. Salir.
    """)

    if condicion == "1":
        posibles_choferes()
    elif condicion == "2":
        modificar_nombre_chofer()        
    elif condicion == "3":
        modificar_recorrido()
    elif condicion == "4":
        agregar_nuevo_coche()  
    elif condicion == "5":
        taxis_disponibles()  
    elif condicion == "6":
        informacion_chofer()
    elif condicion == "7":
        break      
    else:
        print("Opcion ingresada incorrectamente.")












