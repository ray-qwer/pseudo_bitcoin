import block
class BlockChain:
    def __init__(self):
        self._blocks = []
        self._blocks.append(block.NewGenesisBlock())
    def add_block(self, transactions):
        # transactions : type:string
        prevBlock = self._blocks[-1]
        newBlock = block.NewBlock(transactions, prevBlock.Hash, len(self._blocks))
        self._blocks.append(newBlock)
        

def NewBlockChain():
    return BlockChain()

if __name__ == "__main__":
    a = BlockChain()
    print(block.my_decode(a._blocks[0].Transactions))
