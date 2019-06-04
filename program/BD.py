import redis

class BD (object):
    #Conexion con el server de Redis:
    r = redis.Redis(
        host='redis_server',
        port=6379,
        password='',
        charset="utf-8",
        decode_responses=True)

    def guardarListaEnHashBD(self, lista):
        if "id" in lista[0]:    # Es una lista de dicts de los tipos: CC, clientes, cj.ahorro
            for x in lista:
             self.r.hmset(x["id"], x)

        else:                # Es lista de clientes-cuentas (la que relaciona las pk de ambas tablas)
            for x in lista:
                self.r.hmset(x["c_id"] + x["cu_id"], x)

    def getListaCuentas(self):
        keys = (self.r.keys("a[0-9]*"))     #Todas las keys de cuentas
        listaCuentas = []
        for k in keys:
            listaCuentas.append(self.r.hgetall(k))
        return listaCuentas

    def getListaCuentasDelTituar(self, clienteID):
        allkeys = self.r.keys("*")
        print (allkeys)
        keys = self.r.keys(clienteID + "a*")
        print (keys)

        listaCuentasID = []
        for k in keys:
            listaCuentasID.append(self.r.hget(k,'cu_id'))

        listaCuentas = []
        for id in listaCuentasID:
            listaCuentas.append(self.r.hgetall(id))

        return listaCuentas