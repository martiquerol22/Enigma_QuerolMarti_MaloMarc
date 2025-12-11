import re
import unicodedata

def limpiar_texto(raw_text):
    """Normaliza el texto"""
    formato = unicodedata.normalize('NFD', raw_text.upper()) # separa las letras de los acentos (Á --> A´)
    texto_sin_acentos = re.sub(r'[\u0300-\u036f]', '', formato) # elimina ´
    texto_limpio = re.sub(r'[^A-Z]', '', texto_sin_acentos) # elimina todo lo que no sea de la A-Z

    print(f"[OK] Missatge normalitzat correctament!\n")
    return texto_limpio

def separador_mensaje(texto_limpio):
    """Añade un espacio cada 5 caracteres"""
    n = 5 # n = el nombre de caracteres antes del espacio, asi puede variar
    texto_separado = [texto_limpio[i:i+n] for i in range(0, len(texto_limpio), n)]
    print(f"[OK] Missatge separat cada {n} caracters!")
    return ' '.join(texto_separado)

#print(separador_mensaje("HOLABUENDIACOMOESTAMOS"))


#wire = cargar_rotores("data/Rotor1.txt")[0]
#rotor = f"Rotor{int(input("Selecciona un rotor (1-3)."))}.txt"
#notch = "H"

def validar_rotores(wire, rotor):
    print(f"[INFO] Validant {rotor}...")
    if len(wire) != 26:
        print(f"[ERROR] {rotor}: permutacio incorrecta - calen 26 lletres uniques A-Z.")
        return False # si no se cumple sale de la funcion y devuelve False

    """Mira si hay caracteres repetidos"""
    caracteres_vistos = set()
    for char in wire:
        if char in caracteres_vistos:
            print(f"[ERROR] {rotor}: permutacio incorrecta - calen 26 lletres uniques A-Z")
            return False # si no se cumple sale de la funcion y devuelve False
        caracteres_vistos.add(char)
    print(f"[OK] {rotor} validat!\n")
    return True # si se cumplen todas las condiciones devuelve True

#cargar_rotores(rotor)
#validar_rotores(wire)

