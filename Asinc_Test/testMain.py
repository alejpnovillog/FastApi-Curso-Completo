"""
    Estructura de directorios de la aplicacion
    .
    ├── app
    ├── __init__.py
    ├── main.py
    └── test_main.py


    Programa main

    from fastapi import FastAPI

    app = FastAPI()


    @app.get("/")
    async def root():
        return {"message": "Tomato"}

"""

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# controlamos las librerias que importamos
try:

    #  Uvicorn es un servidor web ASGI (interfaz de puerta de enlace de servidor asíncrono)
    import uvicorn

    import pytest
    from httpx import AsyncClient

    from .main import app

except Exception as e:
    print(f'Falta algun modulo en Ejemplo_00 --> {e}')


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# decoredor para el test async
@pytest.mark.anyio
async def test_root():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Tomato"}


# Llamamos al servidor para que inicie
if __name__ ==  "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
