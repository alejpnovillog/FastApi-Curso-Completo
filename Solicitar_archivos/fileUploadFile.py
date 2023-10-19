# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# CONTROLAMOS LAS LIBRERIA QUE IMPORTAMOS
# DOCUMENTACION EN EL LINK https://fastapi.tiangolo.com/tutorial/request-files/
try:

    #  UVICORN ES UN SERVIDOR WEB ASGI (interfaz de puerta de enlace de servidor asíncrono)
    import uvicorn

    # UTILIZAMOS LA CLASE FASTAPI
    from fastapi import FastAPI, File, UploadFile

    from typing import Annotated    

except Exception as e:
    print(f'Falta algun modulo en Ejemplo_00 --> {e}')

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# CREAMOS UNA INSTANCIA DE LA CLASE FastApi
app = FastAPI()


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# EN ESTA OPERACION DE RUTA PARA EL TRATAMIENTO DE ARCHIVOS
@app.post("/files/")
async def create_file(file: Annotated[bytes, File()]):
    """

    Args:
        file (Annotated[bytes, File):  El parametro es de tipo bytes o tipo File()
                                       hereda de la clase Form(). Al utilizar File() declara el parametro
                                       como cuerpo de archivo como dato de formulario 
                                        

    Returns:
        _type_:         Retorna un diccionario
    """    
    return {"file_size": len(file)}


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# EN ESTA OPERACION DE RUTA PARA EL TRATAMIENTO PARA SUBIR ARCHIVOS
@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    """

    Args:
        file (UploadFile):          El parametro es de tipo UploadFile para no utilizar el tipo bytes
                                    Es conveniente porque no tiene limites de el espacio que ocupa el file

    Returns:
        _type_:                     Retorna un diccionario
    """    
    return {"filename": file.filename}


# LLAMAMOS AL SERVIDOR PARA QUE INICIE
if __name__ ==  "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
