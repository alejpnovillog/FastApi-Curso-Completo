# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# controlamos las librerias que importamos
try:

    #  Uvicorn es un servidor web ASGI (interfaz de puerta de enlace de servidor asíncrono)
    import uvicorn

    # utilizamos la clase FastApi
    from fastapi import FastAPI, Path

    from typing import Annotated

    #
    from pydantic import BaseModel

except Exception as e:
    print(f'Falta algun modulo en Ejemplo_00 --> {e}')

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# creamos una instancia de la clase  FastApi
app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


@app.put("/items/{item_id}")
async def update_item(item_id: Annotated[int, Path(title="The ID to get", ge=0, le=1000)], q: str | None = None, item: Item | None = None, ):
    """

    item_id:        Es un parametro requerido de tipo integer con validacion entre minimos y maximos valores
    q:              Es un parametro no requerido de tipo string o None con un valor de default None
    item:           Es un parametro no requerido de tipo objeto o None con un valor de default None

    """

    # asigna  un diccionario
    results = {"item_id": item_id}

    # evalua el valor de q
    if q:
        results.update({"q": q})        # actualiza el diccionario

    # evalua el parametro item
    if item:
        results.update({"item": item})  # actualiza el diccionario

    return results


# Llamamos al servidor para que inicie
if __name__ ==  "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
