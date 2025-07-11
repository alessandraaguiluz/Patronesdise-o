import json
from abc import ABC, abstractmethod


class ProcesadorPago(ABC):
    @abstractmethod
    def procesar_pago(self, json_data):
        pass


class PagoModerno(ProcesadorPago):
    def procesar_pago(self, json_data):
        datos = json.loads(json_data)
        print(f"[MODERNO] Procesando pago de {datos['amount']} {datos['currency']} para usuario {datos['user_id']}")


class ServicioPagoLegacy:
    def pagar(self, datos_legacy):
        print(f"[LEGACY] Procesando pago para cliente {datos_legacy['cliente']} por {datos_legacy['monto_total']} {datos_legacy['moneda']}")


class PagoAdapter(ProcesadorPago):
    def __init__(self, servicio_legacy):
        self.servicio = servicio_legacy

    def procesar_pago(self, json_data):
        print(f"[JSON moderno recibido] {json.loads(json_data)}")

        datos = json.loads(json_data)
        datos_legacy = {
            "cliente": datos["user_id"],
            "monto_total": datos["amount"],
            "moneda": datos["currency"]
        }

        print(f"[Adaptado a legacy] {datos_legacy}")
        self.servicio.pagar(datos_legacy)


if __name__ == "__main__":
    json_input = json.dumps({
        "user_id": "u123",
        "amount": 250.0,
        "currency": "USD"
    })

    print("\n--- Uso de clase moderna ---")
    moderno = PagoModerno()
    moderno.procesar_pago(json_input)

    print("\n--- Uso de clase legacy con adaptador ---")
    legacy = ServicioPagoLegacy()
    adaptador = PagoAdapter(legacy)
    adaptador.procesar_pago(json_input)
