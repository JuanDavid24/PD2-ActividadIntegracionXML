import pytest
from BD import BD
import redis
import os

ID_STR_PARA_GETS = 'id'
CLIENTE_ID_COMO_FK_STR = 'c_id'
CUENTA_ID_COMO_FK_STR = 'cu_id'

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

else:
    #Dev env
    r1 = redis.Redis(
        host='redis_sv_test',  # Nombre del container
        port=6379,
        password='',
        encoding="utf-8",
        decode_responses=True)

bd = BD(r=r1)

listaClientes = [{'id': 'c1', 'nombre': 'Ricardo Carotenuto', 'direccion': 'Gral Chamizo 50'},
                 {'id': 'c2', 'nombre': 'Trapito Paez', 'direccion': 'Ojo Pekin 670'},
                 {'id': 'c3', 'nombre': 'Luis Solari', 'direccion': 'Rodeo Drive 145'},
                 {'id': 'c4', 'nombre': 'EVA-01', 'direccion': 'Tokio-03'}] #cliente sin cuentas (a ver...es un EVA!)
listaCuentas = [{'id': 'a1', 'interes': '0.03', 'balance': '2500'},
                {'id': 'a2', 'interes': '0.03', 'balance': '15075'},
                {'id': 'a3', 'balance': '4025'},
                {'id': 'a4', 'balance': '-125'},
                {'id': 'a5', 'balance': '325'}]
listaClientesCuentas = [{'c_id': 'c1', 'cu_id': 'a2'},
                        {'c_id': 'c1', 'cu_id': 'a3'},
                        {'c_id': 'c2', 'cu_id': 'a4'},
                        {'c_id': 'c3', 'cu_id': 'a1'},
                        {'c_id': 'c3', 'cu_id': 'a5'}]
cuentasC1 = [{'id': 'a2', 'interes': '0.03', 'balance': '15075'}, {'id': 'a3', 'balance': '4025'}]
cuentasC2 = [{'id': 'a4', 'balance': '-125'}]
cuentasC3 = [{'id': 'a1', 'interes': '0.03', 'balance': '2500'}, {'id': 'a5', 'balance': '325'}]
cuentasC4 = []


@pytest.fixture(scope='module')
def setupParaTestsGet():
    print('*GET tests setup* : Poblando la BD de redis')
    r1.hmset('c1', {'id': 'c1', 'nombre': 'Ricardo Carotenuto', 'direccion': 'Gral Chamizo 50'})
    r1.hmset('c2', {'id': 'c2', 'nombre': 'Trapito Paez', 'direccion': 'Ojo Pekin 670'})
    r1.hmset('c3', {'id': 'c3', 'nombre': 'Luis Solari', 'direccion': 'Rodeo Drive 145'})
    r1.hmset('c4', {'id': 'c4', 'nombre': 'EVA-01', 'direccion': 'Tokio-03'})
    r1.hmset('a1', {'id': 'a1', 'interes': '0.03', 'balance': '2500'})
    r1.hmset('a2', {'id': 'a2', 'interes': '0.03', 'balance': '15075'})
    r1.hmset('a3', {'id': 'a3', 'balance': '4025'})
    r1.hmset('a4', {'id': 'a4', 'balance': '-125'})
    r1.hmset('a5', {'id': 'a5', 'balance': '325'})
    r1.hmset('c1a2', {'c_id': 'c1', 'cu_id': 'a2'})
    r1.hmset('c1a3', {'c_id': 'c1', 'cu_id': 'a3'})
    r1.hmset('c2a4', {'c_id': 'c2', 'cu_id': 'a4'})
    r1.hmset('c3a1', {'c_id': 'c3', 'cu_id': 'a1'})
    r1.hmset('c3a5', {'c_id': 'c3', 'cu_id': 'a5'})

@pytest.fixture(scope='function')
def setupParaTestSave():
    print('*SAVE tests setup* : se limpia la BD de redis')
    r1.flushdb()

# -----TESTS de consulta a la BD-----
#-caso cliente con mas de una cuenta
def testGetListaCuentasTitularTieneMasDeUnaCuenta(setupParaTestsGet):
        returnedList = bd.getListaCuentasDelTitular('c1')
        for x in returnedList:
            assert x in cuentasC1

#-caso cliente con una cuenta
def testGetListaCuentasTitularTieneUnaCuenta(setupParaTestsGet):
    returnedList = bd.getListaCuentasDelTitular('c2')
    assert returnedList == cuentasC2

#-cliente sin cuentas
def testGetListaCuentasTitularSinCuentas(setupParaTestsGet):
    returnedList = bd.getListaCuentasDelTitular('c4')
    assert returnedList == []

#-cliente inexistente
def testGetListaCuentasTitularInexistente(setupParaTestsGet):
    returnedList = bd.getListaCuentasDelTitular('c8')
    assert returnedList == []

#-lista de todas las cuentas
def testGetListaCuentas(setupParaTestsGet):
    returnedList = bd.getListaCuentas()
    print('returnedList: ' + str(returnedList))
    for x in listaCuentas:
        assert (x in returnedList)

# -----TESTS de guardar en la BD-----
#-Lista de clientes
def testGuardarListaClientes(setupParaTestSave):
    bd.guardarListaEnHashBD(listaClientes)
    for cliente in listaClientes:
        returnedCliente = r1.hgetall(cliente[ID_STR_PARA_GETS])
        assert (returnedCliente in listaClientes)

#-Lista de cuentas
def testGuardarListaCuentas(setupParaTestSave):
    bd.guardarListaEnHashBD(listaCuentas)
    for cta in listaCuentas:
        returnedCta = r1.hgetall(cta[ID_STR_PARA_GETS])
        assert (returnedCta in listaCuentas)

#-Lista de clientes-cuentas
def testGuardarListaClientesCuentas(setupParaTestSave):
    bd.guardarListaClientesCuentasEnHashBD(listaClientesCuentas)
    for cteCta in listaClientesCuentas:
        returnedCteCta = r1.hgetall(cteCta[CLIENTE_ID_COMO_FK_STR] + cteCta[CUENTA_ID_COMO_FK_STR])
        assert (returnedCteCta in listaClientesCuentas)