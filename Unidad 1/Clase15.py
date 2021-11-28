"""
Crear una funcion que debe: (usar diccionario)

Guardar en un diccionario los precios de las frutas de la tabla.
Preguntar al usuario por una fruta, un número de kilos y mostrar por pantalla el precio de ese número de kilos de fruta.
Si la fruta no está en el diccionario debe mostrar un mensaje informando ERROR.
"""

frutas = {
    "Manzana": 50,
    "Banana" : 40,
    "Mandarina": 30
    }

def frutas_():
    fruta_ingresada = input("Ingrese a continuacion una fruta: ")
    if fruta_ingresada in frutas:
        while True:
            try:            
                kilos_ingresados = float(input("Ingrese el numero de kilos: "))
                valor = frutas.get(fruta_ingresada, "no existe")
                print(f"El valor es de {valor*kilos_ingresados}")
            except:
                print("Ingrese solo numeros.")


frutas_()

diccionario_frutas={    
    "Pera": 110,
    "Manzana": 90,
    "Naranja": 80
}

def venta_de_fruta():
    fruta=input("Ingrese la fruta que desea: ").capitalize()
    if fruta in diccionario_frutas:
        while True:
            try:
                cantidad=float(input("Ingrese la cantidad de kilos: "))
                precio=(diccionario_frutas.get(fruta))*cantidad
                print(f"Por {cantidad}Kg. de {fruta} debe pagar: {precio}")
                return
            except:
       
                print("Cantidad Erronea.")
    else:
        print("La fruta no existe")

