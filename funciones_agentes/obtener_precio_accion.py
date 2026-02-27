import yfinance as yf


def obtener_precio_por_nombre(nombre_empresa):
    try:
        # Buscar empresa
        search = yf.Search(nombre_empresa)
        resultados = search.quotes
        
        if not resultados:
            return "No encontré esa empresa."
        
        # Tomamos el primer resultado
        ticker = resultados[0]["symbol"]
        nombre_real = resultados[0]["shortname"]
        
        stock = yf.Ticker(ticker)
        precio = stock.history(period="1d")["Close"].iloc[-1]
        
        # Obtenemos la moneda en la que cotiza (ej. USD, MXN, EUR)
        # Usamos .get() por si acaso yfinance no encuentra el dato, no marque error
        moneda = stock.info.get("currency", "")
        
        return f"{nombre_real} ({ticker}): ${precio:.2f} {moneda}"
    
    except Exception as e:
        return "Hubo un error al consultar la empresa."