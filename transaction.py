class TXInput:
    def __init__(self,scriptSig):
        self._scriptSig = scriptSig
        # todo
        # Txid byte
        # vout int

class TXOutput:
    def __init__(self,scriptPubKey):
        self._scriptPubKey = scriptPubKey
        # todo 
        # value int

class Transaction:
    def __init__(self,id):
        self.Vin =  []  # TXInput
        self.Vout = []  # TXOutput
        self.ID = id
