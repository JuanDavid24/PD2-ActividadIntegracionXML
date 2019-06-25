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
        print("Ingrese ID del cliente: ")
        clienteID = input()

        if self.bd.existeCliente(clienteID):
            listaCuentas = self.bd.getListaCuentasDelTitular(clienteID)
            print("\nID del cliente: " + clienteID)

            if listaCuentas == []:
                print("\nEl cliente no posee cuentas")
            else:
                for c in listaCuentas:
                    self.printCuenta(c)
        else:
            print("\nEl cliente no existe en la base de datos!")

    def printCuenta(self, cuenta):
        print("Cuenta id: " + cuenta['id'] + "\n \t Balance: " + cuenta['balance'])

    def __init__(self, bd):
        self.bd = bd
        self.key = ''
        self.keySwitcher = {"1": self.verListaCuentas,
                            "2": self.verCuentasTitular,
                            "q": quit}
