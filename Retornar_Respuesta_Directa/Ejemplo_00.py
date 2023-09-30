# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# controlamos las librerias que importamos
try:

    # datetime es una clase del modulo datetime
    from datetime import datetime

    # Union indica que el valor puede tener dos alternativas
    from typing import Union

    # utilizamos la clase FastApi
    from fastapi import FastAPI

    # Es una funcion para convertir un objeto en formato JSON
    from fastapi.encoders import jsonable_encoder

    # Es una subclase de Response que retorna informacion en formato JSON
    from fastapi.responses import JSONResponse

    # Esta clase se utiliza para crear modelos de datos que se pueden validar y convertir en JSON
    from pydantic import BaseModel

except Exception as e:
    print(f'Falta algun modulo en Ejemplo_00 --> {e}')



# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# definimos la clase para tratar el modelo Item a validar
class Item(BaseModel):
    title: str
    timestamp: datetime
    description: Union[str, None] = None


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# creamos una instancia de la clase  FastApi
app = FastAPI()


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# En esta operacion de ruta se recibe un parametro
# id  es un parametro de tipo string
# item es valor de tipo Item
# la definicion async def me permite procesar la operacion de ruta en forma async con el beneficio de poder recibir
# mas peticiones concurrentes
@app.put("/items/{id}")
def update_item( id: str, item: Item):
    """
    Recibimos los parametros para actualizar

    **id**      es el id **obligatorio** tipo **str**

    **item**    es el item de tipo **Item** (objeto de modelo)

    **return**   Puede retornar un **item** o un **JSONResponse**

    """
    json_compatible_item_data = jsonable_encoder(item)          # convertimos el objeto item en formato JSON
    return JSONResponse(content=json_compatible_item_data)      # retornamos en contenido
