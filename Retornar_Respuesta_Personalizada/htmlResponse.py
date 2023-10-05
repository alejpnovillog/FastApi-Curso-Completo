# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# controlamos las librerias que importamos
try:

    #  Uvicorn es un servidor web ASGI (interfaz de puerta de enlace de servidor asíncrono)
    import uvicorn

    # utilizamos la clase FastApi
    from fastapi import FastAPI

    # Es una subclase de Response que retorna informacion en formato JSON
    from fastapi.responses import HTMLResponse

except Exception as e:
    print(f'Falta algun modulo en Ejemplo_00 --> {e}')


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# creamos una instancia de la clase  FastApi
app = FastAPI()

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# En esta operacion de ruta
# el capitulo del curso
# https://www.youtube.com/watch?v=bqPJl7sxUs8&list=PL2PZw96yQChzll2RHgViiQ8eUvIQycAVl&index=216
# https://www.youtube.com/watch?v=YYSURQ2RpRk&list=PL2PZw96yQChzll2RHgViiQ8eUvIQycAVl&index=217
@app.get("/items/", response_class=HTMLResponse)
async def read_items():
    """
        Debemos asignar a response_class la clase HTMLResponse lo cual asigna a content-type el valor
        "text/html" que sera visualizado en la docs de la url
    """


    html_content = """
    <html>
        <head>
            <title>Some HTML in here</title>
        </head>
        <body>
            <h1>Look ma! HTML!</h1>
        </body>
    </html>
    """

    return HTMLResponse(content=html_content, status_code=200)

# Llamamos al servidor para que inicie
if __name__ ==  "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
