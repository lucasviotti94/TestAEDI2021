import Libro as lb
import gestorDeLibros as gp

gestor = gp.gestorDeLibros()
while True:
    opcion = input(
    """
-----------Programa de Gestión de la biblioteca-----------
Por favor ingrese una opcion:
    1. Crear libro.
    2. Listar libros disponibles.
    3. Cambiar estado de libro.
    8. Salir
    Opcion: """
    )
    if (opcion=="1"):
        gestor.crear_libro()
    elif (opcion=="2"):
        gestor.lista_libros_disponbles()
    elif (opcion=="3"):
        gestor.cambiar_estado_libro()
    elif (opcion=="4"):
        break
    else: 
        print("ninguna opcion correcta")