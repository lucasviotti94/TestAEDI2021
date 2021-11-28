from Funciones import ver_productos, pagar_credito, consultar_stock, pagar_debito, pagar_efectivo, agregar_stock, cambiar_precio



while True:                                  #Este es el menu donde pido que ingrese una condicion para saber que desea hacer el usuario
    condicion = input(""" 
    Bienvenido a ningun lado, a continuacion ingrese lo que desee hacer:
    1. Ver los productos
    2. Pagar con tarjeta de credito (Se debe contar 10% mas, y se debe descontar el stock).
    3. Pagar con tarjeta de debido (Se debe descontar el stock).
    4. Pagar con efectivo (Se debe descontar el stock y resto 10%).
    5. Consultar productos y stock.
    6. Agregar stock a los productos.
    7. Cambiar el precio a los productos.
    """)

    if condicion == "1":
        ver_productos()
    elif condicion == "2":
        pagar_credito()        
    elif condicion == "3":
        pagar_debito()
    elif condicion == "4":
        pagar_efectivo()  
    elif condicion == "5":
        consultar_stock()  
    elif condicion == "6":
        agregar_stock()
    elif condicion == "7":
        cambiar_precio()      
    else:
        print("Opcion ingresada incorrectamente.")


























