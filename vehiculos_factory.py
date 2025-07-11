from abc import ABC, abstractmethod

class Vehiculo(ABC):
    @abstractmethod
    def crear(self):
        pass

class Motor(ABC):
    @abstractmethod
    def usar(self):
        pass

class Carro(Vehiculo):
    def crear(self):
        print("Creando vehiculo terrestre: Carro")

class MotorCombustion(Motor):
    def usar(self):
        print("Usando motor: Motor de combustion")

class Lancha(Vehiculo):
    def crear(self):
        print("Creando vehiculo acuatico: Lancha")

class MotorNautico(Motor):
    def usar(self):
        print("Usando motor: Motor nautico")

# Abstract Factory
class VehiculoFactory(ABC):
    @abstractmethod
    def crear_vehiculo(self) -> Vehiculo:
        pass

    @abstractmethod
    def crear_motor(self) -> Motor:
        pass

class FabricaTerrestre(VehiculoFactory):
    def crear_vehiculo(self):
        return Carro()

    def crear_motor(self):
        return MotorCombustion()

class FabricaAcuatica(VehiculoFactory):
    def crear_vehiculo(self):
        return Lancha()

    def crear_motor(self):
        return MotorNautico()

def renderizar_vehiculo(fabrica: VehiculoFactory):
    vehiculo = fabrica.crear_vehiculo()
    motor = fabrica.crear_motor()
    vehiculo.crear()
    motor.usar()

# Uso
if __name__ == "__main__":
    renderizar_vehiculo(FabricaTerrestre())
    print()
    renderizar_vehiculo(FabricaAcuatica())
