
<div align="center">
<img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge" alt="Python" />
<img src="https://img.shields.io/badge/Status-Production-brightgreen?style=for-the-badge" alt="Status" />
<img src="https://img.shields.io/badge/Hybridge%20Education-Ingenier%C3%ADa%20en%20Software-orange?style=for-the-badge" alt="Hybridge" />
</div>

<div align="center">
<h1>Chatbot de Automatización Simple</h1>
</div>

---

Este es un asistente virtual desarrollado en Python que permite a los usuarios consultar información en tiempo real a través de una interfaz de línea de comandos (CLI). El bot procesa el lenguaje natural básico para identificar la intención del usuario, extrae las entidades clave (como ciudades o empresas) y devuelve datos precisos consultando APIs externas de forma continua.

Este proyecto fue desarrollado como parte del 4to cuatrimestre de la carrera de Ingeniería en Software en **Hybridge Education**.

Este es un asistente virtual desarrollado en Python que permite a los usuarios consultar información en tiempo real a través de una interfaz de línea de comandos (CLI). El bot procesa el lenguaje natural básico para identificar la intención del usuario, extrae las entidades clave (como ciudades o empresas) y devuelve datos precisos consultando APIs externas de forma continua.

Este proyecto fue desarrollado como parte del 4to cuatrimestre de la carrera de Ingeniería en Software en **Hybridge Education**.

## Características Principales
---

- **Procesamiento de Texto Modular:** Uso de utilidades personalizadas (`definir_entidad` y `sanitizar_texto`) para limpiar "stop words" y caracteres especiales. Esto permite al bot entender solicitudes directas de forma natural (ej. "quiero saber el clima de los mochis" o "precio apple").
- **Ejecución Continua:** Implementación de un bucle de interacción que permite al usuario hacer múltiples consultas sin necesidad de reiniciar el script.
- **Consulta de Clima en Tiempo Real:** Integración con la API de OpenWeatherMap para obtener la temperatura actual de cualquier ciudad.
- **Mercado Financiero:** Uso de la librería `yfinance` para buscar y devolver el precio de cierre y la divisa (USD, MXN, etc.) de las acciones de empresas que cotizan en bolsa.
- **Arquitectura Limpia:** Código estructurado en módulos, separando la lógica de ejecución principal, las funciones de los agentes externos y las herramientas de procesamiento de texto.

## Tecnologías y Librerías Utilizadas
---

- **Python 3.x**
- **Requests:** Para el consumo de la API REST de OpenWeatherMap.
- **YFinance:** Para la extracción de datos financieros de Yahoo Finance.
- **JSON:** Para el parseo de respuestas de la API.

## Estructura del Proyecto
---

```
automatizacion_simple/
│
├── main.py                  # Archivo principal y bucle de interacción
├── requirements.txt         # Dependencias del proyecto
├── README.md                # Documentación del proyecto
│
├── funciones_agentes/       # Módulo de conexión con APIs externas
│   ├── __init__.py
│   ├── obtener_clima.py     # Lógica de OpenWeatherMap
│   └── obtener_precio_accion.py # Lógica de Yahoo Finance
│
└── utils/                   # Módulo de procesamiento de lenguaje
   ├── __init__.py
   ├── definir_entidad.py   # Filtro de stop words y extracción de palabras clave
   └── sanitizar_texto.py   # Lógica de limpieza y formateo a minúsculas
```

## Instalación y Uso
---

<div align="center">
<img src="https://img.shields.io/badge/Instalaci%C3%B3n-F%C3%A1cil-blue?style=flat-square" alt="Instalación Fácil" />
<img src="https://img.shields.io/badge/CLI-Interactivo-lightgrey?style=flat-square" alt="CLI Interactivo" />
</div>


### Clonar el repositorio
```bash
git clone https://github.com/TU_USUARIO/TU_REPOSITORIO.git
cd automatizacion_simple
```


### Instalar las dependencias
```bash
pip install -r requirements.txt
```
*Nota: Asegúrate de que `yfinance` esté instalado en tu entorno.*


### Configurar la API Key
El proyecto requiere una API Key de OpenWeatherMap. Actualmente se encuentra configurada dentro de `funciones_agentes/obtener_clima.py`.


### Ejecutar el bot
```bash
python main.py
```

## Ejemplos de Uso
---


Al ejecutar el script, el bot entrará en un ciclo y te preguntará qué deseas hacer. Puedes usar lenguaje natural:

#### Para Clima
```text
--> quiero saber el clima de los mochis
Temperatura actual en los mochis: 24.5°C
```

#### Para Acciones
```text
--> dame el precio de apple
Apple Inc. (AAPL): $182.52 USD
```

## Autor
---

<div>
<img src="https://img.shields.io/badge/Hybridge%20Education-Ingenier%C3%ADa%20en%20Software-green?style=for-the-badge" alt="Hybridge" />
<img src="https://img.shields.io/badge/Autor-Alonso%20Irazoqui-blue?style=for-the-badge" alt="Autor Alonso Irazoqui" />
<img src="https://img.shields.io/badge/Estudiante-4to%20Cuatrimestre-red?style=for-the-badge" alt="Estudiante 4to Cuatrimestre" />
</div>

---