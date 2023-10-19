# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# CONTROLAMOS LAS LIBRERIA QUE IMPORTAMOS
try:

    #  UVICORN ES UN SERVIDOR WEB ASGI (interfaz de puerta de enlace de servidor asíncrono)
    import uvicorn

    # UTILIZAMOS LA CLASE FASTAPI
    from fastapi import FastAPI, Form

    # LIBRERIA DE MODELOS DE VALIDACIÓN DE DATOS ENVIADOS O RECIBIDOS
    from pydantic import BaseModel
    
    from typing import Annotated

except Exception as e:
    print(f'Falta algun modulo en Ejemplo_00 --> {e}')

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# CREAMOS UNA INSTANCIA DE LA CLASE FastApi
app = FastAPI()



# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# EN ESTA OPERACION DE RUTA
@app.post("/login/")
async def login(username: Annotated[str, Form()], password: Annotated[str, Form()]):
    """

    definimos el tipado Annotated[str, Form()] determina que puede utilizar cualquier opcion

    Args:
        username (Annotated[str, Form):     Es un parametro no requeridos para enviar a un formulario
        
        password (Annotated[str, Form):     Es un parametro no requeridos para enviar a un formulario

    Returns:
        _type_:                 Retornamos un diccionario
    """
    return {"username": username}


# LLAMAMOS AL SERVIDOR PARA QUE INICIE
if __name__ ==  "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
