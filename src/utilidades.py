def validar_rotores(rotor):
    try:
        with open(rotor,"r") as file:
            data = file.readlines()
    except FileNotFoundError:
        print(f"ERROR: No se ha encontrado el archivo {rotor}.")

        