# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# controlamos las librerias que importamos
try:

    #  Uvicorn es un servidor web ASGI (interfaz de puerta de enlace de servidor asíncrono)
    import uvicorn

    # la clase Union define que un atributo tiene dos opciones de valor
    from typing import Union

    # utilizamos la clase FastApi
    from fastapi import FastAPI


except Exception as e:
    print(f'Falta algun modulo en Ejemplo_00 --> {e}')

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# creamos una instancia de la clase  FastApi
app = FastAPI()


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# En esta operacion de ruta
# Un ejemplo de la invocacion de la url
# http://127.0.0.1:8000/items/foo-item?needy=sooooneedy
# devuelve { "item_id": "foo-item", "needy": "sooooneedy" }
@app.get("/items/{item_id}")
async def read_user_item(item_id: str, needy: str, skip: int = 0, limit: Union[int, None] = None):
    """
    item_id:        Tipo str y es requerido
    needy:          needy str y es requerido
    skip:           skip no requrido con un valor por default
    limit:          limit no requerido con un valor por default

    """

    # asignamos a item un diccionario
    item = {"item_id": item_id, "needy": needy, "skip": skip, "limit": limit}
    return item
