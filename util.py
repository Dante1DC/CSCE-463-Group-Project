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

SERVER = {"alias" : "localhost", "port" : 3000}

encoded_key = open("phone.pk", "rb").read()
PHONE_PRIVATE_KEY = RSA.import_key(encoded_key)
PHONE_PUBLIC_KEY = PHONE_PRIVATE_KEY.public_key()

encoded_key = open("server.pk", "rb").read()
SERVER_PRIVATE_KEY = RSA.import_key(encoded_key)
SERVER_PUBLIC_KEY = SERVER_PRIVATE_KEY.public_key()

def encrypt(m, k, n):
    ctr = Counter.new(128, initial_value=int.from_bytes(n, byteorder='big'))
    cipher = AES.new(k, AES_MODE, counter=ctr)
    return cipher.encrypt(m)

# NOTE: this and encrypt are identical, but separated here for readability
def decrypt(ciphertext, k, n):
    ctr = Counter.new(128, initial_value=int.from_bytes(n, byteorder='big'))
    cipher = AES.new(k, AES_MODE, counter=ctr)
    return cipher.decrypt(ciphertext)

# attempts to read until we have n bytes. will hang forever
def read_n(sock, n):
    return sock.recv(n, socket.MSG_WAITALL)
    # concat = b""
    # while len(concat) < n:
    #     print("will read upto:", n-len(concat))
    #     incoming = sock.recv(n-len(concat))
    #     concat = concat + incoming
    # return concat

import time
# very hacky, reads until there N seconds of no incoming data
def read_until_time_gap(sock, seconds):
    buffer = b""
    last_packet_time = time.time()
    while time.time() - last_packet_time < seconds:
        buffer += sock.recv(n, 1024)
        last_packet_time = time.time()
    return buffer

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