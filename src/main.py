import gestor_archivos.py, utilidades.py
import os

while True:
    try:
        opcion = int(input(
"""

Que vols fer?
1. Xifrar missatge
2. Desxifrar missatge
3. Editar rotors
4. Sortir
"""))
    
        if opcion == 1:
            cifrado()

        elif opcion == 2:
            descifrado()

        elif opcion == 3:
            entrada = input("Quin rotor vols editar (1-3)? ")

            if entrada not in ["1", "2", "3"]:
                print("[ERROR] Has de triar un número entre 1 i 3.")
                input("Prem ENTER per tornar al menu...")
                os.system('cls') # limpia la consola
                continue # inicia el bucle de nou

            ruta = f"data/Rotor{entrada}.txt"
            nuevo_wire = input("Escriu la nova permutacio (26 lletres): ").upper()
            
            gestor_archivos.editar_rotor(ruta, nuevo_wire)
            input("\nPrem ENTER per continuar...")

        elif opcion == 4:
            print("\nSortint del programa...")
            break
    except:
        os.system('cls') # limpia la consola
        print("Escull una opcio valida!")
        continue