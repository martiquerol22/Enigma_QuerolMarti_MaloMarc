def validar_rotores(rotor):
    try:
        with open(rotor,"r") as file:
            data = file.readlines()
            print(data)
    except FileNotFoundError:
        print(f"ERROR: No se ha encontrado el archivo {rotor}.")


import re
import unicodedata

def limpiar_texto(raw_text):
    """Normaliza el texto"""
    formato = unicodedata.normalize('NFD', raw_text.upper()) # separa las letras de los acentos (Á --> A´)
    texto_sin_acentos = re.sub(r'[\u0300-\u036f]', '', formato) # elimina ´
    texto_limpio = re.sub(r'[^A-Z]', '', texto_sin_acentos) # elimina todo lo que no sea de la A-Z
    

    """Añade un espacio cada 5 caracteres"""
    texto_separado = [texto_limpio[i:i+5] for i in range(0, len(texto_limpio), 5)]
    return ' '.join(texto_separado)
