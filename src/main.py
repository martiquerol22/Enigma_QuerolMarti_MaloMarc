import gestor_archivos, utilidades, enigma
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
            print("\n--- XIFRATGE ---")
            
            datos_r1 = gestor_archivos.cargar_rotores("data/Rotor1.txt")
            datos_r2 = gestor_archivos.cargar_rotores("data/Rotor2.txt")
            datos_r3 = gestor_archivos.cargar_rotores("data/Rotor3.txt")

            if datos_r1 is None or datos_r2 is None or datos_r3 is None:
                input("[ERROR] al carregant rotors. Prem ENTER...")
                continue

            wire1 = list(datos_r1[0])
            notch1 = datos_r1[1]
            wire2 = list(datos_r2[0])
            notch2 = datos_r2[1]
            wire3 = list(datos_r3[0])
            notch3 = datos_r3[1]

            pos1 = input("Posició inicial Rotor 1: ").upper()
            pos2 = input("Posició inicial Rotor 2: ").upper()
            pos3 = input("Posició inicial Rotor 3: ").upper()

            enigma.posicion_inicial_rotor("R1", wire1, pos1)
            enigma.posicion_inicial_rotor("R2", wire2, pos2)
            enigma.posicion_inicial_rotor("R3", wire3, pos3)

            try:
                with open("data/Mensaje.txt", "r") as f:
                    mensaje_raw = f.read()
            except FileNotFoundError:
                print("[ERROR] No s'ha trobat data/Mensaje.txt")
                input("Prem ENTER per continuar...")
                continue

            mensaje_limpio = utilidades.limpiar_texto(mensaje_raw)
            resultado = ""

            for letra in mensaje_limpio:
                if letra in enigma.ALFABETO:
                    enigma.gestionar_movimiento_rotores_triple(wire1, notch1, wire2, notch2, wire3, notch3)
                    enigma.movimiento_rotor(wire1, notch1)
                    
                    letra_cifrada = enigma.encriptar(letra, wire1, wire2, wire3)
                    resultado += letra_cifrada

            resultado_final = utilidades.separador_mensaje(resultado)

            with open("data/Xifrat.txt", "w") as f:
                f.write(resultado_final)
            
            print(f"Missatge xifrat guardat a data/Xifrat.txt: {resultado_final}")
            input("Prem ENTER per continuar...")

        elif opcion == 2:
            print("\n--- DESXIFRATGE ---")

            datos_r1 = gestor_archivos.cargar_rotores("data/Rotor1.txt")
            datos_r2 = gestor_archivos.cargar_rotores("data/Rotor2.txt")
            datos_r3 = gestor_archivos.cargar_rotores("data/Rotor3.txt")

            if datos_r1 is None or datos_r2 is None or datos_r3 is None:
                input("[ERROR] al carregant rotors. Prem ENTER...")
                continue

            wire1 = list(datos_r1[0])
            notch1 = datos_r1[1]
            wire2 = list(datos_r2[0])
            notch2 = datos_r2[1]
            wire3 = list(datos_r3[0])
            notch3 = datos_r3[1]

            pos1 = input("Posició inicial Rotor 1: ").upper()
            pos2 = input("Posició inicial Rotor 2: ").upper()
            pos3 = input("Posició inicial Rotor 3: ").upper()

            enigma.posicion_inicial_rotor("R1", wire1, pos1)
            enigma.posicion_inicial_rotor("R2", wire2, pos2)
            enigma.posicion_inicial_rotor("R3", wire3, pos3)

            try:
                with open("data/Xifrat.txt", "r") as f:
                    mensaje_cifrado = f.read().replace(" ", "")
            except FileNotFoundError:
                print("[ERROR] No s'ha trobat data/Xifrat.txt")
                input("Prem ENTER per continuar...")
                continue

            resultado = ""

            for letra in mensaje_cifrado:
                if letra in enigma.ALFABETO:
                    enigma.gestionar_movimiento_rotores_triple(wire1, notch1, wire2, notch2, wire3, notch3)
                    enigma.movimiento_rotor(wire1, notch1)
                    
                    letra_descifrada = enigma.desencriptar(letra, wire1, wire2, wire3)
                    resultado += letra_descifrada

            with open("data/desxifrat.txt", "w") as f:
                f.write(resultado)

            print(f"Missatge desxifrat guardat a data/desxifrat.txt: {resultado}")
            input("Prem ENTER per continuar...")

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