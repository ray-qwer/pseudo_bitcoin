from myfunc import *
import hashlib
import pickle
class TXInput:
    def __init__(self,scriptSig,vout,data):
        self._scriptSig = scriptSig     # from who or someword
        self.vout = vout
        self.Txid = data        # from which transaction
    def __str__(self):
        return "TXIn\nFrom: {f}\namount: {out}\n".format(f = self._scriptSig, out = self.vout)

class TXOutput:
    def __init__(self,scriptPubKey,value):
        self._scriptPubKey = scriptPubKey   # To Who -> here is name
        # todo 
        self.value = value
    def __str__(self):
        return "TXOut\nTo: {t}\namount: {v}\n".format(t = self._scriptPubKey, v = self.value)
class Transaction:
    def __init__(self,Txinput,Txoutput):
        self.Vin =  Txinput  # TXInput array
        self.Vout = Txoutput  # TXOutput array
        self.ID = None
        self.setID()
    def setID(self):
        # TODO
        m = hashlib.sha256()
        m.update(pickle.dumps(self))
        self.ID = my_encode(m.hexdigest())
    def __str__(self):
        string = ""
        for i in self.Vin:
            string += str(i)
        for i in self.Vout:
            string += str(i)
        return string
        

def NewCoinbaseTransaction(to, data = ""):
    # to : the man who get coin
    # data : transaction data?
    subsidy = 10 # now is a constant
    if data == "":
        data = "Reward to {s}".format(s=to)
    txin = TXInput(data,-1,my_encode(""))
    txout = TXOutput(to,subsidy)
    tx = Transaction([txin],[txout])

    return tx

def NewUTXOTransaction(From, To, amount, bc):
    # from : the customer
    # to : the seller
    # amount : how much
    # bc : blockchain
    txin = []
    txout = []
    acc, validOutput = bc.FindSpendableOutput(From)
    if acc < amount:
        
        return None
    # build a list of inputs
    for tx in validOutput:
        for i in tx.Vout:
            if i._scriptPubKey == From:
                txin.append(TXInput(From,i.value,tx.ID))
    
    # build a list of output
    txout.append(TXOutput(To,amount))
    if acc > amount:
        txout.append(TXOutput(From,acc-amount))
    
    tx = Transaction(txin,txout)
    return tx
        