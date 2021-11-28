"""
###**Ejercicio 6.4**
Crear una clase padre Vehiculos:
*   Constructor debe incluir los atributos (patente,marca,año,origen)
*   Crear metodos para esta clase de:
    1.  Presentarse (patente,marca,año,origen)
    2.  Indicar tipos de vehiculo(Clases heredadas)
    3.  Metodos que luego modificarán las clases hijas. Acelerar, Retroceder, obtener_velocidad, setear_velocidad
"""
class Vehiculo:
    def __init__(self,patente,marca,año,origen):
        self.patente = patente
        self.marca = marca
        self.año = año
        self.origen = origen
    
    def presentarse(self):
        print(f"soy un vehiculo con patente {self.patente}, marca {self.marca}, del año {self.año} y origen {self.origen}")

    def tipo_vehiculo(self):
        print("Soy un vehiculo tipo", type(self).__name__)

    def acelerar(self):
        pass

    def retroceder(self):
        pass

    def obtener_velocidad_max(self):
        pass

    def setear_velocidad_max(self):
        pass

class Vehiculos_Particular(Vehiculo):
    def __init__(self, patente, marca, ano, origen, velocidad_max = 130): #Velocidad por defecto
        super().__init__(patente, marca, ano, origen)
        self.velocidad_max = velocidad_max
 
    def acelerar(self):
        print("Estoy acelerando VP")
 
    def retroceder(self):
        print("Estoy retrocediendo VP")
 
    def obtener_velocidad_max(self):
        print(f"La velocidad maxima es {self.velocidad_max}")
 
    def setear_velocidad_max(self, velocidad_max_nueva):
        print (f"La velocidad maxima era {self.velocidad_max} y ahora es {velocidad_max_nueva}")
        self.velocidad_max = velocidad_max_nueva
 
class Vehiculos_PickUp(Vehiculo):
    def __init__(self, patente, marca, ano, origen, velocidad_max = 100): #Velocidad por defecto
        super().__init__(patente, marca, ano, origen)
        self.velocidad_max = velocidad_max
 
    def acelerar(self):
        print("Estoy acelerando VPU")
 
    def retroceder(self):
        print("Estoy retrocediendo VPU")
 
    def obtener_velocidad_max(self):
        print(f"La velocidad maxima es {self.velocidad_max}")
 
    def setear_velocidad_max(self, velocidad_max_nueva):
        print (f"La velocidad maxima era {self.velocidad_max} y ahora es {velocidad_max_nueva}")
        self.velocidad_max = velocidad_max_nueva
 
class Vehiculos_Deportivo(Vehiculo):
    def __init__(self, patente, marca, ano, origen, velocidad_max = 200): #Velocidad por defecto
        super().__init__(patente, marca, ano, origen)
        self.velocidad_max = velocidad_max
 
    def acelerar(self):
        print("Estoy acelerando VD")
 
    def retroceder(self):
        print("Estoy retrocediendo VD")
 
    def obtener_velocidad_max(self):
        print(f"La velocidad maxima es {self.velocidad_max}")
 
    def setear_velocidad_max(self, velocidad_max_nueva):
        print (f"La velocidad maxima era {self.velocidad_max} y ahora es {velocidad_max_nueva}")
        self.velocidad_max = velocidad_max_nueva
 
