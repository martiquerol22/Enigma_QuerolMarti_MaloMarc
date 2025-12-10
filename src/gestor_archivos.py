def cargar_rotores(rotor):
    try:
        print(f"[INFO] Llegint {rotor}...")
        with open(rotor,"r") as file:
            data = file.readlines()
            wire = data[0].strip() # elimina el \n
            
            """Si no encuentra la 2a linia del archivo asigna el notch como Z"""
            try:
                notch = data[1]
            except:
                notch = "Z"

    except FileNotFoundError:
        print(f"[ERROR]: No s'ha trobat el arxiu {rotor}.")
        return

    print(f"[OK] Arxiu {rotor} llegit correctament!\n")
    return wire, notch

wire = cargar_rotores("Rotor1.txt")[0]
rotor = "Rotor1.txt"
def validar_rotores(wire):
    print(f"[INFO] Validant {rotor}...")
    if len(wire) != 26:
        print(f"[ERROR] {rotor}: permutació incorrecta — calen 26 lletres uniques A-Z.")
        return False # si no se cumple sale de la funcion y devuelve False

    """Mira si hay caracteres repetidos"""
    caracteres_vistos = set()
    for char in wire:
        if char in caracteres_vistos:
            print(f"[ERROR] {rotor}: permutació incorrecta — calen 26 lletres uniques A-Z")
            return False # si no se cumple sale de la funcion y devuelve False
        caracteres_vistos.add(char)
    print(f"[OK] {rotor} validat!\n")
    return True # si se cumplen todas las condiciones devuelve True

#cargar_rotores(rotor)
validar_rotores(wire)