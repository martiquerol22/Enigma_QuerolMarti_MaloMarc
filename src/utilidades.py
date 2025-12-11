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
