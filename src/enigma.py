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