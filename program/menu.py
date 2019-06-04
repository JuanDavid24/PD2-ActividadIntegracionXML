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
        listaCuentas = self.bd.getListaCuentas()
        for c in listaCuentas:
            self.printCuenta(c)

    def verCuentasTitular(self):
        print ("Ingrese ID del cliente: ")
        clienteID = input()

        listaCuentas = self.bd.getListaCuentasDelTituar(clienteID)

        print("\nID del cliente: " + clienteID)
        for c in listaCuentas:
            self.printCuenta(c)

    def printCuenta(self, cuenta):
        print("Cuenta id: " + cuenta['id'] + "\n \t Balance: " + cuenta['balance'])

    def __init__(self, bd):
        self.bd = bd
        self.key = ''
        self.keySwitcher = {"1": self.verListaCuentas,
                            "2": self.verCuentasTitular,
                            "q": quit}
