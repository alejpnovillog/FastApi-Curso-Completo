"""
    Definimos la estructura de los directorios para el manejo de Bases de Datos
    .
    └── sql_app
        ├── __init__.py
        ├── crud.py
        ├── database.py
        ├── main.py
        ├── models.py
        ├── schemas.py
        └── tests
            ├── __init__.py
            └── test_sql_app.py
"""
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# controlamos las librerias que importamos
try:

    #  Uvicorn es un servidor web ASGI (interfaz de puerta de enlace de servidor asíncrono)
    import uvicorn

    from fastapi.testclient import TestClient
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy.pool import StaticPool

    from ..database import Base
    from ..main import app, get_db

except Exception as e:
    print(f'Falta algun modulo en Ejemplo_00 --> {e}')

# definimo la constante
SQLALCHEMY_DATABASE_URL = "sqlite://"

# definimos el engine del motor de base de datos
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)

# asignamos la session maker
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# asignamos la metadata de la clase para crear con el engine del motor de la base de datos
Base.metadata.create_all(bind=engine)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# definimos la funcion para obtener el motor de base de datos
def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

# asignamos la dependency con la funcion para obtener la base de datos
app.dependency_overrides[get_db] = override_get_db

# generamos una instancia de TestClient
client = TestClient(app)


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# definimos la funcion de test
def test_create_user():
    response = client.post(
        "/users/",
        json={"email": "deadpool@example.com", "password": "chimichangas4life"},
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["email"] == "deadpool@example.com"
    assert "id" in data
    user_id = data["id"]

    response = client.get(f"/users/{user_id}")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["email"] == "deadpool@example.com"
    assert data["id"] == user_id


# Llamamos al servidor para que inicie
if __name__ ==  "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
