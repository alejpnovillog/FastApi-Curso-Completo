# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# CONTOLAMOS LAS LIBRERIAS QUE IMPORTAMOS
try:

    #  UVICORN ES UN SERVIDOR WEB ASGI (interfaz de puerta de enlace de servidor asíncrono)
    import uvicorn

    # utilizamos la clase FastApi
    from fastapi import FastAPI

    #
    from pydantic import BaseModel

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
async def update_item(item_id: int, item: Item, user: User):
    """

    item_id:        Es un parametro requerido de tipo integer
    item:           Es un parametro requerido de tipo objeto Item para el body
    user:           Es un parametro requerido de tipo objeto User para el body

    """

    # asignamos un diccinario
    results = {"item_id": item_id, "item": item, "user": user}

    return results


# Llamamos al servidor para que inicie
if __name__ ==  "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
