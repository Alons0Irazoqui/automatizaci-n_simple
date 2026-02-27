from .sanitizar_texto import sanitizar_texto

palabras_ignorar = [
    "quiero", "saber", "dame", "buscar", "cual", "es", "por", "favor",
    "el", "la", "un", "una", "de", "en", "del", "a",
    "precio", "accion", "acciones", "clima", "temperatura", "las", "para"
]

def definir_entidad(texto):
    texto = sanitizar_texto(texto)
    palabras_usuario = texto.split()
    palabras_limpias = []
    
    for palabra in palabras_usuario:
        if palabra not in palabras_ignorar:
            palabras_limpias.append(palabra)
    
    entidad_encontrada = " ".join(palabras_limpias)
    
    return entidad_encontrada