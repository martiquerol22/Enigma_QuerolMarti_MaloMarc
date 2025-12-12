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
contador_mensaje_encriptar = 0
tamano_mensaje = len(mensaje_encriptar)

print(tamano_mensaje)

letra_seleccionada1 = input("Escriba la letra que quiera para que sea la primera del rotor 1: ")
letra_seleccionada2 = input("Escriba la letra que quiera para que sea la primera del rotor 2: ")
letra_seleccionada3 = input("Escriba la letra que quiera para que sea la primera del rotor 3: ")

def movimiento_rotor(rotor):
    primer_caracter = wire_1.pop(0)
    wire_1.append(primer_caracter)

    return rotor

def procesar_mensaje_rotor(mensaje):
    for i, caracter_entrada in enumerate(mensaje):
        rotor_actual = movimiento_rotor(rotor_actual) 
        caracter_salida = rotor_actual[0]
        mensaje_encriptar += caracter_salida
        print(f"Paso {i+1}: Carácter '{caracter_entrada}' -> Rotor: {rotor_actual} -> Salida: '{caracter_salida}'")
    
    return mensaje_encriptar, rotor_actual 

print(procesar_mensaje_rotor)


        



