# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# controlamos las librerias que importamos
try:

    #  Uvicorn es un servidor web ASGI (interfaz de puerta de enlace de servidor asíncrono)
    import uvicorn

    from typing import Any

    import orjson

    # utilizamos la clase FastApi
    from fastapi import FastAPI, Response


except Exception as e:
    print(f'Falta algun modulo en Ejemplo_00 --> {e}')

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# creamos una instancia de la clase  FastApi
app = FastAPI()

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
class CustomORJSONResponse(Response):
    media_type = "application/json"

    def render(self, content: Any) -> bytes:
        assert orjson is not None, "orjson must be installed"
        return orjson.dumps(content, option=orjson.OPT_INDENT_2)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# En esta operacion de ruta
@app.get("/", response_class=CustomORJSONResponse)
async def main():
    return {"message": "Hello World"}


# Llamamos al servidor para que inicie
if __name__ ==  "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
