from parser.parser import Parser
from BD import BD
from menu import Menu


def main():
    p = Parser()
    bd = BD()
    m = Menu(bd)

    print("\nCajas de ahorro: \n" + str(p.cajasAhorro))
    print("\nC. Corrientes: \n" + str(p.ctasCtes))
    print("\nClientes: \n" + str(p.clientes))
    print("\nClientes-cuentas: \n" + str(p.clientesCuentas))

    bd.guardarListaEnHashBD(p.cajasAhorro)
    bd.guardarListaEnHashBD(p.ctasCtes)
    bd.guardarListaEnHashBD(p.clientes)
    bd.guardarListaEnHashBD(p.clientesCuentas)

    while True:
        opcion = m.mostrarMenu()


    #exec("verListaCuentas(bd)")

    #print (r.hgetall('c2'))
    #print (r.hgetall('c3a5'))



if __name__ == "__main__":
    main()