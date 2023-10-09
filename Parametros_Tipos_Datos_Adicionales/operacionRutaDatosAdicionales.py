# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# controlamos las librerias que importamos
try:

    #  Uvicorn es un servidor web ASGI (interfaz de puerta de enlace de servidor asíncrono)
    import uvicorn

    # utilizamos la clase FastApi
    from fastapi import Body, FastAPI

    from datetime import datetime, time, timedelta
    from typing import Annotated
    from uuid import UUID

except Exception as e:
    print(f'Falta algun modulo en Ejemplo_00 --> {e}')

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# creamos una instancia de la clase  FastApi
app = FastAPI()


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# En esta operacion de ruta
@app.put("/items/{item_id}")
async def read_items(item_id: UUID, start_datetime: Annotated[datetime | None, Body()] = None,
                        end_datetime: Annotated[datetime | None, Body()] = None, repeat_at: Annotated[time | None, Body()] = None,
                        process_after: Annotated[timedelta | None, Body()] = None, ):
    """

    item_id:        Es un parametro requerido de tipo UUID
    start_datetime: Es un parametro de body de tipo datetime o None con valor de default None
    end_datetime:   Es un parametro de body de tipo datetime o None con valor de default None
    repeat_at:      Es un parametro de body de tipo time o None con valor de default None
    process_after:  Es un parametro de body de tipo timedelta o None con valor de default None

    """

    # asignamos la variable
    start_process = start_datetime + process_after

    # asignamos la variable
    duration = end_datetime - start_process


    return {
        "item_id": item_id, "start_datetime": start_datetime, "end_datetime": end_datetime, "repeat_at": repeat_at,
        "process_after": process_after, "start_process": start_process, "duration": duration,
    }

# Llamamos al servidor para que inicie
if __name__ ==  "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
