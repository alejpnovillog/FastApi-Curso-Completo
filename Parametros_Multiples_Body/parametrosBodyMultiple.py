# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# CONTOLAMOS LAS LIBRERIAS QUE IMPORTAMOS
try:

    #  UVICORN ES UN SERVIDOR WEB ASGI (interfaz de puerta de enlace de servidor asíncrono)
    import uvicorn

    # UTILIZAMOS LA CLASE FASTAPI
    from fastapi import FastAPI

    # LIBRERIA DE MODELOS DE VALIDACION DE DATOS ENVIADOS O RECIBIDOS 
    from pydantic import BaseModel

except Exception as e:
    print(f'Falta algun modulo en Ejemplo_00 --> {e}')

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# CREAMOS UNA INSTANCIA DE LA CLASE FastApi
app = FastAPI()


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# DEFINIMOS UN MIDELO DE VALIDACION DE DATOS EN EL BODY
# LOS ATRIBUTOS NO REQUERIDOS SON
#   description, tax
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# DEFINIMOS UN MIDELO DE VALIDACION DE DATOS EN EL BODY
# LOS ATRIBUTOS NO REQUERIDOS SON
#   full_name
class User(BaseModel):
    username: str
    full_name: str | None = None


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# EN ESTA OPERACION DE RUTA
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


# LLAMAMOS AL SERVIDOR PARA QUE INICIE
if __name__ ==  "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
