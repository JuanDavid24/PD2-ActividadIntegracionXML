class Menu (object):
    def mostrarMenu(self):
        print("\nIngresar opcion:\n"
                "\t1 - Ver listado de cuentas \n"
                "\t2 - Ver cuentas por titular \n"
                "\tq - salir \n")
        key = input()
        self.procesarOpcion(key)

    def procesarOpcion(self, key):
        item = self.keySwitcher.get(key)
        if callable(item):
            return item()

    def verListaCuentas(self):
        self.bd.printCuentas()

    def verCuentasTitular(self):
        print ("Ingrese ID del cliente: ")
        clienteID = input()
        self.bd.printCuentasTitular(clienteID)

    def __init__(self, bd):
        self.bd = bd
        self.key = ''
        self.keySwitcher = {"1": self.verListaCuentas,
                            "2": self.verCuentasTitular,
                            "q": quit}
