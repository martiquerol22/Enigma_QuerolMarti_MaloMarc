#import gestor_archivos.py, utilidades.py
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
            editar_rotor()

        elif opcion == 4:
            print("\nSortint del programa...")
            break
    except:
        os.system('cls') # limpia la consola
        print("Escull una opcio valida!")
        continue