from ecdsa import SigningKey, SECP256k1
import hashlib
import binascii
import base58
from myfunc import *
import wallets as ws

class Wallet:
    def __init__(self,privateKey,publicKey,name):
        self._privateKey = privateKey   # string now in base64
        self._publicKey = publicKey     # string now in base64
        self._hashPublicKey = self.get_hash_public_key()
        self._address = self.getAddress(self._hashPublicKey)
        self.Name = name
    def getAddress(self,hashpublicKey):
        return base58.base58CheckEncode(0X00,hashpublicKey)
    def get_hash_public_key(self):
        ripemd160 = hashlib.new('ripemd160')
        ripemd160.update(hashlib.sha256(binascii.unhexlify(self._publicKey)).digest())
        return ripemd160.hexdigest()
    

# ecdsa usage
"""
from ecdsa import SigningKey
sk = SigningKey.generate() # uses NIST192p
vk = sk.verifying_key
signature = sk.sign(b"message")
assert vk.verify(signature, b"message")
sk -> private key
vk -> public key
"""
def newWallet(name):
    wallets = ws.wallets()
    privateKey, publicKey = newKeyPair()
    wallet = Wallet(privateKey, publicKey,name)
    wallets.add_wallet(name,wallet._address,wallet)
    return wallet
    

def newKeyPair():
    sk = SigningKey.generate(curve=SECP256k1)
    privateKey = sk.to_string().hex()
    vk = sk.get_verifying_key() 
    publicKey = vk.to_string().hex()  # publickey in string
    # store publicKey and privateKey in string
    # publicKey = '04' + bytes.decode(binascii.hexlify(publicKey.to_string()))
    return privateKey, publicKey

if __name__ == '__main__':
    # a,b = newKeyPair()
    # print(type(a))
    # print(a)
    # print(type(b))
    # print(b) 
    # string = base58.b58encode('00')
    # print(string)
    # string = base58.b58decode(string)
    # print(string)
    w = newWallet('ray')
    print(type(w._hashPublicKey))
    print(w._hashPublicKey)
    assert w._hashPublicKey == address_to_pubkey_hash(
        w._address), "Hash of public key is Not Equal!"
    