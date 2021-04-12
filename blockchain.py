import block
from db import db
import pickle
import transaction
from myfunc import *
from collections import defaultdict
class BlockChain:
    def __init__(self):
        # _db = db()
        # if _db.if_have_block_chain():
        self._db = db()
        if self._db.if_have_blk_chain():
            self._blocks = self._db.get_blk_chain()._blocks
        else:
            self._blocks = []
            # self._blocks.append(block.NewGenesisBlock())

            
    def add_block(self, transactions):
        # transactions : type:string
        # if len(self._blocks) == 0:
        #     self._blocks.append(block.NewGenesisBlock())
        prevBlock = self._blocks[-1]
        newBlock = block.NewBlock(transactions, prevBlock.Hash, len(self._blocks))
        self._blocks.append(newBlock)
        self._db.store_block_chain(self)


    def reset_blk_chain(self):
        self._blocks = []
        # self._blocks.append(block.NewGenesisBlock())
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

    def createGenesisblock(self,name):
        self._blocks = []
        tx = transaction.NewCoinbaseTransaction(name,"")
        GenesisBlk = block.NewBlock(tx,my_encode(""),0)
        self._blocks.append(GenesisBlk)
        self._db.store_block_chain(self)
    
    
    def FindSpendableOutput(self,name,amount):
        # search all blocks 
        # balance = dict()
        # unspentTxs = []
        # acc = 0
        # for block in self._blocks:
        #     for vout in block.Transactions.Vout:
        #         if vout._scriptPubKey == name:
        #             balance[block.Transactions.ID] = [vout.value,block.Transactions]
        #     for vin in block.Transactions.Vin:
        #         if balance.get(vin.Txid) and vin._scriptSig == name:
        #             balance[vin.Txid][0] -= vin.vout
        # for key,value in balance.items():
        #     if value[0] != 0: 
        #         acc += value[0]
        #         unspentTxs.append(value[1])
        #         if acc >= amount:
        #             break
        # return acc, unspentTxs
        gar_block = dict()
        unspentTxs = []
        acc = 0
        for i in range(len(self._blocks)-1,-1,-1):
            block = self._blocks[i]
            if not gar_block.get(block.Transactions.ID):
                for vout in block.Transactions.Vout:
                    if vout._scriptPubKey == name:
                        acc += vout.value
                        unspentTxs.append(block.Transactions)
                        if amount < acc:
                            return acc,unspentTxs
            for vin in block.Transactions.Vin:
                if not gar_block.get(vin.Txid) and vin._scriptSig == name:
                    gar_block[vin.Txid] = True
        return acc,unspentTxs


    def FindBalance(self,name):
        gar_block = dict()
        acc =0
        for i in range(len(self._blocks)-1,-1,-1):
            block = self._blocks[i]
            if not gar_block.get(block.Transactions.ID):
                for vout in block.Transactions.Vout:
                    if vout._scriptPubKey == name:
                        acc += vout.value
            for vin in block.Transactions.Vin:
                if not gar_block.get(vin.Txid) and vin._scriptSig == name:
                    gar_block[vin.Txid] = True
        return acc
        # balance = dict()
        # acc = 0
        # for block in self._blocks:
        #     for vout in block.Transactions.Vout:
        #         if vout._scriptPubKey == name:
        #             balance[block.Transactions.ID] = [vout.value,block.Transactions]
        #     for vin in block.Transactions.Vin:
        #         if balance.get(vin.Txid) and vin._scriptSig == name:
        #             balance[vin.Txid][0] -= vin.vout
        # for key,value in balance.items():
            
        #     if value[0] != 0:
        #         # print(acc)
        #         acc += value[0]
        # return acc
    
    def Verify_Block_Chain(self):
        for i in range(len(self._blocks)):
            if i == 0:
                if self._blocks[i].verifyHash():
                    continue
                else:
                    return False
            else:
                if self._blocks[i].verifyHash() and self._blocks[i-1].Hash == self._blocks[i].PrevBlockHash:
                    continue
                else:
                    return False
        return True

# def cli_addBlock(transaction):
#     blk_chain = BlockChain()
#     blk_chain.add_block(transaction)

def NewBlockChain():
    return BlockChain()


# if __name__ == "__main__":
    # a = BlockChain()
    # cli_print_block_chain()
    # cli_create_bc('ray')
    # cli_print_block_chain()
    # print(a.FindBalance("ray"))
    # sending("ray","simon",3)
    # # print(a.FindBalance('ray'))
    # cli_print_block_chain()
    # f = open("blockchain.pckl","wb")
    # pickle.dump(a,f)
    # f.close()
    