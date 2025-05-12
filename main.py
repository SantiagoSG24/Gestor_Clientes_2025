# main.py

class Cliente:
    def __init__(self, nombre, apellido, dni):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni

    def __str__(self):
        return f"{self.nombre} {self.apellido} - DNI: {self.dni}"


class GestorClientes:
    def __init__(self):
        self.clientes = []

    def listar_clientes(self):
        if not self.clientes:
            print("No hay clientes registrados.")
        else:
            for cliente in self.clientes:
                print(cliente)

    def consultar_cliente(self, dni):
        for cliente in self.clientes:
            if cliente.dni == dni:
                print(cliente)
                return
        print("Cliente no encontrado.")

    def agregar_cliente(self, nombre, apellido, dni):
        if any(cliente.dni == dni for cliente in self.clientes):
            print("Ya existe un cliente con ese DNI.")
        else:
            self.clientes.append(Cliente(nombre, apellido, dni))
            print("Cliente agregado correctamente.")

    def modificar_cliente(self, dni, nuevo_nombre, nuevo_apellido):
        for cliente in self.clientes:
            if cliente.dni == dni:
                cliente.nombre = nuevo_nombre
                cliente.apellido = nuevo_apellido
                print("Cliente modificado correctamente.")
                return
        print("Cliente no encontrado.")

    def borrar_cliente(self, dni):
        for cliente in self.clientes:
            if cliente.dni == dni:
                self.clientes.remove(cliente)
                print("Cliente eliminado correctamente.")
                return
        print("Cliente no encontrado.")


def menu():
    gestor = GestorClientes()

    # Clientes de prueba iniciales
    gestor.agregar_cliente("Juan", "Pérez", "12345678A")
    gestor.agregar_cliente("María", "Gómez", "87654321B")

    while True:
        print("\nGestor de Clientes")
        print("1. Listar clientes")
        print("2. Consultar cliente")
        print("3. Agregar cliente")
        print("4. Modificar cliente")
        print("5. Borrar cliente")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            gestor.listar_clientes()
        elif opcion == "2":
            dni = input("Ingrese el DNI del cliente: ")
            gestor.consultar_cliente(dni)
        elif opcion == "3":
            nombre = input("Ingrese el nombre: ")
            apellido = input("Ingrese el apellido: ")
            dni = input("Ingrese el DNI: ")
            gestor.agregar_cliente(nombre, apellido, dni)
        elif opcion == "4":
            dni = input("Ingrese el DNI del cliente a modificar: ")
            nuevo_nombre = input("Ingrese el nuevo nombre: ")
            nuevo_apellido = input("Ingrese el nuevo apellido: ")
            gestor.modificar_cliente(dni, nuevo_nombre, nuevo_apellido)
        elif opcion == "5":
            dni = input("Ingrese el DNI del cliente a borrar: ")
            gestor.borrar_cliente(dni)
        elif opcion == "6":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    menu()