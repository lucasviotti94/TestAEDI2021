
frutas_stock = [ ]
verduras_stock = [ ]

#Funciones para preguntar el stock
def consultar_stock():
    global frutas_stock
    global verduras_stock
    while True:
            eleccion = input(
            """Ingrese a continuacion que stock desea consultar: 
            1. Ingrese 1 para verificar el stock de Frutas.
            2. Ingrese 2 para verificar el stock de Verduras.
            """)
            if eleccion == "1":
                while True:
                    try:
                        fruta_ingresada = str(input("A continuacion ingrese el nombre de la fruta para conocer su stock actual: "))
                        if fruta_ingresada in frutas_stock:
                            return print(f"Si existe stock actual de {fruta_ingresada} en el sistema.")
                        else:
                            return print(f"No existe stock actual de {fruta_ingresada} en el sistema.")
                    except:
                        print("Datos incorrectos. Intente nuevamente: ")
            elif eleccion == "2":
                    while True:
                        try:
                            verdura_ingresada = str(input("A continuacion ingrese el nombre de la verdura para conocer su stock actual: "))
                            if verdura_ingresada in verduras_stock:
                                return print(f"Si existe stock actual de {verdura_ingresada} en el sistema.")
                            else:
                                return print(f"No existe stock actual de {verdura_ingresada} en el sistema.")
                        except:
                            print("Datos incorrectos. Intente nuevamente: ")
            else:
                print("Esta opcion es incorrecta, intente nuevamente.")
#Funciones para agregar elementos al stock
def agregar_al_stock():
    while True:        
        eleccion = input(
        """
        Ingrese a continuacion la opcion deseada: 
        1. Ingrese "1" para agregar frutas.
        2. Ingrese "2" para agregar verduras 
        """)
        if eleccion == "1":
            global frutas_stock
            while True:    
                fruta_ingresada = input("Ingrese el nombre de la fruta que desee agregar: ")
                if fruta_ingresada != " " and fruta_ingresada.isalpha(): 
                    if fruta_ingresada not in frutas_stock:
                        frutas_stock.append(fruta_ingresada)                                            
                        return print(f"Uds agrego exitosamente {fruta_ingresada} a la lista")                                              
                else:
                    print("Datos incorrectos. Intente nuevamente.")
        elif eleccion == "2":
            global verduras_stock
            while True:
                verdura_ingresada = input("Ingrese el nombre de la verdura que desee agregar: ")
                if verdura_ingresada != " " and verdura_ingresada.isalpha():
                    if verdura_ingresada not in verduras_stock:
                        verduras_stock.append(verdura_ingresada)
                        return print(f"Uds agrego exitosamente {verdura_ingresada} a la lista")                                              
                else:
                    print("Datos incorrectos ingresados. Intente nuevamente.")
        else:
            print("Opcion incorrecta, intente nuevamente.")
#Funciones para eliminar elementos del stock
def eliminar_del_stock():
    while True:        
        eleccion = input(
        """
        Ingrese a continuacion la opcion deseada: 
        1. Ingrese 1 para eliminar verduras.
        2. Ingrese 2 para eliminar frutas. 
        """)
        if eleccion == "1":
            global verduras_stock
            while True:
                verdura_a_eliminar = input("Ingrese el nombre de la verdura que desea eliminar: ")
                if verdura_a_eliminar != " " and verdura_a_eliminar.isalpha(): 
                    if verdura_a_eliminar in verduras_stock:
                        verduras_stock.remove(verdura_a_eliminar)                                  
                        return print(f"Uds elimino exitosamente {verdura_a_eliminar} del stock.")
                    else:
                        print(f"No hay stock de {verdura_a_eliminar} en nuestro sistema.")   
                else:
                    print("No existe esa verdura en nuestro sistema. Intente nuevcamente..")                                             
        elif eleccion == "2":
            global frutas_stock
            while True:   
                fruta_a_eliminar = input("Ingrese el nombre de la fruta que desea eliminar: ")
                if fruta_a_eliminar != " " and fruta_a_eliminar.isalpha(): 
                    if fruta_a_eliminar in frutas_stock:
                        frutas_stock.remove(fruta_a_eliminar)                                  
                        return print(f"Uds elimino exitosamente {fruta_a_eliminar} del stock.")    
                    else:
                        print("No existe esa fruta en nuestro sistema. Intente nuevamente...")
                else:
                    print("Dato incorrecto. Intente nuevamente...")
        else:
            print("Opcion ingresada incorrecta.")
