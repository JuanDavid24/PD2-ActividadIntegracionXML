from parser.parser import Parser
import pytest

p = Parser()

listaClientes = [{'id': 'c1', 'nombre': 'Ricardo Carotenuto', 'direccion': 'Gral Chamizo 50'},
                 {'id': 'c2', 'nombre': 'Trapito Paez', 'direccion': 'Ojo Pekin 670'},
                 {'id': 'c3', 'nombre': 'Luis Solari', 'direccion': 'Rodeo Drive 145'}]
listaCtasCtes = [{'id': 'a3', 'balance': '4025'},
           {'id': 'a4', 'balance': '-125'},
           {'id': 'a5', 'balance': '325'}]
listaCAhorro = [{'id': 'a1', 'interes': '0.03', 'balance': '2500'},
                {'id': 'a2', 'interes': '0.03', 'balance': '15075'}]
listaClientesCuentas = [{'c_id': 'c1', 'cu_id': 'a2'},
                        {'c_id': 'c1', 'cu_id': 'a3'},
                        {'c_id': 'c2', 'cu_id': 'a4'},
                        {'c_id': 'c3', 'cu_id': 'a1'},
                        {'c_id': 'c3', 'cu_id': 'a5'}]

@pytest.mark.parametrize('testInput,expected',[("p.clientes",listaClientes),
                                               ("p.cajasAhorro", listaCAhorro),
                                               ("p.ctasCtes", listaCtasCtes),
                                               ("p.clientesCuentas",listaClientesCuentas)])
def testLista(testInput,expected):
    assert eval(testInput) == expected