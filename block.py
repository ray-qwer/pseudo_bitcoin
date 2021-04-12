import datetime
import pow
from myfunc import *
import transaction

class block:
    def __init__(self, Transactions, PrevBlockHash, PrevHeight):
        self.Height = PrevHeight+1
        self.PrevBlockHash = PrevBlockHash
        self.time = datetime.datetime.strftime(datetime.datetime.now(),'%Y-%m-%d %H:%M:%S')
        self.Bits = 12 # a static num for now
        self.Nonce = None
        self.Transactions = Transactions
        self.Hash = None
    def setHash(self):
        # get nonce and hash
        # nonce,hash = pow.Run
        proof_of_block = pow.PoW(self)
        nonce,hashHex = proof_of_block.Run()
        self.Nonce, self.Hash = nonce, my_encode(hashHex)
    def verifyHash(self):
        proof_of_block = pow.PoW(self)
        nonce,hashHex = proof_of_block.Run()
        if (nonce != self.Nonce or my_encode(hashHex) != self.Hash):
            return False
        else:
            return True
        # print(proof_of_block.Validate())
    def __str__(self):
        return ("block:\nheight: {height}\ntime: {time}\nBits: {Bits}\nNonce: {Nonce}\nhash: {hash}\nprevious block hash: {prev_hash}\ntransaction: {transaction}\n"\
            .format(height = self.Height,time = self.time,Bits = self.Bits, Nonce = self.Nonce, 
            hash = my_decode(self.Hash), transaction = self.Transactions, prev_hash = my_decode(self.PrevBlockHash)))
        

def NewBlock(transaction, PrevBlockHash, PrevHeight):
    blk = block(transaction, PrevBlockHash,PrevHeight)
    blk.setHash()
    # print("complete mining")
    return blk

# def NewGenesisBlock(to,data = ""):
#     transaction.NewCoinbaseTransaction(to,data)
#     return NewBlock(data,my_encode(""),0)

# if __name__ == "__main__":
    # a = NewGenesisBlock("ray")
    # print(a)

    