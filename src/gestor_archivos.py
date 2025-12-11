import utilidades

def cargar_rotores(rotor):
    try:
        print(f"[INFO] Llegint {rotor}...")
        with open(rotor,"r") as file:
            data = file.readlines()
            wire = data[0].strip() # elimina el \n
            
            """Si no encuentra la 2a linia del archivo asigna el notch como Z"""
            try:
                notch = data[1].strip() # por si hubiera in \n
            except:
                notch = "Z"

    except FileNotFoundError:
        print(f"[ERROR]: No s'ha trobat el arxiu {rotor}.")
        return

    print(f"[OK] Arxiu {rotor} llegit correctament!\n")
    return wire, notch

#wire = cargar_rotores("Rotor1.txt")[0]
#rotor = "data/Rotor1.txt"

def editar_rotor(rotor, new_wire):
    if utilidades.validar_rotores(new_wire, rotor) == False:
        return
    
    datos = cargar_rotores(rotor)
    
    if datos is None:
        return
    
    notch_actual = datos[1]

    try:
        with open(rotor, "w") as file:
            file.write(f"{new_wire}\n{notch_actual}")
        print(f"[OK] {rotor} actualitzat correctament.")

    except Exception as e:
        print(f"[ERROR] No s'ha pogut escriure: {e}")

    
"""
entrada = input("Selecciona un rotor (1-3): ")
ruta = f"data/Rotor{entrada}.txt" 
    
# Alfabeto válido de prueba
nuevo_alfabeto = "EKMFLGDQVZNTOWYHXUSPAIBRCJ" 
    
editar_rotor(ruta, nuevo_alfabeto)
"""