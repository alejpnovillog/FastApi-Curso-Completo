# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# CONTROLAMOS LAS LIBRERIA QUE IMPORTAMOS
# DOCUMENTACION LINK https://fastapi.tiangolo.com/tutorial/request-forms-and-files/
try:

    #  UVICORN ES UN SERVIDOR WEB ASGI (interfaz de puerta de enlace de servidor asíncrono)
    import uvicorn

    # UTILIZAMOS LA CLASE FASTAPI
    from fastapi import FastAPI, File, Form, UploadFile

    # 
    from typing import Annotated

except Exception as e:
    print(f'Falta algun modulo en solicitarFormularioArchivo --> {e}')

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# CREAMOS UNA INSTANCIA DE LA CLASE FastApi
app = FastAPI()


@app.post("/files/")
async def create_file(file: Annotated[bytes, File()], fileb: Annotated[UploadFile, File()], token: Annotated[str, Form()],):
    """

    Args:
        file (Annotated[bytes, File):       Parametro para recibir un archivo pequeño 
        fileb (Annotated[UploadFile, File): Paremetro para poder levantar un archivo
        token (Annotated[str, Form):        Parametro para recibir un atributo del formulario

    Returns:
        _type_:         Retornamos un diccionario con los datos del formulario y archivos
    """
    return {
        "file_size": len(file),
        "token": token,
        "fileb_content_type": fileb.content_type,
    }


# LLAMAMOS AL SERVIDOR PARA QUE INICIE
if __name__ ==  "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
