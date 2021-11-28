"""
Ejercicio MONEDAS
Crear una funcion que debe: (usar diccionario)
Contener un diccionario con distintas monedas de paises, siendo:
La key el nombre de la moneda y el valor el simbolo.
Preguntar al usuario que tipo de moneda desea y mostrar el simbolo si existe en el diccionario, caso contrario indicar que no existe.
"""
monedas = {
    "Peso":"$", 
    "Dolar": "USD",
    "Euro":  "€"
    }
## De esta manera veniamos haciendola
def obtener_simbolo():
    moneda = input("Ingrese que tipo de moneda desea saber el simbolo: ").capitalize()
    print(moneda)
    if moneda in Monedas:
        print(f"El simbolo de {moneda} es {Monedas[moneda]}")
    else:
        print("La moneda ingresada no exite en el diccionario.")

## Esta es una manera nueva utilizando.get que se utiliza como if y else todo junto
def obtener_simbolo_2():
    moneda = input("Ingrese que tipo de moneda desea saber el simbolo: ").capitalize()
    valor = Monedas.get(moneda, "No existe")
    print(f"El simbolo de {moneda} es {valor}")


obtener_simbolo_2()


# Iterar key y valor juntos
print(diccionario_persona.items())

for i, j in diccionario_persona.items():
    print(f"Key: {i} - Valor: {j}")

# De esta manera cambiamos el valor ded una key con .update

diccionario_persona = {
    "Nombre": "juan",
    "Edad": 30,
    "DNI": [1,2,3,4,5],
}
print(diccionario_persona)
diccionario_persona.update({"Nombre":"Federico"})
print(diccionario_persona)

"""
Ejercicio FRUTA
Crear una funcion que debe: (usar diccionario)
*   Guardar en un diccionario los precios de las frutas de la tabla.
*   Preguntar al usuario por una fruta, un número de kilos y mostrar por pantalla el precio de ese número de kilos de fruta. 
*   Si la fruta no está en el diccionario debe mostrar un mensaje informando ERROR.

| Fruta | Precio|
|:-|:-:|
|banana | 50 |
|manzana | 80|
|pera| 100|
|naranja | 30|

"""
stock_frutas = {
    "banana" : 50,
    "manzana" : 80,
    "pera" : 100,
    "naranja" : 30
}
def precio_final(stock_frutas):
    fruta = input("Ingrese la fruta a comprar: ").casefold()
    valor = stock_frutas.get(fruta,'La fruta no está en el stock')
    while True:
        if valor == "La fruta no está en el stock":
            print(valor)
            break
        else: 
            try:
                kilos = int(input("Ingrese la cantidad de Kilos a comprar: "))
                precio = valor*kilos
                print(f"{kilos} kilos de {fruta} es: {precio}")
                break1
            except:
                print("Reintentar, valor erroneo.")

precio_final(stock_frutas)


"""

Ejercicio PERSONAS
Crear una funcion que debe: (usar diccionario)
*    Crear un diccionario vacío y lo vaya llenado con información sobre una persona (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.)
*    Pida al usuario el dato a agregar (key) y el valor
*    Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario.

"""

personas={ }

def agregar_informacion():
  while True:
    key = input("Ingrese la informacion que registrara o salir (para abandonar el programa): ")
    if key =="salir":
      break
    if key in personas:
      print("Ya existe el valor, ingrese uno diferente!!")
    else:
      valor = input(f"Por favor ingrese el valor de {key}: ")
      personas.setdefault(key,valor)
      print(personas)

def imprimir_diccionario(nombre,diccionario):
  print(f"--------{nombre}--------")
  print(f"--key\tValor--")
  for i in diccionario:
    print(f"  {i}\t{diccionario.get(i)}")

def imprimir_diccionario2(nombre,diccionario):
  print(f"--------{nombre}--------")
  print(f"--key\tValor--")
  for i,j in diccionario.items(): #i trae los key (tupla) j trae los valores (tupla)
    print(f"  {i}\t{j}")


agregar_informacion()
#imprimir_diccionario("Datos de la persona",personas)
imprimir_diccionario2("Datos de la persona",personas)


