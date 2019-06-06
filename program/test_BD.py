from BD import BD
import pytest
from parser.parser import Parser
import redis
import os

listaCuentasC1 = [{'id': 'a2', 'interes': '0.03', 'balance': '15075'},
                  {'id': 'a3', 'balance': '4025'}]
listaCuentasC2 = [{'id': 'a4', 'balance': '-125'}]

#Detecto el entorno en el cual estoy corriendo: Travis o Dev
if "TRAVIS_ENV" in os.environ:
    #Travis env
    r1 = redis.Redis(
        host='localhost',   # El redis de travis corre en localhost
        port=6500,
        password='',
        encoding="utf-8",
        decode_responses=True)
    bd = BD(r=r1)
else:
    #Dev env
    bd = BD()

p = Parser()

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