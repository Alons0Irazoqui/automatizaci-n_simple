#formatear el texto minusculas y quitar acentos
def sanitizar_texto(texto):
    texto = texto.lower()
    texto = texto.replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u")
    return texto
