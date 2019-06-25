from parser.parser import Parser
from BD import BD
from menu import Menu


def main():
    p = Parser()
    bd = BD()
    m = Menu(bd)
    '''
    print("\nCajas de ahorro: \n" + str(p.cajasAhorro))
    print("\nC. Corrientes: \n" + str(p.ctasCtes))
    print("\nClientes: \n" + str(p.clientes))
    print("\nClientes-cuentas: \n" + str(p.clientesCuentas))
    '''
    bd.guardarListaEnHashBD(p.cajasAhorro)
    bd.guardarListaEnHashBD(p.ctasCtes)
    bd.guardarListaEnHashBD(p.clientes)
    bd.guardarListaClientesCuentasEnHashBD(p.clientesCuentas)

    while True:
        m.mostrarMenu()

if __name__ == "__main__":
    main()