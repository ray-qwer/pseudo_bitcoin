import hashlib
import sys
from myfunc import my_decode
from myfunc import my_encode

maxNonce = sys.maxsize
class PoW:
    def __init__(self,block):
        self._block = block
        self._target = 1<<(256-block.Bits)
    def prepare_data(self, nonce):
        data_list = [
            self._block.PrevBlockHash,
            self._block.Transactions,
            my_encode(self._block.time),
            my_encode(str(nonce))
        ]
        data = bytearray()
        for i in data_list:
            data.extend(i)
        # here we just need to create a randnum
        return data
    def Validate(self):
        hashNum = int(sha256_hash(self.prepare_data(self._block.Nonce)),16)
        return self._target > hashNum
    def Run(self):
        nonce = 0
        print('start mining')
        while nonce < maxNonce:
            data = self.prepare_data(nonce)
            hashString =  sha256_hash(data)
            hashNum = int(hashString,16)
            if self._target > hashNum:
                break
            else:
                nonce+=1
        return  nonce, hashString

def sha256_hash(data):
    s = hashlib.sha256()
    s.update(data)
    return s.hexdigest()
def sha256_bytes(data):
    s = hashlib.sha256()
    s.update(data)
    return s.digest()