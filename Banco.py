#Código principal

class banco:
    def __init__(self, numero, titular, saldo, limite):

        self.numero= numero
        self.titular= titular
        self.saldo= saldo
        self.limite= limite


    def deposita(self, numero, valor):
        numero = numero
        self.saldo += valor

        if valor == 0: #usando essa condição para fazer o teste, caso o usuario nao deposite nada
                       #verificar se há saldo.
            return self.saldo

        else:
            return valor

    def saca(self, numero, valor):
        numero= numero
        self.saldo -= valor

        if valor == 0: #usando essa condição para fazer o teste, caso o usuario nao saque nada
                       #verificar se há saldo.
            return self.saldo

        else:
            return valor

    def transfere(self, numero, valor, contadestino=1002):
        numero= numero
        self.contadestino= contadestino
        self.saldo -= valor

        if valor == 0: #usando essa condição para fazer o teste, caso o usuario nao saque nada
                       #verificar se há saldo.
            return self.saldo
        else:
            return contadestino

    def extrato(self, numero, saldo):
        self.numero= numero
        self.saldo= saldo

        return saldo

