import block
from db import db
import pickle
class BlockChain:
    def __init__(self):
        # _db = db()
        # if _db.if_have_block_chain():
        self._db = db()
        if self._db.if_have_blk_chain():
            self._blocks = self._db.get_blk_chain()._blocks
        else:
            self._blocks = []
            self._blocks.append(block.NewGenesisBlock())
    def add_block(self, transactions):
        # transactions : type:string
        prevBlock = self._blocks[-1]
        newBlock = block.NewBlock(transactions, prevBlock.Hash, len(self._blocks))
        self._blocks.append(newBlock)

    def reset_blk_chain(self):
        self._blocks = []
        self._blocks.append(block.NewGenesisBlock())
        self._db.store_block_chain(self)


        

def NewBlockChain():
    return BlockChain()

if __name__ == "__main__":
    a = BlockChain()
    print(block.my_decode(a._blocks[1].Transactions))
    a.add_block("blabla")
    a._db.store_block_chain(a)
    print(block.my_decode(a._blocks[2].Transactions))
    a.reset_blk_chain()
    a.add_block("hi")
    print(block.my_decode(a._blocks[1].Transactions))

    # f = open("blockchain.pckl","wb")
    # pickle.dump(a,f)
    # f.close()
    