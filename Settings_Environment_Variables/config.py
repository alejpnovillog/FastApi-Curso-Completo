# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# controlamos las librerias que importamos
try:

    from pydantic_settings import BaseSettings

except Exception as e:
    print(f'Falta algun modulo en Ejemplo_00 --> {e}')


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# definimos la clase Settings que hereda de BaseSettings lo que permite poder tomar los valores de las variables de
# entorno que pasamos desde la terminal
# ADMIN_EMAIL, APP_NAME la clase toma las variables independiente de que este en mayusculas
class Settings(BaseSettings):
    app_name: str = "Awesome API"
    admin_email: str
    items_per_user: int = 50
