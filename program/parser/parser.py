import xml.dom.minidom as dom

class Parser(object):
    xmlFile = dom.parse("parser/banco.xml")

    #Listas de nodos:
    nodosCajasAhorro = (xmlFile.getElementsByTagName("caja_ahorro"))
    nodosCtasCtes = (xmlFile.getElementsByTagName("cuenta_corriente"))
    nodosClientes = (xmlFile.getElementsByTagName("cliente"))
    nodosClientesCuentas = (xmlFile.getElementsByTagName("cliente_cuenta"))

    def printListaNodos(self, listaNodos):
        for nodo in listaNodos:
            print(nodo.toprettyxml())

    #Recibe una lista de tags en formato Nodo de DOM.
    #Devuelve listas que tienen los atributos y elementos de cada nodo (ej: listas de atributos y elementos de todos los clientes)
    def parsearListaDeNodos(self, listaNodos):
        listaTotalAtributos = []     #lista de listas de tuplas
        listaTotalElementos = []     #lista de listas de tuplas
        for nodo in listaNodos:
            atributosDelNodo = []
            atributosDelNodo.append(nodo.attributes.items())    #lista de tuplas
            listaTotalAtributos += atributosDelNodo

            elementosDelNodo = []       #lista de tuplas
            for hijo in nodo.childNodes:
                if hijo.nodeType == dom.Node.ELEMENT_NODE:
                    elementosDelNodo.append((hijo.tagName, hijo.childNodes[0].data))
            listaTotalElementos.append(elementosDelNodo)

        return(listaTotalAtributos, listaTotalElementos)

    #Arma dict con los datos de un nodo (ej: un cliente, una caja de ahorro, etc)
    def armarDiccionario(self, listaAtributosNodo, listaElementosNodo):
        dict = {}
        for a in listaAtributosNodo:
            dict[a[0]] = a[1]
        for e in listaElementosNodo:
            dict[e[0]] = e[1]
        return dict

    #Lista de dicts (ej: lista con dicts de clientes)
    def armarListaDiccionarios(self, listaTotalAtributos, listaTotalElementos):
        listaDict = []
        for x in range(len(listaTotalAtributos)):
            listaDict.append(self.armarDiccionario(listaTotalAtributos[x], listaTotalElementos[x]))
        return listaDict


    def deListaDeNodosAListaDeDiccionarios(self, listaNodos):
        ATS, ELS = self.parsearListaDeNodos(listaNodos)
        listaDict = self.armarListaDiccionarios(ATS, ELS)
        return (listaDict)

    def __init__(self):
        self.cajasAhorro = self.deListaDeNodosAListaDeDiccionarios(self.nodosCajasAhorro)
        self.ctasCtes = self.deListaDeNodosAListaDeDiccionarios(self.nodosCtasCtes)
        self.clientes = self.deListaDeNodosAListaDeDiccionarios(self.nodosClientes)
        self.clientesCuentas = self.deListaDeNodosAListaDeDiccionarios(self.nodosClientesCuentas)

