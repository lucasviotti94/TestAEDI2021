alfabeto_a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alfabeto_b = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']



def mostrar_alfabeto_a():
    global alfabeto_a
    print(alfabeto_a)

def mostrar_alfabeto_b():
    global alfabeto_b
    print(alfabeto_b)

def modificar_letra():
        global alfabeto_a
        global alfabeto_b       
        while True:
            try:
                letra_a_modificar = str(input("Ingrese la letra que desea modificar: "))
                if letra_a_modificar in alfabeto_a:
                    posicion0 = alfabeto_a.index(letra_a_modificar)
                    nueva_letra0 = input("Ingrese la nueva letra: ")
                    if nueva_letra0.islower() and nueva_letra0.isalpha():
                        alfabeto_a [posicion0] = nueva_letra0
                        alfabeto_b [posicion0] = nueva_letra0
                        return print("Cambio la letra de manera correcta.")
                    else:
                        print("Tienes que ingresar una letra minuscula.")                    
                elif letra_a_modificar in alfabeto_b:                     
                    posicion1 = alfabeto_b.index(letra_a_modificar)
                    nueva_letra1 = input("Ingrese la nueva letra: ")
                    if nueva_letra1.isupper() and nueva_letra1.isalpha():
                        alfabeto_a [posicion1] = nueva_letra1
                        alfabeto_b [posicion1] = nueva_letra1
                        return print("Cambio la letra de manera correcta.")
                    else:
                        print("Tienes que ingresar una letra Mayuscula.")
                else:
                    print("Esa letra no existe en ninguno de los alfabetos.")                
            except:
                print("Error.")
              
def conversion_a_to_b():
    while True:
        global alfabeto_a   
        global alfabeto_b        
        conversion_hecha = [ ]
        try:
            cantidad = int(input("Ingrese la cantidad de letras que desea convertir."))
            if cantidad > 0:
                for i in range(0,cantidad,1):                    
                    letra = input(f"Ingrese la {i} letra que desea convertir.")
                    if letra.isalpha() and letra != " ":            
                        posicion_0 = alfabeto_a.index(letra)
                        conversion_hecha.append(alfabeto_b [posicion_0])
                print(conversion_hecha)
        except:
            print("Esto no es un numero.")
        break
        



            


        


















