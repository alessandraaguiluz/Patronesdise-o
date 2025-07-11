class Orden:
    def __init__(self):
        self.usuario = None
        self.productos = []
        self.direccion = None
        self.metodo_pago = None
        self.descuento = 0
        self.total = 0.0

    def __str__(self):
        productos_str = ', '.join([f"{nombre} (${precio})" for nombre, precio in self.productos])
        return (
            f"Orden de: {self.usuario}\n"
            f"Productos: {productos_str}\n"
            f"Direccion: {self.direccion}\n"
            f"Pago: {self.metodo_pago}\n"
            f"Descuento: {self.descuento}%\n"
            f"Total a pagar: ${self.total}"
        )


class OrdenBuilder:
    def __init__(self):
        self.orden = Orden()

    def set_usuario(self, nombre):
        self.orden.usuario = nombre
        return self

    def agregar_producto(self, nombre, precio):
        self.orden.productos.append((nombre, precio))
        return self

    def set_direccion(self, direccion):
        self.orden.direccion = direccion
        return self

    def set_metodo_pago(self, metodo):
        self.orden.metodo_pago = metodo
        return self

    def set_descuento(self, porcentaje):
        self.orden.descuento = porcentaje
        return self

    def build(self):
        return self.orden


class CalculadorDeTotal:
    def calcular(self, orden):
        subtotal = sum(precio for _, precio in orden.productos)
        descuento = subtotal * (orden.descuento / 100)
        total = subtotal - descuento
        return round(total, 2)


# Ejemplo de uso
if __name__ == "__main__":
    builder = OrdenBuilder()
    orden = (
        builder.set_usuario("Juan Perez")
        .agregar_producto("Laptop", 1200)
        .agregar_producto("Mouse", 50)
        .set_direccion("Av. Siempre Viva 742")
        .set_metodo_pago("Tarjeta de credito")
        .set_descuento(10)  # 10%
        .build()
    )

    calculador = CalculadorDeTotal()
    orden.total = calculador.calcular(orden)

    print(orden)
