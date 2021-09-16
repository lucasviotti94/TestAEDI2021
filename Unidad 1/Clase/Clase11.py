# def palindromos():
    lista = [ ]
    try:            
        palabra_o_frase = str(input("Ingrese una palabra o frase: "))
        if palabra_o_frase == palabra_o_frase.reverse() 
    except:
        print("Error.")


def materias():
    lista = [ ]
    for i in range(5):
        materia = input("Ingrese la materia")
        palabra_o_frase(materia)
        if palabra_o_frase == True:
            if materia.isalpha():
                for i in materia:
                    if i != " ":
                        print("Esto es una frase") 
                    break                    
            else:
                print("error")                   

    lista.sort()
    return lista

materias()
def palabra_o_frase(a):
    for i in a:
        if i == " ":
            False            
        else:
            True



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






        









