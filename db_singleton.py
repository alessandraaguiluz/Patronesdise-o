class DatabaseConnection:
    _instance = None
    _connected = False
    _connection_count = 0

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
        return cls._instance

    def conectar(self):
        if not self._connected:
            print("Conectando a la base de datos...")
            self._connected = True
            DatabaseConnection._connection_count = 1
        else:
            print("Ya existe una conexion activa.")

    def desconectar(self):
        if self._connected:
            print("Conexion cerrada.")
            self._connected = False
            DatabaseConnection._connection_count = 0
        else:
            print("No hay conexion activa.")

    def conexiones_abiertas(self):
        print(f"Conexiones abiertas: {DatabaseConnection._connection_count}")


# Ejemplo de uso
if __name__ == "__main__":
    db1 = DatabaseConnection()
    db2 = DatabaseConnection()

    db1.conectar()
    db2.conectar()

    db1.desconectar()

    db2.conexiones_abiertas()
