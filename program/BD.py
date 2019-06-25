import redis

#Constantes para los strings usados
ID_STR_PARA_DB_SETS = 'id'
CLIENTE_ID_COMO_FK_STR = 'c_id'
CUENTA_ID_COMO_FK_STR = 'cu_id'
REGEXP_PARA_CUENTA_IDS = 'a[0-9]*'

class BD (object):

    def __init__(self, r=None):
        # Conexion con el server de Redis:
        if r is None:
            self.r = redis.Redis(
                host='redis_sv',
                port=6379,
                password='',
                encoding="utf-8",
                decode_responses=True)
        else:
            self.r = r

    def existeCliente(self, clienteID):
        exists = self.r.exists(clienteID)
        if exists == 1:
            return True
        else:
            return False

    # Guarda una lista de dicts de los tipos: CC, clientes, cj.ahorro
    def guardarListaEnHashBD(self, lista):
        for x in lista:
            self.r.hmset(x[ID_STR_PARA_DB_SETS], x)

    # Guarda lista de clientes-cuentas (la que relaciona las pk de ambas tablas)
    def guardarListaClientesCuentasEnHashBD(self, lista):
        for x in lista:
            self.r.hmset(x[CLIENTE_ID_COMO_FK_STR] + x[CUENTA_ID_COMO_FK_STR], x)

    def getListaCuentas(self):
        keys = (self.r.keys(REGEXP_PARA_CUENTA_IDS))     #Todas las keys de cuentas
        listaCuentas = []
        for k in keys:
            listaCuentas.append(self.r.hgetall(k))
        return listaCuentas

    def getListaCuentasDelTitular(self, clienteID):
        keysClienteCuenta = self.r.keys(clienteID + REGEXP_PARA_CUENTA_IDS)
        listaCuentasID = []
        for k in keysClienteCuenta:
            listaCuentasID.append(self.r.hget(k, CUENTA_ID_COMO_FK_STR))
        listaCuentas = []
        for id in listaCuentasID:
            listaCuentas.append(self.r.hgetall(id))

        return listaCuentas