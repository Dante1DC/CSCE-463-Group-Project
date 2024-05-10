from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Hash import SHA256
import socket

from util import SERVER, generate_n

import util

def phone():
   # RSA_KEY_PAIR = RSA.generate(2048)
   # private_key = RSA_KEY_PAIR.export_key(format='PEM')
   # public_key = RSA_KEY_PAIR.publickey().export_key(format='PEM')
   encoded_key = open("phone.pk", "rb").read()
   private_key = RSA.import_key(encoded_key)
   public_key = private_key.public_key()

   sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   sock.connect(("tcpbin.com", 4242))
   nonce_p = generate_n()
   cipher = PKCS1_OAEP.new(public_key, SHA256)
   encrypted_nonce_p = cipher.encrypt(nonce_p)

   print("encrypted_nonce_p", len(encrypted_nonce_p), )

   concat = encrypted_nonce_p + (public_key.export_key('PEM'))
   sock.send(concat)

   concat = sock.recv(1024)

   encrypted_nonce_p = concat[:256]
   phone_public_key = concat[257:]
  

   cipher = PKCS1_OAEP.new(private_key, SHA256)

   print("nonce_p", len(encrypted_nonce_p), encrypted_nonce_p)
   nonce_p = cipher.decrypt(encrypted_nonce_p)

   print("nonce_p", nonce_p)
    

phone()
