# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# controlamos las librerias que importamos
try:

    #  Uvicorn es un servidor web ASGI (interfaz de puerta de enlace de servidor asíncrono)
    import uvicorn

    # utilizamos la clase FastApi
    from fastapi import Body, FastAPI

    #
    from pydantic import BaseModel

    from typing import Annotated

except Exception as e:
    print(f'Falta algun modulo en Ejemplo_00 --> {e}')

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# creamos una instancia de la clase  FastApi
app = FastAPI()


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# definimos un modelo de validacion de datos en el body
# los atributos no requeridos son
#   description, tax
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# En esta operacion de ruta
@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Annotated[Item, Body(embed=True)]):
    """

    item_id:        Es un parametro requerido de tipo integer
    item:           Es un parametro de tipo objeto Item  embebido  en el body

    """

    # asignamos un diccionario
    results = {"item_id": item_id, "item": item}

    return results
