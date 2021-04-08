import datetime
import pow
from myfunc import my_decode
from myfunc import my_encode


class block:
    def __init__(self, Transactions, PrevBlockHash, PrevHeight):
        self.Height = PrevHeight+1
        self.PrevBlockHash = my_encode(PrevBlockHash)
        self.time = datetime.datetime.strftime(datetime.datetime.now(),'%Y-%m-%d-%H:%M:%S')
        self.Bits = 7 # a static num for now
        self.Nonce = None
        self.Transactions = my_encode(Transactions)
        self.Hash = None
    def setHash(self):
        # get nonce and hash
        # nonce,hash = pow.Run
        proof_of_block = pow.PoW(self)
        print(proof_of_block.preprare_data(0))
        nonce,hashHex = proof_of_block.Run()
        self.Nonce, self.Hash = nonce, my_encode(hashHex)

        

def NewBlock(transaction, PrevBlockHash, PrevHeight):
    blk = block(transaction, PrevBlockHash,PrevHeight)
    blk.setHash()
    print("complete mining")
    return blk

def NewGenesisBlock():
    return NewBlock("creational block: \nwelcome to the lab","",0)

if __name__ == "__main__":
    a = NewGenesisBlock()

    