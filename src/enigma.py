
"""
wire_1 = cargar_rotores("src/Rotor1.txt")[0]
notch_1 = cargar_rotores("src/Rotor1.txt")[1]

wire_2 = cargar_rotores("src/Rotor2.txt")[0]
notch_2 = cargar_rotores("src/Rotor2.txt")[1]

wire_3 = cargar_rotores("src/Rotor3.txt")[0]
notch_3 = cargar_rotores("src/Rotor3.txt")[1]
"""

wire_1 = list("YFGXRHAZOVCDBLPEQMIJKSUWNT") #lista de rorotres de prueba
notch_1 = "N"
wire_2 = list("DGNRISMJZKOVWETLAQPXHCUYBF")
notch_2 = "H"
wire_3 = list("TLUYDGMCPOAKRXJHQBESIFZVWN")
notch_3 = "M"

print(wire_1)

mensaje_encriptar = input("Escriba el mensaje que desea encriptar: ") #input del mensaje que el usuario quiere encriptar


letra_seleccionada1 = input("Escriba la letra que quiera para que sea la primera del rotor 1: ").upper()
letra_seleccionada2 = input("Escriba la letra que quiera para que sea la primera del rotor 2: ").upper()
letra_seleccionada3 = input("Escriba la letra que quiera para que sea la primera del rotor 3: ").upper()

def posicion_inicial_rotor(rotor_name, wire, letra_seleccionada): #funcion que hace rotar el rotor hasta la letra inicial que le usuario ha seleccionado

    while wire[0] != letra_seleccionada:
        primer_caracter = wire.pop(0)
        wire.append(primer_caracter)

    return wire

def movimiento_rotor(wire, notch): #funcion que hace que el rotor gire una posicion por cada letra en el mensaje para encriptar
    primer_caracter = wire.pop(0)
    wire.append(primer_caracter)

    return wire


def gestionar_movimiento_rotores_triple(wire_1, notch_1, wire_2, notch_2, wire_3, notch_3): #funcion que hace que el segundo y el tercer rotor giren cuando llegue a su letra notch
    
    if wire_2[0] == notch_2:
        movimiento_rotor(wire_3, notch_3) 
    if wire_1[0] == notch_1 or wire_2[0] == notch_2:
        movimiento_rotor(wire_2, notch_2) 

    return wire_1, wire_2, wire_3

def procesar_mensaje_rotor(texto_limpio, wire): #el print que se ha utilizado para debugar el programa y ver en consola las posiciones de cada rotor 
    global wire_1, wire_2, wire_3, notch_1, notch_2, notch_3 

    print(" R1 | R2 | R3 ")
    print("----|----|----")

    for i, caracter_entrada in enumerate(texto_limpio):

        gestionar_movimiento_rotores_triple(wire_1, notch_1, wire_2, notch_2, wire_3, notch_3)
        
        movimiento_rotor(wire_1, notch_1)

        print(f"  {wire_1[0]} | {wire_2[0]}  |  {wire_3[0]} ")
    
    return wire_1, wire_2, wire_3 


wire_1 = posicion_inicial_rotor("rotor", wire_1, letra_seleccionada1)
wire_2 = posicion_inicial_rotor("rotor", wire_2, letra_seleccionada2)
wire_3 = posicion_inicial_rotor("rotor", wire_3, letra_seleccionada3)

print("\n- Posición Inicial -")
print(f"R 1: {wire_1[0]} | R 2: {wire_2[0]} | R 3: {wire_3[0]}")


procesar_mensaje_rotor(mensaje_encriptar, wire_1 ) 


        



