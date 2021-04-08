import datetime

def my_encode(str, code ='utf-8'):
    return str.encode(code)
def my_decode(byte, code = 'utf-8'):
    return byte.decode(code)

class block:
    def __init__(self, Transactions, PrevBlockHash, PrevHeight):
        self.Height = PrevHeight+1
        self.PrevBlockHash = my_encode(PrevBlockHash)
        self.time = int(datetime.datetime.now().timestamp())
        self.Bits = 0
        self.Nonce = 0
        self.Transactions = my_encode(Transactions)
        self.Hash = None
    def setHash(self):
        self.Hash = 0


def NewBlock(transaction, PrevBlockHash, PrevHeight):
    blk = block(transaction, PrevBlockHash,PrevHeight)
    blk.setHash()
    return blk

def NewGenesisBlock():
    return NewBlock("creational block: \nwelcome to the lab","",0)