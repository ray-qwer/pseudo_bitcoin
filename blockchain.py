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

    def createGenesisblock(self,addr):
        self._blocks = []
        tx = transaction.NewCoinbaseTransaction(addr,"")
        GenesisBlk = block.NewBlock(tx,my_encode(""),0)
        self._blocks.append(GenesisBlk)
        self._db.store_block_chain(self)
    
    
    def FindSpendableOutput(self,pubkey,amount):
        gar_block = dict()
        unspentTxs = {}
        acc = 0
        for i in range(len(self._blocks)-1,-1,-1):
            block = self._blocks[i]
            if not gar_block.get(block.Transactions.ID):
                for i,vout in enumerate(block.Transactions.Vout):
                    if vout._scriptPubKey == pubkey:
                        acc += vout.value
                        unspentTxs.setdefault(block.Transactions.ID,[]).append(i)
                        # unspentTxs.append(block.Transactions)
                        if amount < acc:
                            return acc,unspentTxs
            for vin in block.Transactions.Vin:
                if not gar_block.get(vin.Txid) and vin.pubKey == pubkey:
                    gar_block[vin.Txid] = True
        return acc,unspentTxs


    def FindBalance(self,pubkey):
        gar_block = dict()
        acc =0
        for i in range(len(self._blocks)-1,-1,-1):
            block = self._blocks[i]
            if not gar_block.get(block.Transactions.ID):
                for vout in block.Transactions.Vout:
                    if vout._scriptPubKey == pubkey:
                        acc += vout.value
            for vin in block.Transactions.Vin:
                # print(i,vin.pubKey)
                if not gar_block.get(vin.Txid) and vin.pubKey == pubkey:
                    gar_block[vin.Txid] = True
        return acc
    
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

    def find_transaction(self, txid):
        for blk in self._blocks:
            if blk.Transactions.ID == txid:
                return blk.Transactions 

    def sign(self,tx,privateKey):
        prev_txs = {}
        if len(self._blocks) == 0:
            tx.sign(privateKey,prev_txs)
            return
        for vin in tx.Vin:
            prev_tx = self.find_transaction(vin.Txid)
            prev_txs[prev_tx.ID] = prev_tx
        tx.sign(privateKey,prev_txs)

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
    