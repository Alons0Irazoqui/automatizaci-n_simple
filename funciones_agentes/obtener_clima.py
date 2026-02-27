import requests

API_KEY = "9e0207c605b2d4abb191039667b78bcb"

#obtener el clima
def obtener_clima(ciudad):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={API_KEY}&units=metric"

    respuesta = requests.get(url)
    datos = respuesta.json()

    if respuesta.status_code == 200:
        temperatura = datos["main"]["temp"]
        print(f"Temperatura actual en {ciudad}: {temperatura}°C")
    else:
        print("No se encontró la ciudad.")
        print(respuesta.status_code)
        print(datos)

