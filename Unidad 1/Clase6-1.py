"""Actividad cuenta regresiva"""

cond = True
while cond:
    try:
        numeroIngresado = int(input("Ingrese a continuacion un numero entero positivo: "))
        if numeroIngresado <= 0:
            continue
        else:
            for i in range(numeroIngresado,-1,-1):
                print(i,end=", ")
                cond = False
    except:
        print("Dato ingresado incorrecto, por favor intente nuevamente.")














        





























