import sys
from blockchain import BlockChain


print(sys.argv)
if __name__ == "__main__":
    arg = sys.argv
    if len(arg) == 1:
        print("Need more variables. Type -h for usage.")
    elif len(arg) == 2:
        if arg[1].lower() == 'printchain':
            # todo->blockchain: __str__
            print("printchain...")
        elif arg[1].lower() == '-h':
            print("usage")
    elif len(arg) > 3:
        if arg[1].lower() == "addblock" and arg[2].lower() == '-transaction':
            transactions = ' '.join(arg[3:])
            print("addblock",transactions)
        elif arg[1].lower() == "printblock" and arg[2].lower() == "-height":
            try:
                height = str(arg[3])
                print("printblock",height)
            except:
                print("\"printblock\" needs a number. Type -h for usage.")
    else:
        print("Illegal command. Type -h for usage")