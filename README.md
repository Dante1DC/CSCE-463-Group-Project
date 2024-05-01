# Setup
By default, server.ipynb uses port 1000. If this doesn't work, change it in util.py's SERVER constant. 

# TODO
- device.ipynb
- 3-way handshakes
- phone only sends requests bc there's no pv model of receiving requests 
- server blasts message to socket channel, but phone has already closed socket connection, phone needs listener 
- rsa???

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