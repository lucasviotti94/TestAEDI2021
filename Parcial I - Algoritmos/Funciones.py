alumnos = [["Lucas", "Micaela", "Juan", "Alejandro"], [15, 17, 12, 18], ["lucas@gmail.com", "micaela@gmail.com", "juan@gmail.com", "alejandro@gmail.com"]]
materias = ["Matematicas", "Lengua", "Geografia", "Programacion", "Historia"]

def consultar_lista():
    global alumnos
    print(f"""
    -Nombre de usuario-   -Edad-   -Email-
    """)
    for i in range(0,len(alumnos)+1,1): 
        print(f" {alumnos[0][i]}               {alumnos[1][i]}         {alumnos[2][i]}")

def agregar_alumno():
    global alumnos    
    while True:        
        usuario_nuevo = input("Ingrese el nombre de usuario del alumno que desea agregar: ")        
        if usuario_nuevo not in alumnos [0]:
            alumnos[0].append(usuario_nuevo)
            print("Se agrego el nombre de manera correcta.")
            break
        else:
            print("Ya existe ese nombre de usuario. Intente nuevamente...")
    while True:
        edad_nueva = input("Ingrese a continuacion la edad del alumno nuevo: ")
        if edad_nueva.isdigit():
            if int(edad_nueva) > 9 and int(edad_nueva) < 19:
                alumnos[1].append(edad_nueva)
                print("Se agrego la edad de manera correcta.")  
                break                        
            else:
                print("Ingrese edad entre 10 - 18 años.")
        else:
            print("Ingrese solo numeros.")
    while True:
        mail_nuevo = input("Ingrese a continuacion el mail del alumno.")                    
        if "@" in mail_nuevo:
            alumnos[2].append(mail_nuevo)                        
            print("Se agregaron los datos de manera correcta.")
            break
        else:
            print("Le falta agregar @.")
    print(alumnos) 

def editar_edad():
    while True:
        global alumnos 
        nombre_pedido = input("Ingrese a continuacion el nombre de usuario del alumno a editar: ")
        if nombre_pedido in alumnos [0]:
            edad_nueva = input("Ingrese la edad nueva del alumno a editar: ")
            if edad_nueva.isdigit():
                if int(edad_nueva) >= 10 and int(edad_nueva) <= 18:
                    posicion = alumnos[0].index(nombre_pedido)                          #Aqui descrubro la posicion del alumno a editar
                    alumnos[1][posicion] = edad_nueva
                    break                    
        else:
            print("Este nombre de usuario no existe en nuestro sistema. Intente nuevamente")

def consultar_materias():
    global materias
    print(f"""

        -Materias-

    """)
    for i in materias: 
        print(f" {i}")  

def agregar_materias():
    while True:
        materia_nueva = input("Ingrese a continuacion la materia que desee agregar al sistema: ")
        if materia_nueva not in materias:
            materias.append(materia_nueva)
            print(f"Se agrego {materia_nueva} de manera correcta al sistema.")
            break
        else:
            print("Esta materia ya existe en nuestro sistema, intente nuevamente...")









