import sys
from blockchain import BlockChain
from blockchain import cli_addBlock
from blockchain import cli_printblock
from blockchain import cli_print_block_chain

def strcompare(inputStr,commandStr):
    if len(inputStr) > len(commandStr) or len(inputStr) == 1:
        return False
    else:
        inputStr = inputStr.lower()
        for i in range(len(inputStr)):
            if inputStr[i] != commandStr[i]:
                return False
        return True

# print(sys.argv)
if __name__ == "__main__":
    arg = sys.argv
    if len(arg) == 1:
        print("Need more variables. Type -h for usage.")
    elif len(arg) == 2:
        if arg[1].lower() == 'printchain':
            # todo->blockchain: __str__
            cli_print_block_chain()
        elif arg[1].lower() == '-h':
            print("""usage:
            1. cli.py addblock -transaction { someword }  
            2. cli.py printchain 
            3. cli.py printblock -height { height }
                        """)
    elif len(arg) > 3:
        if arg[1].lower() == "addblock" and strcompare(arg[2],"-transaction"):
            transactions = ' '.join(arg[3:])
            print("addblock \"{transactions}\"".format(transactions = transactions))
            cli_addBlock(transactions)
        elif arg[1].lower() == "printblock" and strcompare(arg[2],"-height"):
            try:
                height = int(arg[3])
                cli_printblock(height)
            except:
                print("\"printblock\" needs a number. Type -h for usage.")
    else:
        print("Illegal command. Type -h for usage")
