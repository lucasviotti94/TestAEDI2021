"""
El programa debe:
*   mostrar el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará."""
""""""

while True:
    try: 
        i=input("Introduzca algo.")
        if i == "salir":
            print("Nos vimo en disney")
            break
        else:
            print(i)
    except:
        print("Error.")


"""""

El programa debe:
*   mostrar el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.
*  si el usuario escribe "hola" o "chau" que no se haga el eco 

"""

while True:
    try: 
        i=input("Introduzca algo.")
        if i == "salir":
            print("Nos vimo en disney")
            break
        elif i=="hola" or "chau":
            continue
        else:
            print(i)
    except:
        print("Error.")






























