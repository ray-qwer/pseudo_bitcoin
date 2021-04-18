import sys
from blockchain import BlockChain
import transaction
from wallet import *
import wallets as WS

def strcompare(inputStr,commandStr):
    if len(inputStr) > len(commandStr) or len(inputStr) == 1:
        return False
    else:
        inputStr = inputStr.lower()
        for i in range(len(inputStr)):
            if inputStr[i] != commandStr[i]:
                return False
        return True
def cli_sending(From, To, amount):
    blk_chain = BlockChain()
    if not blk_chain.Verify_Block_Chain():
        print("Your database may be damaged. Cannot open this database.")
        return
    tx = transaction.NewUTXOTransaction(From,To,amount,blk_chain)
    if tx == None:
        print("Error: not enough funds")
        return
    blk_chain.add_block(tx)
    print ("From: {f}\nTo: {t}\nAmount: {a}".format(f=From,t=To,a=amount))

def cli_check_balance(Addr):
    blk_chain = BlockChain()
    if not blk_chain.Verify_Block_Chain():
        print("Your database may be damaged. Cannot open this file.")
        return
    ws = WS.wallets()
    wallet = ws.get_wallet_by_addr(Addr)
     
    amount = blk_chain.FindBalance(wallet._hashPublicKey)
    print("Address: {addr}\nAmount: {a}".format(addr = Addr,a = amount))

def cli_create_bc(Addr):
    blk_chain = BlockChain()
    blk_chain.createGenesisblock(Addr)

def cli_printblock(height):
    blk_chain = BlockChain()
    if not blk_chain.Verify_Block_Chain():
        print("Your database may be damaged. Cannot open this file.")
        return
    print(blk_chain.get_block(height-1))

def cli_print_block_chain():
    blk_chain = BlockChain()
    if not blk_chain.Verify_Block_Chain():
        print("Your database may be damaged. Cannot open this database.")
        return
    print(blk_chain)
    for i in range(blk_chain.get_length()):
        print(blk_chain.get_block(i))

# create wallet by name
def cli_create_wallet(name):
    NewWallet = newWallet(name)

def cli_check_balance_by_name(name):
    ws = WS.wallets()
    wallet = ws.get_wallet_by_name(name)
    cli_check_balance(wallet._address)

def createblockchain_by_name(name):
    ws = WS.wallets()
    wallet = ws.get_wallet_by_name(name)
    cli_create_bc(wallet._address)

def cli_sending_by_name(fromName,toName,amount):
    ws = WS.wallets()  
    w1 = ws.get_wallet_by_name(fromName)
    w2 = ws.get_wallet_by_name(toName)
    cli_sending(w1._address,w2._address,amount)
# print(sys.argv)
# if __name__ == "__main__":
#     arg = sys.argv
#     if len(arg) == 1:
#         print("Need more variables. Type -h for usage.")
#     elif len(arg) == 2:
#         if arg[1].lower() == 'printchain':
#             # todo->blockchain: __str__
#             cli_print_block_chain()
#         elif arg[1].lower() == '-h':
#             print("""usage:
#             1. cli.py createblockchain -address { Name }
#             2. cli.py getbalance -address { address }
#             3. cli.py send -from { From } -to { To } -amount { How-much }
#             4. cli.py printchain 
#             5. cli.py printblock -height { height }
#                         """)
#     elif len(arg) > 3:
#         # if arg[1].lower() == "addblock" and strcompare(arg[2],"-transaction"):
#         #     transactions = ' '.join(arg[3:])
#         #     print("addblock \"{transactions}\"".format(transactions = transactions))
#         #     cli_addBlock(transactions)
#         if arg[1].lower() == "createblockchain" and strcompare(arg[2], "-address"):
#             name = ' '.join(arg[3:])
#             cli_create_bc(name)
#         elif arg[1].lower() == "getbalance" and strcompare(arg[2],"-address"):
#             name = ' '.join(arg[3:])
#             cli_check_balance(name)
#         elif arg[1].lower() == "printblock" and strcompare(arg[2],"-height"):
#             try:
#                 height = int(arg[3])
#                 cli_printblock(height)
#             except:
#                 print("\"printblock\" needs a number. Type -h for usage.")
#         elif len(arg) == 8:
#             if arg[1].lower() == "send" and strcompare(arg[2],"-from") and strcompare(arg[4],"-to") and strcompare(arg[6],"-amount"):
#                 try:
#                     name1 , name2= arg[3],arg[5]
#                     amount = int(arg[7])
#                     cli_sending(name1,name2,amount)
#                 except:
#                     print("\"amount\" needs a number when sending. Type -h for usage.")
#         else:
#             print("Illegal command. Type -h for usage")
#     else:
#         print("Illegal command. Type -h for usage")

if __name__ == '__main__':
    # cli_create_wallet('arthur')
    # createblockchain_by_name('ray')
    # cli_sending_by_name('ray','arthur',5)
    cli_check_balance_by_name('ray')
