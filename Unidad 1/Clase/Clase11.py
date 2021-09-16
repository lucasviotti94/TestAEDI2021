# Funcion para saber si una palabra es capicua
def es_palindromo():
  palabra_original = input("Ingrese una palabra: ")
  if not palabra_original.isalpha():
    print("la palabra no es correcta")
  else:
    palabra_original_lista = list(palabra_original)
    palabra_reversa = palabra_original_lista.copy()
    palabra_reversa.reverse()
    if palabra_original_lista == palabra_reversa:
      print("OK! es una palabra capicua")
    else:
      print("ERROR! No es una palabra capicua")

es_palindromo()


# Funcion para ordenar materias
def ordenamiento_de_palabras():
    lista_materias=[]
    for i in range(5):
        while True:
            materia = input(f"Ingrese la materia numero {i+1}: ")
            if materia.isalpha():
                lista_materias.append(materia)
                break
            else:
                print("Reintentar, valor erroneo.")
    lista_materias.sort()
    print(lista_materias)

ordenamiento_de_palabras()

# Pequeña funcion para saber si una variable string es palabra o frase
materias()
def palabra_o_frase(a):
    for i in a:
        if i == " ":
            True            
        else:
            False



def viajes():
    lista = [ ]
    acumulador_duracion = 0
    try:
        tramos = int(input("Ingresar la cantidad de tramos: "))
    except:
        print("Error.")
    for i in range(tramos):
        duracion_tramo = input(f"Ingrese la duracion del {i} tramo, en minutos.")
        if duracion_tramo.isdigit():
            duracion_tramo.append(lista)
            acumulador_duracion += duracion_tramo
    print(f"El tiempo total del viaje es de {acumulador_duracion}")          






        









