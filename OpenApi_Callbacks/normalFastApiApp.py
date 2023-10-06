# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# controlamos las librerias que importamos
try:

    #  Uvicorn es un servidor web ASGI (interfaz de puerta de enlace de servidor asíncrono)
    import uvicorn

    from typing import Union

    # utilizamos la clase FastApi
    from fastapi import APIRouter, FastAPI

    # Es una subclase de Response que retorna informacion en formato JSON
    from pydantic import BaseModel, HttpUrl

except Exception as e:
    print(f'Falta algun modulo en plainTextResponse --> {e}')

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# creamos una instancia de la clase  FastApi
app = FastAPI()


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# la clase invoce (factura) que utiliza pydantic
class Invoice(BaseModel):
    id: str
    title: Union[str, None] = None
    customer: str
    total: float


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# la clase (evento de la factura) que utiliza pydantic
class InvoiceEvent(BaseModel):
    description: str
    paid: bool


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# la clase (evento de la factura recivida) que utiliza pydantic
class InvoiceEventReceived(BaseModel):
    ok: bool


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# generamos una instancia de la clase ApiRouter
invoices_callback_router = APIRouter()


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# definimos una operacion de ruta
@invoices_callback_router.post("{$callback_url}/invoices/{$request.body.id}", response_model=InvoiceEventReceived)
def invoice_notification(body: InvoiceEvent):
    pass


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# definimos una operacion de ruta
@app.post("/invoices/", callbacks=invoices_callback_router.routes)
def create_invoice(invoice: Invoice, callback_url: Union[HttpUrl, None] = None):
    """
    Create an invoice.

    This will (let's imagine) let the API user (some external developer) create an
    invoice.

    And this path operation will:

    * Send the invoice to the client.
    * Collect the money from the client.
    * Send a notification back to the API user (the external developer), as a callback.
        * At this point is that the API will somehow send a POST request to the
            external API with the notification of the invoice event
            (e.g. "payment successful").
    """

    # Send the invoice, collect the money, send the notification (the callback)
    return {"msg": "Invoice received"}
