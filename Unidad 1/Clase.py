"""

El programa debe:

- Pedir por teclado el dinero actual de una persona
- Pedir por teclado el precio del insumo que quiere comprar en USD
- Convertir ese dinero a dolares (1 USD -> 170$)
- Devolver true o false si se pude comprar o no

- No deben aparecer errores

"""
try:    
    dato1= int(input("Ingresar un entero:"))
    dato2= int(input("Ingresar otro entero:"))
    suma= (dato1+dato2)
    print("La suma es: ",suma)
except:
    print("Ingresaste datos erroneos")





try:
    dato_1 = str(input("Ingresar su nombre:"))
    dato_2 = str(input("Ingresar su apellido:"))
    dato_3 = int(input("Ingrese su edad:"))
    dato_4 = float(input("Ingrese su numero de calzado:"))
    print(f"Sus dato son los siguientes:/nNombre:{dato_1}/nApellido:{dato_2}/nEdad:{dato_3}/nNumero de calzado:{dato_4}")
except:
    print("El valor ingresado es incorrecto")




try:
    numero = int(input("Por favor ingrese el numero: "))
    if numero < 0:  
        print("Pedi un numero positivo")
    else:
        print(f"El numero positivo que ingreso es: {numero}") 
except:
    print("No ingreso un numero entero.")

"""
El programa debe:

pedir al usuario que ingrese la cant de dinero que dispone.
verificar que la cantidad ingresada sea un numero y sino mostrar error
verificar la cantidad de ingresada e indicar que auto o autos puede comprar

"""
Ford = 10000
Renault = 11000
Chevrolet = 15000


try:
    dinero_disponible = float(input("Ingrese a continuación el dinero que dispone: "))
    if dinero_disponible >= 10000:
        print("Udsted puede comprarse un Ford")
    elif dinero_disponible >= 11000:
        print("Udsted puede comrparse un Renault")
    elif (dinero_disponible >= 15000):
        print("Udsted puede comprarse una Chevrolet")
except:
    print("No ingreso un numero.")



try: 
    color1= str(input("Ingrese el primer color: "))
    if color1=="rojo":
        color12= str(input("Ingrese el segundo color: ")
        if color12=="azul"
            print("Morado.")
        elif
            print("Amarillo.")
        else:
            pass
    elif:
        color13= str(input("Ingrese el segudo color: "))
        if color13=="verde":
            print("Cyan.")
        elif:
            print("Morado.")
except:
    print("Ingreso un dato incorrecto.")




n = 1
while n <= 10
    print(n)
    n+1=1
    














    
    