"""
    creamos un  config.py con el siguiente contenido

    from pydantic_settings import BaseSettings


    class Settings(BaseSettings):
        app_name: str = "Awesome API"
        admin_email: str
        items_per_user: int = 50

"""


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# controlamos las librerias que importamos
try:

    #  Uvicorn es un servidor web ASGI (interfaz de puerta de enlace de servidor asíncrono)
    import uvicorn

    from functools import lru_cache
    from typing import Annotated

    # utilizamos la clase FastApi
    from fastapi import Depends, FastAPI

    # obtenemos la clase settings del archivo config.py
    from .config import Settings


except Exception as e:
    print(f'Falta algun modulo en Ejemplo_00 --> {e}')


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# creamos una instancia de la clase  FastApi
app = FastAPI()

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# permite guardar en cache los resultados de la funcion get_settings
@lru_cache()
def get_settings():
    return Settings()


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# En esta operacion de ruta
# el  parametro settings es de tipo Settings que es una clase o el valor obtenido de la funcion get_settings
# el parametro hereda los atributos app_name, admin_email, items_per_user
@app.get("/info")
async def info(settings: Annotated[Settings, Depends(get_settings)]):
    return {
        "app_name": settings.app_name,
        "admin_email": settings.admin_email,
        "items_per_user": settings.items_per_user,
    }

# Llamamos al servidor para que inicie
if __name__ ==  "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, ADMIN_EMAIL="deadpool@example.com", APP_NAME="Chimichangapp")
