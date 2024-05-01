import socket

from Crypto.Cipher import AES
from Crypto.Util import Counter
from Crypto.Hash import HMAC, SHA256
from Crypto.Random import get_random_bytes

# NOTE: chose bc lower performance overhead and less error propogation, subject to change
AES_MODE = AES.MODE_CTR 

SIZE_N = 16
SIZE_K = 32

SERVER = {"alias" : "localhost", "port" : 1000}

def encrypt(m, k, n):
    ctr = Counter.new(128, initial_value=int.from_bytes(n, byteorder='big'))
    cipher = AES.new(k, AES_MODE, counter=ctr)
    return cipher.encrypt(m)

# NOTE: this and encrypt are identical, but separated here for readability
def decrypt(ciphertext, k, n):
    ctr = Counter.new(128, initial_value=int.from_bytes(n, byteorder='big'))
    cipher = AES.new(k, AES_MODE, counter=ctr)
    return cipher.decrypt(ciphertext)

# hash function (equilvalent to Hash1 in the pv file) 
def hash(m, k, n):
    h = HMAC.new(k, digestmod=SHA256)
    h.update(n)
    h.update(m)
    # spits out the auth code given the updates above
    return h.digest()

def generate_n():
    return get_random_bytes(SIZE_N)

def generate_k():
    return get_random_bytes(SIZE_K)