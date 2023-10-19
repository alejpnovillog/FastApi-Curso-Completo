# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# CONTROLAMOS LAS LIBRERIA QUE IMPORTAMOS
try:

    #  UVICORN ES UN SERVIDOR WEB ASGI (interfaz de puerta de enlace de servidor asíncrono)
    import uvicorn

    # UTILIZAMOS LA CLASE FASTAPI
    from fastapi import FastAPI

    # LIBRERIA DE MODELOS DE VALIDACIÓN DE DATOS ENVIADOS O RECIBIDOS
    from pydantic import BaseModel
    
    # LIBRERIA UTILIZADA PARA DETERMINAR EL TIPADO ESTATICO
    from typing import Union

except Exception as e:
    print(f'Falta algun modulo en union --> {e}')

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# CREAMOS UNA INSTANCIA DE LA CLASE FastApi
app = FastAPI()



# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# DEFINIMOS UN MODELO DE VALIDACIÓN DE DATOS EN EL BODY
class BaseItem(BaseModel):
    description: str
    type: str


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# DEFINIMOS UN MODELO DE VALIDACIÓN DE DATOS EN EL BODY (es una subclase de BaseItem)
# DONDE REESCRIBIMOS EL ATRIBUTO type CON UN VALOR POR DEFAULT
class CarItem(BaseItem):
    """

    Args:
        BaseItem (_type_):  El parametro hereda de la clase BaseItem
    """
    
    # ATRIBUTO DE TIPO STRING CON UN VALOR POR DEFAULT
    type: str = "car"



# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# DEFINIMOS UN MODELO DE VALIDACIÓN DE DATOS EN EL BODY (es una subclase de BaseItem)
# DONDE REESCRIBIMOS EL ATRIBUTO type CON UN VALOR POR DEFAULT
class PlaneItem(BaseItem):
    """

    Args:
        BaseItem (_type_):  El parametro hereda de la clase BaseItem
    """

    # ATRIBUTO DE TIPO STRING CON UN VALOR POR DEFAULT    
    type: str = "plane"
    
    size: int



# ASIGNAMOS UN DICCIONARIO
items = {
    "item1": {"description": "All my friends drive a low rider", "type": "car"},
    "item2": {
        "description": "Music is my aeroplane, it's my aeroplane",
        "type": "plane",
        "size": 5,
    },
}




# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# EN ESTA OPERACION DE RUTA
@app.get("/items/{item_id}", response_model=Union[PlaneItem, CarItem])
async def read_item(item_id: str):
    """_summary_

    Args:
        item_id (str):      El parametro es de tipo string 

    Returns:
        _type_:             Retornamos el elemento del diccionario items 
                            response_model determina que puede devolver un modelo de
                            tipo PlanetItem o CarItem
        

    """
    return items[item_id]
