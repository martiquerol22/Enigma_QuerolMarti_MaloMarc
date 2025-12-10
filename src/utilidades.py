
#wire = cargar_rotores("data/Rotor1.txt")[0]
#rotor = f"Rotor{int(input("Selecciona un rotor (1-3)."))}.txt"
#notch = "H"

def validar_rotores(wire, rotor):
    print(f"[INFO] Validant {rotor}...")
    if len(wire) != 26:
        print(f"[ERROR] {rotor}: permutacio incorrecta - calen 26 lletres uniques A-Z.")
        return False # si no se cumple sale de la funcion y devuelve False

    """Mira si hay caracteres repetidos"""
    caracteres_vistos = set()
    for char in wire:
        if char in caracteres_vistos:
            print(f"[ERROR] {rotor}: permutacio incorrecta - calen 26 lletres uniques A-Z")
            return False # si no se cumple sale de la funcion y devuelve False
        caracteres_vistos.add(char)
    print(f"[OK] {rotor} validat!\n")
    return True # si se cumplen todas las condiciones devuelve True

#cargar_rotores(rotor)
#validar_rotores(wire)

