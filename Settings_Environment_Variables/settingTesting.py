# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# controlamos las librerias que importamos
try:

    #  Uvicorn es un servidor web ASGI (interfaz de puerta de enlace de servidor asíncrono)
    import uvicorn

    # obtenemos la clase settings del archivo config.py
    from .config import Settings

    from fastapi.testclient import TestClient

    from .main import app, get_settings

except Exception as e:
    print(f'Falta algun modulo en Ejemplo_00 --> {e}')


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# creamos una instancia de la clase  TestClient
client = TestClient(app)


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# definimos una funcion que sobreescribe un atributo de la clase
def get_settings_override():
    return Settings(admin_email="testing_admin@example.com")


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# asignamos la dependecy overrides de la funcion get_settings importada con el resultado de la funcion
# get_settings_override
app.dependency_overrides[get_settings] = get_settings_override


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# definimos una funcion para realizar el  test
def test_app():
    response = client.get("/info")
    data = response.json()
    assert data == {
        "app_name": "Awesome API",
        "admin_email": "testing_admin@example.com",
        "items_per_user": 50,
    }


