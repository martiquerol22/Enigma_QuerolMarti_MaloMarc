def cargar_rotores(rotor):
    try:
        with open(rotor,"r") as file:
            data = file.readlines()
            wire = data[0].strip() # elimina el \n
            
            """Si no encuentra la 2a linia del archivo asigna el notch como Z"""
            try:
                notch = data[1]
            except:
                notch = "Z"

    except FileNotFoundError:
        print(f"ERROR: No se ha encontrado el archivo {rotor}.")
        return
    
    return wire, notch

print(cargar_rotores("src/Rotor1.txt"))

def validar_rotores(wire):
    if len(wire) != 26:
        print(f"ERROR: El cableado ha de ser de 26 letras y tiene {len(wire)}.")
        return False # si no se cumple sale de la funcion y devuelve False

    """Mira si hay caracteres repetidos"""
    caracteres_vistos = set()
    for char in wire:
        if char in caracteres_vistos:
            print("ERROR: Hay letras repetidas en el cableado.")
            return False # si no se cumple sale de la funcion y devuelve False
        caracteres_vistos.add(char)

    return True # si se cumplen todas las condiciones devuelve True
        

print(validar_rotores())