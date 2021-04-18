from wallet import *
import pickle
import sys
class wallets:
    def __init__(self):
        try:
            with open('wallets.pckl','rb') as f:
                walletsData = pickle.load(f)
                self.wallets = walletsData.wallets
                self.walletAddr = walletsData.walletAddr
        except FileNotFoundError:
            self.wallets = {}
            self.walletAddr = {}
    def add_wallet(self,name,addr,wallet):
        if self.isExistbyName(name):
            print("this wallet({name}) is already exist!".format(name=name))
            sys.exit()
        self.walletAddr[addr] = name
        self.wallets[name] = wallet
        self.store_wallet()
    def get_wallet_by_addr(self,addr):
        if not self.isExistbyAddr(addr):
            print("this wallet({addr}) is not existed!".format(addr=addr))
            sys.exit()    
        name = self.walletAddr[addr]
        return self.wallets[name]
    def get_wallet_by_name(self,name):
        if not self.isExistbyName(name):
            print("this wallet({name}) is not existed!".format(name=name))
            sys.exit()
        return self.wallets[name]
    def store_wallet(self):
        with open('wallets.pckl','wb') as f:
            pickle.dump(self,f)
    def isExistbyName(self,name):
        if self.wallets.get(name,None):
            # print("this wallet({name}) is already exist!".format(name=name))
            return True
        return False
    def isExistbyAddr(self,addr):
        if self.walletAddr.get(addr,None):
            return True
        return False
# id:wallet