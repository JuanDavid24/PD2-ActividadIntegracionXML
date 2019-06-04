from BD import BD
import pytest

listaCuentas = [{'id': 'a3', 'balance': '4025'},
                {'id': 'a5', 'balance': '325'},
                {'id': 'a2', 'interes': '0.03', 'balance': '15075'},
                {'id': 'a1', 'interes': '0.03', 'balance': '2500'},
                {'id': 'a4', 'balance': '-125'}]

listaCuentasC1 = [{'id': 'a2', 'interes': '0.03', 'balance': '15075'},
                  {'id': 'a3', 'balance': '4025'}]

listaCuentasC2 = [{'id': 'a4', 'balance': '-125'}]

bd = BD()

@pytest.mark.parametrize('testInput,expected',[("bd.getListaCuentas()",listaCuentas),
                                               ("bd.getListaCuentasDelTituar('c1')", listaCuentasC1),
                                               ("bd.getListaCuentasDelTituar('c2')", listaCuentasC2)])
def testGetLista(testInput,expected):
    assert eval(testInput) == expected