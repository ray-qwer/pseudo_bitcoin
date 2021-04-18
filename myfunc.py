import base58
def my_encode(str, code ='utf-8'):
    return str.encode(code)
def my_decode(byte, code = 'utf-8'):
    return byte.decode(code)
def address_to_pubkey_hash(address):
    return base58.base58CheckDecode(address)