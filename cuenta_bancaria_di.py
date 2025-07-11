class Logger:
    def log(self, mensaje):
        print(f"[LOG] {mensaje}")


class EmailService:
    def enviar(self, mensaje):
        print(f"[EMAIL] Enviando email: {mensaje}")


class CuentaBancaria:
    def __init__(self, logger, email_service):
        self.logger = logger
        self.email_service = email_service

    def transferir(self, monto):
        self.logger.log(f"Se transfirieron ${monto}")
        self.email_service.enviar(f"Se transfirieron ${monto} a su cuenta")


# Uso del sistema con inyección de dependencias
if __name__ == "__main__":
    logger = Logger()
    email = EmailService()
    cuenta = CuentaBancaria(logger, email)

    cuenta.transferir(100)
