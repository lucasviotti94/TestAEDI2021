
productos_lista = [[10,10,10], ["Papel","Lapiz","Goma"], [300,400,500],[5,4,7]]

def ver_productos():
    global productos_lista
    print(f"""
    Stock   Productos   Precios   Codigo            
     {productos_lista [0] [0]}      {productos_lista [1] [0]}        {productos_lista [2] [0]}       {productos_lista [3] [0]}
     {productos_lista [0] [1]}      {productos_lista [1] [1]}        {productos_lista [2] [1]}       {productos_lista [3] [1]}
     {productos_lista [0] [2]}      {productos_lista [1] [2]}         {productos_lista [2] [2]}       {productos_lista [3] [2]}
    """)

def pagar_credito():
    global productos_lista  
    monto_a_abonar = 0       
    while True:        
        opcion_elegida = input(
            """Ingrese a continuacion que productos desea comprar utilizando tarjeta de credito. Seleccione la opcion Pagar cuando termine su eleccion: 
            1. Papel
            2. Lapiz
            3. Goma
            4. Pagar
            """)
        if opcion_elegida == "1":
            monto_a_abonar+= 300
            productos_lista [0] [0]-= 1         
        elif opcion_elegida == "2":
            monto_a_abonar+= 400
            productos_lista [0] [1]-= 1 
        elif opcion_elegida == "3":
            monto_a_abonar+= 500
            productos_lista [0] [2]-= 1        
        elif opcion_elegida == "4":
            break
        else:
            print("Dato incorrecto, intente nuevamente.")
    porcentaje = monto_a_abonar*10/100
    print(f"El monto a pagar es de {monto_a_abonar+porcentaje}.")

def pagar_debito():
    global productos_lista  
    monto_a_abonar = 0       
    while True:        
        opcion_elegida = input(
            """Ingrese a continuacion que productos desea comprar utilizando tarjeta de debito. Seleccione la opcion Pagar cuando termine su eleccion: 
            1. Papel
            2. Lapiz
            3. Goma
            4. Pagar
            """)
        if opcion_elegida == "1":
            monto_a_abonar+= 300
            productos_lista [0] [0]-= 1         
        elif opcion_elegida == "2":
            monto_a_abonar+= 400
            productos_lista [0] [1]-= 1 
        elif opcion_elegida == "3":
            monto_a_abonar+= 500
            productos_lista [0] [2]-= 1        
        elif opcion_elegida == "4":
            break
        else:
            print("Dato incorrecto, intente nuevamente.")
    print(f"El monto a pagar es de {monto_a_abonar}.")

def pagar_efectivo():
    global productos_lista  
    monto_a_abonar = 0       
    while True:        
        opcion_elegida = input(
            """Ingrese a continuacion que productos desea comprar utilizando efectivo. Seleccione la opcion Pagar cuando termine su eleccion: 
            1. Papel
            2. Lapiz
            3. Goma
            4. Pagar
            """)
        if opcion_elegida == "1":
            monto_a_abonar+= 300
            productos_lista [0] [0]-= 1         
        elif opcion_elegida == "2":
            monto_a_abonar+= 400
            productos_lista [0] [1]-= 1 
        elif opcion_elegida == "3":
            monto_a_abonar+= 500
            productos_lista [0] [2]-= 1        
        elif opcion_elegida == "4":
            break
        else:
            print("Opcion incorrecta, intente nuevamente.")
    porcentaje = monto_a_abonar*10/100
    print(f"El monto a pagar es de {monto_a_abonar-porcentaje}.")

def consultar_stock():
    global productos_lista
    print(
        f"""El stock actual de los productos es el siguiente:
        Papeles = {productos_lista [0] [0]}
        Lapices = {productos_lista [0] [1]}
        Gomas = {productos_lista [0] [2]}
        """)

def agregar_stock():
    global productos_lista
    while True:
        producto_elegido = input(
            """Ingrese a continuacion el producto al cual le desea sumar stock, ingrese Salir cuando termine:
            1. Papel
            2. Lapiz
            3. Goma
            4. Salir
            """)
        if producto_elegido == "1":
            while True:
                try:
                    cantidad_a_agregar0 = int(input("Ingrese la cantidad de stock que desea agregar: "))
                    if cantidad_a_agregar0 > 0:
                        productos_lista [0] [0]+= cantidad_a_agregar0
                        print(f"Se agrego exitosamente la cantidad de {cantidad_a_agregar0} al stock de Papeles.")
                        break
                    else:
                        print("Por favor ingrese una cantidad mayor a 0.")  
                except:
                    print("Dato incorrecto, intente nuevamente..")       
        elif producto_elegido == "2":
            while True:
                try:
                    cantidad_a_agregar1 = int(input("Ingrese la cantidad de stock que desea agregar: "))
                    if cantidad_a_agregar1 > 0:
                        productos_lista [0] [1]+= cantidad_a_agregar1
                        print(f"Se agrego exitosamente la cantidad de {cantidad_a_agregar1} al stock de Lapices.")
                        break 
                    else:
                        print("Por favor ingrese una cantidad mayor a 0.")  
                except:
                    print("Dato incorrecto, intente nuevamente..")    
        elif producto_elegido == "3":
            while True:
                try:
                    cantidad_a_agregar2 = int(input("Ingrese la cantidad de stock que desea agregar: "))
                    if cantidad_a_agregar2 > 0:
                        productos_lista [0] [2]+= cantidad_a_agregar2
                        print(f"Se agrego exitosamente la cantidad de {cantidad_a_agregar2} al stock de Gomas.") 
                        break 
                    else:
                        print("Por favor ingrese una cantidad mayor a 0.")                     
                except:
                    print("Dato incorrecto, intente nuevamente..")           
        elif producto_elegido == "4":
            break
        else:
            print("Opcion incorrecta, intente nuevamente.")

def cambiar_precio():
    while True:
        global productos_lista
        eleccion = input(
            """Ingrese a continuacion el producto al cual le desea cambiar el precio:
            1. Papel
            2. Lapiz
            3. Goma
            4. Salir
            """)
        if eleccion == "1":
            while True:
                try:
                    precio_nuevo0 = float(input(f"Ingrese el nuevo precio de Papel: "))
                    if precio_nuevo0 > 0:
                        productos_lista [2] [0] = precio_nuevo0
                        return print("El nuevo precio de Papel se corrigio existosamente.")
                    else:
                        print("Ingrese un numero mayor a 0.")                
                except:
                    print("Dato incorrecto, intente nuevamente.")
        elif eleccion == "2":
            while True:
                try:
                    precio_nuevo1 = float(input(f"Ingrese el nuevo precio de Lapiz: "))
                    if precio_nuevo1 > 0:
                        productos_lista [2] [1] = precio_nuevo1
                        return print("El nuevo precio de Lapiz se corrigio existosamente.")
                    else:
                        print("Ingrese un numero mayor a 0.")                
                except:
                    print("Dato incorrecto, intente nuevamente.")
        elif eleccion == "3":
            while True:
                try:
                    precio_nuevo2 = float(input(f"Ingrese el nuevo precio de Goma: "))
                    if precio_nuevo2 > 0:
                        productos_lista [2] [2] = precio_nuevo2
                        return print("El nuevo precio de Goma se corrigio existosamente.")
                    else:
                        print("Ingrese un numero mayor a 0.")                
                except:
                    print("Dato incorrecto, intente nuevamente.")
        elif eleccion == "4":
            break
        else:
            print(("Opcion incorrecta, intente nuevamente"))
















