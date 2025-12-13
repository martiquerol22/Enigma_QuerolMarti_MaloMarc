#movimiento de los rotores
"""
wire_1 = cargar_rotores("src/Rotor1.txt")[0]
notch_1 = cargar_rotores("src/Rotor1.txt")[1]

wire_2 = cargar_rotores("src/Rotor2.txt")[0]
notch_2 = cargar_rotores("src/Rotor2.txt")[1]

wire_3 = cargar_rotores("src/Rotor3.txt")[0]
notch_3 = cargar_rotores("src/Rotor3.txt")[1]
"""

wire_1 = list("YFGXRHAZOVCDBLPEQMIJKSUWNT")
notch_1 = "N"
wire_2 = list("DGNRISMJZKOVWETLAQPXHCUYBF")
notch_2 = "H"
wire_3 = list("TLUYDGMCPOAKRXJHQBESIFZVWN")
notch_3 = "M"

print(wire_1)

mensaje_encriptar = input("Escriba el mensaje que desea encriptar: ")


letra_seleccionada1 = input("Escriba la letra que quiera para que sea la primera del rotor 1: ").upper()
letra_seleccionada2 = input("Escriba la letra que quiera para que sea la primera del rotor 2: ").upper()
letra_seleccionada3 = input("Escriba la letra que quiera para que sea la primera del rotor 3: ").upper()

def posicion_inicial_rotor(rotor, wire, letra_seleccionada):
    while wire[0] != letra_seleccionada:
        primer_caracter = wire.pop(0)
        wire.append(primer_caracter)

    return wire

def movimiento_rotor(rotor, wire):
    primer_caracter = wire.pop(0)
    wire.append(primer_caracter)

    return wire


print(posicion_inicial_rotor("rotor", wire_1, letra_seleccionada1))
print(movimiento_rotor("rotor", wire_1))


def procesar_mensaje_rotor(mensaje, wire):
    rotor_actual = wire 
    for i, caracter_entrada in enumerate(mensaje):
        rotor_actual = movimiento_rotor(rotor_actual) 
        caracter_salida = rotor_actual[0]
        mensaje_encriptar += caracter_salida
        print(f"Paso {i+1}: Carácter '{caracter_entrada}' -> Rotor: {rotor_actual} -> Salida: '{caracter_salida}'")
    
    return mensaje_encriptar, rotor_actual 

print(procesar_mensaje_rotor(mensaje_encriptar, wire_1))



        



