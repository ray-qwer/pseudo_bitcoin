from myfunc import *
import hashlib
import pickle
import wallets as ws
import ecdsa
import binascii
import base58
import binascii
class TXInput:
    def __init__(self,scriptSig,vout,data,publicKey):
        self._scriptSig = scriptSig     # sign
        self.vout = vout        # the num of item in list at txid.vout
        self.Txid = data        # from which transaction
        self.pubKey = publicKey      # pubkey
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
    def trimmed_copy(self):
        inputs = []
        outputs = [] 
        for vin in self.Vin:
            inputs.append(TXInput(None,vin.vout,vin.Txid,None))
        for vout in self.Vout:
            outputs.append(TXOutput(vout._scriptPubKey,vout.value))
        return Transaction(inputs,outputs)
    def sign(self,privatekey,prev_txs):
        for i in self.Vin:
            if not prev_txs[i.Txid].ID:
                print("previos transaction is not correct")
        tx_copy = self.trimmed_copy()
        for i,vin in enumerate(tx_copy.Vin):
            prev_tx = prev_txs[vin.Txid]
            vin._scriptSig = None
            vin.pubKey = prev_tx.Vout[vin.vout]._scriptPubKey
            tx_copy.setID()
            vin.pubKey = None

            sk = ecdsa.SigningKey.from_string(binascii.unhexlify(privatekey),curve=ecdsa.SECP256k1)
            sig = sk.sign(tx_copy.ID)

            self.Vin[i]._scriptSig = sig
    def verify(self,prev_txs):
        for vin in self.Vin:
            if not prev_txs[vin.Txid].ID:
                print("previous transaction is not correct")
        tx_copy = self.trimmed_copy()

        for i, vin in enumerate(self.Vin):
            prev_tx = prev_txs[vin.Txid]
            vin._scriptSig = None
            vin.pubKey = prev_tx.Vout[vin.vout].publicKey
            tx_copy.setID()
            vin.pubKey = None

            sig = self.Vin[i]._scriptSig
            vkstring = binascii.unhexlify(my_encode(vin.pubKey))
            vk = ecdsa.VerifyingKey.from_string(vkstring,curve = ecdsa.SECP256k1)

            if not vk.verify(sig,tx_copy.ID):
                return False
        return True


    


def NewCoinbaseTransaction(to,data = ""):
    # to : the man who get coin
    # data : transaction data?
    subsidy = 10 # now is a constant
    if data == "":
        data = "Reward to {s}".format(s=to)
    txin = TXInput(None,-1,my_encode(""),None)
    wallets = ws.wallets()
    wallet = wallets.get_wallet_by_addr(to)
    pubkey_hash = wallet._hashPublicKey
    txout = TXOutput(pubkey_hash,subsidy)
    tx = Transaction([txin],[txout])
    # bc.sign(tx,pubkey_hash)
    return tx

def NewUTXOTransaction(FromAddr, ToAddr, amount, bc):
    # from : the customer
    # to : the seller
    # amount : how much
    # bc : blockchain
    txin = []
    txout = []
    wallets = ws.wallets()
    wallet1 = wallets.get_wallet_by_addr(FromAddr)
    pubkey_hash1 = wallet1._hashPublicKey
    wallet2 = wallets.get_wallet_by_addr(ToAddr)
    pubkey_hash2 = wallet2._hashPublicKey

    acc, validOutput = bc.FindSpendableOutput(pubkey_hash1,amount)
    print(acc)
    if acc < amount:
        
        return None
    # build a list of inputs
    for tx_id,outs in validOutput.items():
        for out in outs:
            txin.append(TXInput(None,out,tx_id,pubkey_hash1))

    txout.append(TXOutput(pubkey_hash2,amount))
    if acc > amount:
        txout.append(TXOutput(pubkey_hash1,acc-amount))
    
    tx = Transaction(txin,txout)
    bc.sign(tx,wallet1._privateKey)
    return tx
        