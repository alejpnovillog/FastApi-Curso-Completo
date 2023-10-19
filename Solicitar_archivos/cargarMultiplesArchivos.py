# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# CONTROLAMOS LAS LIBRERIA QUE IMPORTAMOS
# DOCUMENTACION EN EL LINK https://fastapi.tiangolo.com/tutorial/request-files/
try:

    #  UVICORN ES UN SERVIDOR WEB ASGI (interfaz de puerta de enlace de servidor asíncrono)
    import uvicorn

    # UTILIZAMOS LA CLASE FASTAPI
    from fastapi import FastAPI, File, UploadFile
    from fastapi.responses import HTMLResponse

    from typing import Annotated    

except Exception as e:
    print(f'Falta algun modulo en Ejemplo_00 --> {e}')

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# CREAMOS UNA INSTANCIA DE LA CLASE FastApi
app = FastAPI()


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# EN ESTA OPERACION DE RUTA PARA EL TRATAMIENTO DE ARCHIVOS
@app.post("/files/")
async def create_files(files: Annotated[list[bytes], File()]):
    """

    Args:
        files (Annotated[list[bytes], File):    El parametro es de tipo lista de bytes y tipo File() lo que permite
                                                cargar varios archivos pequeños 

    Returns:
        _type_:                                 Retornamos un diccionario con la lista de los archivos recibidos
    """    """"""
    return {"file_sizes": [len(file) for file in files]}


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# EN ESTA OPERACION DE RUTA PARA EL TRATAMIENTO PARA SUBIR ARCHIVOS
@app.post("/uploadfiles/")
async def create_upload_files(files: list[UploadFile]):
    """

    Args:
        files (list[UploadFile]):   El parametro es una lista de tipo UploadFile_

    Returns:
        _type_:                     Retornamos un diccionario con la lista de los archivos recibidos
    """
    return {"filenames": [file.filename for file in files]}


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# EN ESTA OPERACION DE RUTA PARA OBTENER EN UN HTML LAS DISTINTAS FORMAS DE CARGAR ARCHIVOS
@app.get("/")
async def main():
    content = """
<body>
<form action="/files/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
<form action="/uploadfiles/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
</body>
    """
    return HTMLResponse(content=content)


# LLAMAMOS AL SERVIDOR PARA QUE INICIE
if __name__ ==  "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
