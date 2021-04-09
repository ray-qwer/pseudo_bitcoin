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
        self._db.store_block_chain(self)

    def reset_blk_chain(self):
        self._blocks = []
        self._blocks.append(block.NewGenesisBlock())
        self._db.store_block_chain(self)

    def get_block(self,height):
        try:
            return self._blocks[height]
        except:
            return "This block is not exist yet!!"

    def __str__(self):
        blk_chain_str = "blockchain:\nlength: {length}".format(length = len(self._blocks))
        return blk_chain_str        
    
    def get_length(self):
        return len(self._blocks)

def cli_addBlock(transaction):
    blk_chain = BlockChain()
    blk_chain.add_block(transaction)


def cli_printblock(height):
    blk_chain = BlockChain()
    print(blk_chain.get_block(height-1))

def cli_print_block_chain():
    blk_chain = BlockChain()
    print(blk_chain)
    for i in range(blk_chain.get_length()):
        print(blk_chain.get_block(i))
    
def NewBlockChain():
    return BlockChain()

if __name__ == "__main__":
    a = BlockChain()
    print(block.my_decode(a._blocks[0].Transactions))
    a.add_block("blabla")
    a._db.store_block_chain(a)
    print(block.my_decode(a._blocks[1].Transactions))
    a.reset_blk_chain()
    a.add_block("hi")
    print(block.my_decode(a._blocks[1].Transactions))

    # f = open("blockchain.pckl","wb")
    # pickle.dump(a,f)
    # f.close()
    