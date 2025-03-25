# Lista para almacenar las personas
personas = []

while True:
    # Pedimos los datos personales
    nombre = input("Ingrese el nombre: ")
    apellido = input("Ingrese el apellido: ")
    dni = input("Ingrese el DNI: ")
    
    # Lista para los teléfonos
    telefonos = []
    while True:
        telefono = input("Ingrese un número de teléfono (o 'fin' para terminar): ")
        if telefono.lower() == 'fin':  # Si el usuario escribe "fin", se detiene la carga de teléfonos
            break
        telefonos.append(telefono)
    
    # Guardamos los datos en una lista y la agregamos a la lista principal
    personas.append([nombre, apellido, dni, telefonos])
    
    # Preguntamos si quiere cargar otra persona
    continuar = input("¿Desea cargar otra persona? (si/no): ")
    if continuar.lower() != 'si': 
        break

# Mostramos los datos almacenados
print("\nDatos ingresados:") #\n essto es un salto de linea
for persona in personas:
    print(persona)
