ALFABETO = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

#hace lo mismo que el de desencriptar pero a la inversa
def desencriptar(letra, wire_1, wire_2, wire_3):
    if letra not in ALFABETO: 
        return letra
    
    indice_r3 = wire_3.index(letra)
    letra_puente_2 = ALFABETO[indice_r3]
    
    indice_r2 = wire_2.index(letra_puente_2)
    letra_puente_1 = ALFABETO[indice_r2]
    
    indice_r1 = wire_1.index(letra_puente_1)
    salida = ALFABETO[indice_r1]
    
    return salida

def encriptar(letra, wire_1, wire_2, wire_3):
    if letra not in ALFABETO: 
        return letra #devuelve el caracter que no esta dentro del alfabeto
    indice = ALFABETO.index(letra) #busca la posicion de cada letra del mensaje en el alfabeto
    letra_r1 = wire_1[indice] #la letra del primer rotor sera 
    
    indice_r2 = ALFABETO.index(letra_r1)
    letra_r2 = wire_2[indice_r2]
    
    indice_r3 = ALFABETO.index(letra_r2)
    salida = wire_3[indice_r3]
    
    return salida


