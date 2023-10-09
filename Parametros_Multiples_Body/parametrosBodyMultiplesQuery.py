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
# definimos un modelo de validacion de datos en el body
# los atributos no requeridos son
#   full_name
class User(BaseModel):
    username: str
    full_name: str | None = None


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# En esta operacion de ruta
@app.put("/items/{item_id}")
async def update_item(*, item_id: int, item: Item, user: User, importance: Annotated[int, Body(gt=0)], q: str | None = None, ):
    """

    *:              Es un valor que indica que los parametros siguientes son de tipo clave-valor como es el diccionario
    item_id:        Es un parametro requerido de tipo integer
    item:           Es un parametro requerido de tipo objeto Item para el body
    user:           Es un parametro requerido de tipo objeto User para el body
    importance:     Es un parametro requerido de tipo integer y es otra clave en el body con un valor mayor que cero
    q:              Es un parametro no requerido de tipo string o None con valor por default es None

    """

    # asignamos un diccionario
    results = {"item_id": item_id, "item": item, "user": user, "importance": importance}

    # evaluamos a q
    if q:
        results.update({"q": q})        # actualizamos el diccionario


    return results
