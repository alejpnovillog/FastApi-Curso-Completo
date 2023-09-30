# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# controlamos las librerias que importamos
try:
    #  Uvicorn es un servidor web ASGI (interfaz de puerta de enlace de servidor asíncrono)
    import uvicorn

    # Union indica que el valor puede tener dos alternativas
    from typing import Union

    # status es un modulo
    # FastApi es una clase
    # Body es un metodo
    from fastapi import Body, FastAPI, status

    # Es una subclase de Response que retorna informacion en formato JSON
    from fastapi.responses import JSONResponse

except Exception as e:
    print(f'Falta algun modulo en Ejemplo_00 --> {e}')

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# creamos una instancia de la clase  FastApi
app = FastAPI()

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# simulamos el acceso a una base de datos con 2 registros
# primer  registro foo
# segundo registro bar
items = {"foo": {"name": "Fighters", "size": 6}, "bar": {"name": "Tenders", "size": 3}}

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# En esta operacion de ruta se recibe un parametro
# item_id  es un parametro de tipo string
# name es una opcion una string o un None. Su valor es un Boby = Son valores que se pasan en el body en formato Json con valor None por default
# size es una opcion una integer o un None. Su valor es un Boby = Son valores que se pasan en el body  en formato Json con valor None por default
# la definicion async def me permite procesar la operacion de ruta en forma async con el beneficio de poder recibir
# mas peticiones concurrentes
@app.put("/items/{item_id}")
async def upsert_item( item_id: str, name: Union[str, None] = Body(default=None), size: Union[int, None] = Body(default=None), ):
    """
    Recibimos los parametros para actualizar la base de datos de items

    **item_id**: es el item **obligatorio** tipo **str**, que vamos a buscar en la base de datos items

    **name**:    es el name del registro tipo **str**. Se ingresa en el **body** con formato json

    **size**:    es el size del registro tipo **int**. Se ingresa en el **body** con formato json

    **return**   Puede retornar un **item** o un **JSONResponse**

    """

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # verificamos si el item_id esta dentro del diccionario recibido de la base de datos
    if item_id in items:

        item = items[item_id]   # asignamos el valor del registro
        item["name"] = name     # asignamos el valor del name
        item["size"] = size     # asignamos el valor del size
        return item             # retornamos el valor del item
    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # si no lo encontramos el item_id dentro de items
    else:

        item = {"name": name, "size": size}     # generamos un nuevo registro
        items[item_id] = item                   # actualizamos la base de datos
        return JSONResponse(status_code=status.HTTP_201_CREATED, content=item)  # retornamos un nuevo codigo


# Llamamos al servidor para que inicie
if __name__ ==  "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
