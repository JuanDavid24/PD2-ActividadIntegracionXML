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
        if "id" in lista[0]:
            for x in lista:
             self.r.hmset(x["id"], x)
        else:
            for x in lista:
                self.r.hmset(x["c_id"] + x["cu_id"], x)

    def printCuentas(self):
        keys = (self.r.keys("a[0-9]*"))
        for k in keys:
            self.printCuentaPorID(k)

    def printCuentaPorID (self, cuentaID):
        print("Cuenta id: " + cuentaID + "\n \t Balance: " + str(self.r.hget(cuentaID, 'balance')))

    def printCuentasTitular(self, clienteID):
        allkeys = self.r.keys("*")
        print (allkeys)
        keys = self.r.keys(clienteID + "a*")
        print (keys)
        print("\nID del cliente: " + clienteID)
        for k in keys:
            cuentaID = self.r.hget(k, "cu_id")
            self.printCuentaPorID(cuentaID)
