# Setup
By default, server.ipynb uses port 1000, then all the other files increment ports up to 1003. Additionally, temp ports are sourced from your available ports. If this doesn't work, change it in util.py's SERVER constant. 

# TODO
- Yeah the 3-way handshake from the phone to the server doesn't work. This seems to be because RSA isn't implemented in the right order, ie., the message is sent and decryption is attempted with the public key of the wrong key pair.  

# util.py
util.py is a file that implements universal versions of certain methods ensuring a common implementation of a protocol. Those methods are as follows:
- encrypt
- decrypt
- hash
- generate_n
- generate_k

PyCryptodome and socket are in scope of util, but not device, phone, and server directly, for ease of access. util.py also stores several constants:
- AES_MODE: int
- SIZE_N: int
- SIZE_K: int 
- SERVER: dict
    - "alias" : "localhost"
    - "port" : 1000