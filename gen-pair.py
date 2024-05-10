import socket

from Crypto.Cipher import AES
from Crypto.Util import Counter
from Crypto.Hash import HMAC, SHA256
from Crypto.Random import get_random_bytes

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# NOTE: chose bc lower performance overhead and less error propogation, subject to change
AES_MODE = AES.MODE_CTR 

SIZE_N = 16
SIZE_K = 32

SERVER = {"alias" : "localhost", "port" : 1000}

def make_pair_file(filename):
    pair = RSA.generate(2048)
    with open(filename + ".pk", "wb") as f:
        private_key = pair.export_key(format='PEM')
        f.write(private_key)
    
    with open(filename + ".pub", "wb") as f:
        public_key = pair.publickey().export_key(format='PEM')
        f.write(public_key)

make_pair_file("phone")
make_pair_file("server")