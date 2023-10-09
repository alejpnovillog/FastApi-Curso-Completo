# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# controlamos las librerias que importamos
try:

    #  Uvicorn es un servidor web ASGI (interfaz de puerta de enlace de servidor asíncrono)
    import uvicorn

    # utilizamos la clase FastApi
    from fastapi import FastAPI, Path, Query

    #
    from typing import Annotated

except Exception as e:
    print(f'Falta algun modulo en Ejemplo_00 --> {e}')

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# creamos una instancia de la clase  FastApi
app = FastAPI()


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# En esta operacion de ruta
@app.get("/items/{item_id}")
async def read_items(*, item_id: Annotated[int, Path(title="The ID of the item to get", ge=0, le=1000)], q: str, size: Annotated[float, Query(gt=0, lt=10.5)], ):
    """

    item_id:        Es un parametro requerido de tipo int que sea mayor o igual a 0 y menor o igual a 1000
    q:              Es un parametro requerido de tipo str
    size:           Es un parametro requerido de tipo float que sea mayor o igual a 0 y menor o igual a 10.5

    """

    # asignamos el diccionario
    results = {"item_id": item_id}

    # verificamos si hay query
    if q:
        results.update({"q": q})    # actualizamos el diccionario


    return results

# Llamamos al servidor para que inicie
if __name__ ==  "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
