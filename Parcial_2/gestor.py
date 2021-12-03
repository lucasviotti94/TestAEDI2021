import Clases as cl
import os

path = os.path.abspath(os.path.dirname("historial_habitaciones.csv"))
lista_habitaciones = []
precio_habitaciones = {
    "Habitacion": 300, 
    "HabitacionClasica": 400,
    "HabitacionPremium": 500
    }


class GestorHabitaciones():    
    def __init__(self):
        pass

    def crear_habitacion(self):
        while True:
            datos = []            
            opcion = input("""
Ingrese a continuacion que tipo de habitacion desea crear: 
1 - Habitacion normal.
2 - Habitacion Clasica.
3 - Habitacion Premium.
""")  
            if (opcion=="1" or opcion=="2" or opcion=="3"):
                break
            else:
                print("Opcion Incorrecta")
        # Numero de la habitacion        
        Flag = True
        while Flag:
            try:
                numero_habitacion = int(input("Ingrese a continuacion el numero de la habitacion nueva: "))
                for habitaciones in lista_habitaciones:
                    if (numero_habitacion != habitaciones.numero):                            
                        datos.append(numero_habitacion)
                        Flag = False
                    else:
                        print("Ya existe este numero de habitacion, ingrese otro.")
            except:
                print("Ingrese solamente numeros enteros.")
        # Max_pesonas de la habitacion
        while True:
            try:
                max_personas_nuevo = int(input("Ingrese a continuacion la cantidad de personas de la pieza nueva: "))
                if (max_personas_nuevo > 1) and (max_personas_nuevo < 7):
                    print("Numero ingresado correctamente.")
                    datos.append(max_personas_nuevo)
                    break
                else:
                    print("Ingrese unicamente un numero entre 2 y 6 inclusives.")
            except:
                print("Ingrese solo numeros enteros..")
        # Precio de la habitacion
        Flag = True
        while Flag:
            try:
                precio_habitacion = float(input("Ingrese a continuacion el precio de la habitacion en pesos: "))
                precio_en_dolar = precio_habitacion/200
                print("Precio agregado de manera correcta en dolares.")
                datos.append(precio_en_dolar)
                Flag = False
            except:
                print("Ingrese unicamente numeros.")

        if opcion == "1":       #Aqui creo la habitacion normal
            nombre_instancia = cl.Habitacion(numero_habitacion, max_personas_nuevo, precio_en_dolar)
            lista_habitaciones.append(nombre_instancia)
            print("La habitacion se creo de manera existosa.")
            habitacion_tipo = str(nombre_instancia.tipo_de_habitacion())
            datos.append(habitacion_tipo)           
            self.logeador_habitaciones(datos)
            return
        elif opcion == "2":
            while True:
                try:
                    cant_televeisores_nuevo = int(input("Ingrese a continuacion la cantidad de televisores de la pieza nueva: "))
                    if (cant_televeisores_nuevo >= 0) and (cant_televeisores_nuevo <= 3):                        
                        nombre_instancia = cl.HabitacionClasica(numero_habitacion, max_personas_nuevo, precio_en_dolar,cant_televeisores_nuevo)
                        lista_habitaciones.append(nombre_instancia)
                        print("La habitacion se creo de manera existosa.")
                        habitacion_tipo = str(nombre_instancia.tipo_de_habitacion())
                        datos.append(habitacion_tipo)                        
                        self.logeador_habitaciones(datos)
                        break
                    else:
                        print("Ingrese unicamente un numero entre 0 y 3 inclusives.")
                except:
                    print("Ingrese solo numeros enteros..")
        else:
            while True:
                opcion_elegida = input(
"""Ingrese a continuacion si la habitacion nueva posee Jacuzzi: 
1 - Si
2 - No
""") 
                if (opcion_elegida == "1"):
                    jacuzzi_habitacion_nueva = True
                    break 
                elif (opcion_elegida == "2"):
                    jacuzzi_habitacion_nueva = False
                    break
                else:
                    print("Opcion incorrecta..")

            nombre_instancia = cl.HabitacionPremium(numero_habitacion, max_personas_nuevo, precio_en_dolar,jacuzzi_habitacion_nueva)
            lista_habitaciones.append(nombre_instancia)
            print("La habitacion se creo de manera existosa.")
            habitacion_tipo = str(nombre_instancia.tipo_de_habitacion())
            datos.append(habitacion_tipo)           
            self.logeador_habitaciones(datos)

    def cambiar_precio(self):
        Flag = True
        while Flag:
            numero_elegido = input("Ingrese a continuacion el numero de la habitacion que desea cambiar de precio: ")
            for habitacion in lista_habitaciones:
                if (int(numero_elegido) == habitacion.numero):
                    info_personas = int(habitacion.max_personas())                  #Aca almaceno el max de personas en una variable interna
                    tipo_habitacion = str(habitacion.tipo_de_habitacion())        #Aca almaceno el tipo de habitacion en una variable interna
                    for i in precio_habitaciones:
                        if tipo_habitacion == i:
                            precio_habitacion_cambio = precio_habitaciones.get(i)
                            nuevo_precio = precio_habitacion_cambio*info_personas
                            habitacion.set_precio(nuevo_precio)
                            Flag = False
                else:
                    print("No existe ninguna habitacion con este numero, intente nuevamente...")

    def listar_habitaciones(self):        
        while True:
            try:
                numero_pedido = int(input("Ingrese a continuacion un numero: "))
                cont = 0
                for i in lista_habitaciones:
                    cont+=1
                if (numero_pedido <= cont):
                    for i in range(0,numero_pedido+1,1):
                        print(lista_habitaciones[i])
                    break
                else:
                    print("No existe esa cantidad de habitaciones listadas, ingrese nuevamente otro numero.")
                break
                    
            except:
                print("Solo numeros enteros")

    def logeador_habitaciones(self,datos_parametro):
        try:
            fichero = open(path+"\\historial_habitaciones.csv", "a+")   #Permiso de apertura y actualizacion, y agregar al fondo si existe el archivo
            for i in datos_parametro:
                fichero.write(i+",")
            fichero.write("\n")
            fichero.close()
        except:
            print("Error")


