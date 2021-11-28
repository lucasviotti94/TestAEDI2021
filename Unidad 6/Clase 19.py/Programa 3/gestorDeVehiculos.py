
"""
Crear clase GestorAutos que cuente con las siguientes funciones para un menu
1.   Crear auto, indicando tipo de auto y guardar en una lista
2.   Listar autos (presentandolos), indicando tipo de Vehiculo.
3.   Cambiar velocidad de un Vehiculo
4.   Calcular tiempo de viaje de un Vehiculo en una cant de Km pasados por parametro (tiempo = Km / Velocidad)
"""
from os import truncate
import vehiculo as vh
lista_autos = []

class gestorDeVehiculos:
    def __init__(self):
        pass

    def crear_vehiculo(self):
        while True:
            tipo_auto=input(
            """
        -----------Crear Vehiculo-----------
        Por favor ingrese una opcion:
            1. Vehiculo Generico
            2. Vehiculo Particular
            3. Vehiculo Deportivo
            4. Vehiculo PickUp

            0. Salir 
            
            Opcion: """
            )
            if (tipo_auto=="1" or tipo_auto=="2" or tipo_auto=="3" or tipo_auto=="4"):
                break
            else:
                print("Opcion Incorrecta")

        #patente, marca, año, origen
        patente = input("Ingrese la patente del vehiculo: ")
        marca = input("Ingrese la marca del vehiculo: ")
        origen = input("Ingrese el origen del vehiculo: ")
        while True:
            try:
                año = int(input("Ingrese el año del vehiculo: "))
                break
            except:
                print("Año incorrecto")
        
        if (tipo_auto=="2" or tipo_auto=="3" or tipo_auto=="4"):
            opcion=input("""Desea agregar una velocidad maxima a este vehiculo?
            1. Si
            2. No
            
            Opcion: """)
            if opcion=="1":
                while True:
                    try:
                        velocidad_maxima= int(input("Ingrese la velocidad Maxima: "))
                        break
                    except:
                        print("Velocidad Erronea")
            elif opcion=="2":
                velocidad_maxima=""
        if tipo_auto=="1":
            nuevo_vehiculo=vh.vehiculos(patente,marca,año,origen)
        elif tipo_auto=="2":
            nuevo_vehiculo=vh.Vehiculo_Particular(patente,marca,año,origen,velocidad_maxima)
        elif tipo_auto=="3":
            nuevo_vehiculo=vh.Vehiculo_Deportivo(patente,marca,año,origen,velocidad_maxima)
        elif tipo_auto=="4":
            nuevo_vehiculo=vh.Vehiculo_PickUp(patente,marca,año,origen,velocidad_maxima)
        lista_autos.append(nuevo_vehiculo)
        
    def listar_vehiculos(self):
        for vehiculo in lista_autos:
            vehiculo.presentarse()
            vehiculo.tipo_vehiculo()

    def cambiar_velocidad(self):
        for vehiculo in lista_autos:
            print(vehiculo.patente)
        
        flag=True
        while flag:
            patente = input("Ingrese la patente del cehiculo a cambiarle la velocidad: ")
            for vehiculo in lista_autos:
                if (vehiculo.patente == patente):
                    if (type(vehiculo).__name__!="vehiculos"):
                        while True:
                            try:
                                nueva_velocidad_maxima= int(input("Ingrese la nueva velocidad maxima: "))
                                flag=False
                            except:
                                print("Error")
                        vehiculo.setear_velocidad_max(nueva_velocidad_maxima)
                    else:
                        print("El vehiculo generico no tiene velocidad max")

    def calcular_tiempo(self):
        for vehiculo in lista_autos:
            print(vehiculo.patente)
        
        flag=True
        while flag:
            patente = input("Ingrese la patente del cehiculo a cambiarle la velocidad: ")
            for vehiculo in lista_autos:
                if (vehiculo.patente == patente):
                    if (type(vehiculo).__name__!="vehiculos"):
                        while True:
                            try:
                                km= int(input("Ingrese el km: "))
                                print(f"EL tiempo ern recorrer los {km} = {km/vehiculo.velocidad_max}")
                                flag=False
                            except:
                                print("Error")
                    else:
                        print("El vehiculo generico no tiene velocidad max")