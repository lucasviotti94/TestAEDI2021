
 
class Habitacion:
    #constructor
    def __init__(self,numero,max_pesonas,precio):
        self.numero = numero                        #unico
        self.max_pesonas = max_pesonas
        self.precio = precio

    def mostrar_información(self):
        print(f"El numero de esta habitacion es {self.numero}, se realizara el dia {self.max_pesonas}, en {self.precio}.")

    def set_max_personas(self,nueva_max_personas):
        self.max_pesonas = nueva_max_personas
        print(f"La cantidad maximaa de personas se cambio de manera correcta a: {nueva_max_personas}.")

    def set_precio(self,precio_nuevo):
        self.precio = precio_nuevo
        return print(f"El nuevo precio de la habitacion se cambio correctamente a : {precio_nuevo}.")
    
    def tipo_de_habitacion(self):
        return (type(self).__name__)
        


class HabitacionClasica(Habitacion):

    def __init__(self,numero,max_pesonas,precio,cant_televisores): #Atributo extra: Cantidad de televisores
        super().__init__(numero,max_pesonas,precio)
        self.cant_televisores = cant_televisores

    def mostrar_información(self):
        print(f"El numero de esta habitacion es {self.numero}, se realizara el dia {self.max_pesonas}, en {self.precio}, y ademas cuenta con el siguiente numero de televisores: {self.cant_televisores} ") 

class HabitacionPremium(Habitacion):

    def __init__(self,numero,max_pesonas,precio,Jacuzzi = True): #Atributo extra: Jacuzzi
        super().__init__(numero,max_pesonas,precio)
        self.Jacuzzi = Jacuzzi        

    def mostrar_información(self,Jacuzzi):
        if Jacuzzi == True:
            disponible = "Jacuzzi disponible"
            print(f"El numero de esta habitacion es {self.numero}, se realizara el dia {self.max_pesonas}, en {self.precio} y ademas cuenta con {disponible}")        
        else:
            no_disponible = "no cuenta con jacuzzi."
            print(f"El numero de esta habitacion es {self.numero}, se realizara el dia {self.max_pesonas}, en {self.precio} y esta habitacion {no_disponible}")
        
