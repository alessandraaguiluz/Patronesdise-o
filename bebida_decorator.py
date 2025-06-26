class Bebida:
    def calcular_precio(self):
        print("[Base] Café solo: $1.00")
        return 1.00


class DecoradorBebida:
    def __init__(self, bebida):
        self.bebida = bebida


class LecheDescremada(DecoradorBebida):
    def calcular_precio(self):
        base = self.bebida.calcular_precio()
        print("[Leche descremada] +$0.50")
        return base + 0.50


class Canela(DecoradorBebida):
    def calcular_precio(self):
        base = self.bebida.calcular_precio()
        print("[Canela] +$0.25")
        return base + 0.25


class CremaBatida(DecoradorBebida):
    def calcular_precio(self):
        base = self.bebida.calcular_precio()
        print("[Crema batida] +$1.50")
        return base + 1.50


class Saborizante(DecoradorBebida):
    def calcular_precio(self):
        base = self.bebida.calcular_precio()
        print("[Saborizante] +$1.25")
        return base + 1.25


class BebidaGrande(DecoradorBebida):
    def calcular_precio(self):
        base = self.bebida.calcular_precio()
        print("[Tamaño grande] +$2.00")
        return base + 2.00


if __name__ == "__main__":
    bebida = Bebida()
    bebida = LecheDescremada(bebida)
    bebida = Canela(bebida)
    bebida = CremaBatida(bebida)
    bebida = Saborizante(bebida)
    bebida = Saborizante(bebida)  
    bebida = BebidaGrande(bebida)

    total = bebida.calcular_precio()
    print(f"\nPrecio total: ${total:.2f}")
