try:
    tramos=int(input("Ingrese a continuacion la cantidad de tramos que posee el viaje: "))
    
    for i in range(1,tramos+1,1):
        duracionTramos = int(input(f"Ingrese en minutos la duracion del tramo {i}: "))
        totalViaje = duracionTramos+totalViaje            
        print(f"La duracion total del viaje es de {totalViaje}")
              
except:
    print("Udsted ingreso datos incorrectos.")


