from BD import BD
import pytest
from parser.parser import Parser
import redis

listaCuentasC1 = [{'id': 'a2', 'interes': '0.03', 'balance': '15075'},
                  {'id': 'a3', 'balance': '4025'}]
listaCuentasC2 = [{'id': 'a4', 'balance': '-125'}]

#Creo la conexion con el server de redis que correra los tests en Travis
#(este tiene que correr en localhost)
r1 = redis.Redis(
            host='localhost',
            port=6500,
            password='',
            charset="utf-8",
            decode_responses=True)
p = Parser()
bd = BD(r=r1)

bd.guardarListaEnHashBD(p.cajasAhorro)
bd.guardarListaEnHashBD(p.ctasCtes)
bd.guardarListaEnHashBD(p.clientes)
bd.guardarListaEnHashBD(p.clientesCuentas)


@pytest.mark.parametrize('testInput,expected',[("bd.getListaCuentas()",p.ctasCtes),
                                               ("bd.getListaCuentas()",p.cajasAhorro),
                                               ("bd.getListaCuentasDelTituar('c1')", listaCuentasC1),
                                               ("bd.getListaCuentasDelTituar('c2')", listaCuentasC2)])
#Testea que cada elemento de la lista expected este en la lista devuelta por la BD, producto de un get:
def testGetLista(testInput,expected):
    returnedList = eval(testInput)
    for x in expected:
        assert (x in returnedList)