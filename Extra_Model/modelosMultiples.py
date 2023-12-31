# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# CONTROLAMOS LAS LIBRERIA QUE IMPORTAMOS
try:

    #  UVICORN ES UN SERVIDOR WEB ASGI (interfaz de puerta de enlace de servidor asíncrono)
    import uvicorn

    # UTILIZAMOS LA CLASE FASTAPI
    from fastapi import FastAPI

    # LIBRERIA DE MODELOS DE VALIDACIÓN DE DATOS ENVIADOS O RECIBIDOS
    from pydantic import BaseModel, EmailStr

except Exception as e:
    print(f'Falta algun modulo en Ejemplo_00 --> {e}')

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# CREAMOS UNA INSTANCIA DE LA CLASE FastApi
app = FastAPI()


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# DEFINIMOS UN MODELO DE VALIDACIÓN DE DATOS EN EL BODY
# LOS ATRIBUTOS NO REQUERIDOS SON
#   full_name
class UserBase(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# DEFINIMOS UN MODELO DE VALIDACION DE DATOS EN EL BODY
class UserIn(UserBase):
    """

    Args:
        UserBase (_type_):  La clase hereda del modelo UserBase
    """
    
    password: str


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# DEFINIMOS UN MODELO DE VALIDACION DE DATOS EN EL BODY
class UserOut(UserBase):
    """

    Args:
        UserBase (_type_):  La clase hereda del modelo UserBase
                            Se la utiliza para responder con el contenido de la
                            clase UserBase
    """
    
    pass

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# DEFINIMOS UN MODELO DE VALIDACION DE DATOS EN EL BODY
class UserInDB(UserBase):
    """

    Args:
        UserBase (_type_):  La clase hereda del modelo UserBase
    """
    hashed_password: str

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# DEFINIMOS UNA FUNCION PARA RETORNAR UNA PASSWORD EN HASH
def fake_password_hasher(raw_password: str):
    """

    Args:
        raw_password (str):  El parametro es de tipo string

    Returns:
        _type_:             El valor retornado es el hash de la string pasdo por parametro
    """
    return "supersecret" + raw_password


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# DEFINIMOS UNA FUNCION QUE RETORNA EL HASH DE LA PASSWORD ENVIADA EN UN MODELO DE VALIDACION
def fake_save_user(user_in: UserIn):
    """

    Args:
        user_in (UserIn):   El parametro es de tipo del modelo de validacion UserIn

    Returns:
        _type_:             La instancia user_in_db
    """
    
    # OBTENEMOS EL HASH DEL STRING QUE LE PASAMOS COMO PARAMETRO
    hashed_password = fake_password_hasher(user_in.password)
    
    # ASIGNAMOS UNA INSTANCIA DE LA CLASE UserInDb PASANDOLE COMO  PARAMETRO
    # EL MODELO UserIn COMO DICCIONARIO Y PASANDOLE EL VALOR DEL ATRIBUTO
    # DE LA CLASE UserInDb
    user_in_db = UserInDB(**user_in.dict(), hashed_password=hashed_password)
    
    
    print("User saved! ..not really")
    return user_in_db


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# EN ESTA OPERACION DE RUTA
@app.post("/user/", response_model=UserOut)
async def create_user(user_in: UserIn):
    """

    Args:
        user_in (UserIn):          El parametro es de tipo del modelo de validacion UserIn

    Returns:
        _type_: _description_
        
    """
    
    # RETORNAMOS LA INSTANCIA DE LA CLASE UserInDb
    user_saved = fake_save_user(user_in)
    
    return user_saved




# LLAMAMOS AL SERVIDOR PARA QUE INICIE
if __name__ ==  "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
