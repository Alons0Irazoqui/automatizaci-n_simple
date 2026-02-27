from funciones_agentes import obtener_precio_por_nombre, obtener_clima
from utils import sanitizar_texto
from utils import definir_entidad


# Simulación
while True:
    print("\n- Hola soy tu asistente virtual, que deseas hacer hoy ¿Quieres saber el precio de una accion o el clima de una cuidad?:")
    texto = sanitizar_texto((input("--> ")))

    
    if "accion" in texto or "precio" in texto:
        if definir_entidad(texto) != "":
            nombre_empresa = definir_entidad(texto)
        else:
            nombre_empresa = sanitizar_texto(input("¿Qué empresa te interesa buscar la accion? "))
        
        print(obtener_precio_por_nombre(nombre_empresa))
            
    elif "clima" in texto or "temperatura" in texto:
        if definir_entidad(texto) != "":
            ciudad = definir_entidad(texto)
        else:
            ciudad = sanitizar_texto(input("¿En qué ciudad quieres saber el clima? "))
            
        obtener_clima(ciudad)

    else:
        print("Lo siento, no entiendo tu solicitud. Por favor, intenta de nuevo.")
    

