# H@cktivityCon: Triforce
 
![warmup category](https://img.shields.io/badge/Category-Cryptography-brightgreen.svg)  
![score](https://img.shields.io/badge/Score_after_CTF-444-blue.svg)  
![solves](https://img.shields.io/badge/Solves-73-lightgrey.svg) 

## Description
Are you the Hero of Time? Can you bring together the pieces of the Triforce?

## Attached files
- server.py

## Summary
Exploit the fact that they use part of the flag as the IV for AES mode CBC.

## Flag
```
flag{819f9d8d83721ac4c442b1659f36df2d}
```

## Detailed solution
The content of the file server.py:
```
#!/usr/bin/env python3

import os
import socketserver
import string
import threading
from time import *
from Crypto.Cipher import AES
import random
import time
import binascii

flag = open("flag.txt", "rb").read()
piece_size = 16
courage, wisdom, power = [
    flag[i : i + piece_size].ljust(piece_size)
    for i in range(0, piece_size * 3, piece_size)
]

banner = """
           /\\
          /  \\
         /    \\
        /      \\
       /        \\
      /__________\\
     /\\__________/\\
    /  \\        /  \\
   /    \\      /    \\
  /      \\    /      \\
 /        \\  /        \\
/__________\\/__________\\
\\__________/\\__________/
= = =  T R I F O R C E = = =
HELLO SPIRIT, WE WILL GRANT YOU ONE PIECE OF THE TRIFORCE:
         1. COURAGE    2. WISDOM    3.  POWER
WITH THIS PIECE YOU MAY ENCRYPT OR DECRYPT A SACRED SAYING.
    YOU HOLD THE SECRETS OF THE GODS WITH THIS TRIFORCE
"""


class Service(socketserver.BaseRequestHandler):
    def handle(self):

        self.send(banner)
        self.triforce = self.select_piece()
        if not self.triforce:
            return

        while True:
            self.send("1: ENCRYPT A SACRED SAYING")
            self.send("2: DECRYPT A SACRED SAYING")
            self.send("3: SELECT A NEW TRIFORCE PIECE")
            self.send("4: RETURN TO YOUR ADVENTURE")
            choice = self.receive("select# ").decode("utf-8")
            if choice == "1":
                self.encrypt_sacred_saying(self.triforce)
            elif choice == "2":
                self.decrypt_sacred_saying(self.triforce)
            elif choice == "3":
                self.triforce = self.select_piece()
            elif choice == "4":
                self.send("MAY THE GODS OF HYRULE SMILE UPON YOU.")
                return

    def send(self, string, newline=True):
        if type(string) is str:
            string = string.encode("utf-8")

        if newline:
            string = string + b"\n"
        self.request.sendall(string)

    def receive(self, prompt="> "):
        self.send(prompt, newline=False)
        return self.request.recv(4096).strip()

    def magic_padding(self, msg):
        val = 16 - (len(msg) % 16)
        if val == 0:
            val = 16
        pad_data = msg + (chr(val) * val)
        return pad_data

    def encrypt_sacred_saying(self, triforce):
        self.send("PLEASE ENTER YOUR SACRED SAYING IN HEXADECIMAL: ")

        sacred = self.receive("encrypt> ")
        sacred = self.magic_padding(str(binascii.unhexlify(sacred)))
        cipher = AES.new(self.triforce, AES.MODE_CBC, iv=self.triforce)
        saying = cipher.encrypt(sacred.encode("utf-8"))

        self.send("THANK YOU. THE GODS HAVE SPOKEN: ")
        self.send(binascii.hexlify(saying).decode("utf-8") + "\n")

    def decrypt_sacred_saying(self, triforce):
        self.send("PLEASE ENTER YOUR SACRED SAYING IN HEXADECIMAL: ")

        saying = self.receive("decrypt> ")
        saying = binascii.unhexlify(saying)
        if (len(saying) % 16) != 0:
            self.send("THIS IS NOT A SACRED SAYING THAT THE GODS CAN UNDERSTAND")
            return
        cipher = AES.new(self.triforce, AES.MODE_CBC, iv=self.triforce)

        sacred = cipher.decrypt(saying)
        self.send("THANK YOU. THE GODS HAVE SPOKEN: ")
        self.send(binascii.hexlify(sacred).decode("utf-8") + "\n")

    def select_piece(self):
        self.send("WHICH PIECE OF THE TRIFORCE WOULD YOU LIKE? (1,2,3)")
        piece = self.receive("triforce# ").decode("utf-8").strip()
        for i, triforce in enumerate([courage, wisdom, power]):
            if piece == str(i + 1):
                piece = triforce
                return piece
        else:
            self.send("THIS HERO OF TIME IS STUPID. PLZ PICK A REAL TRIFORCE PIECE.")
            return False


class ThreadedService(
    socketserver.ThreadingMixIn,
    socketserver.TCPServer,
    socketserver.DatagramRequestHandler,
):
    pass


def main():

    port = 3156
    host = "0.0.0.0"

    service = Service
    server = ThreadedService((host, port), service)
    server.allow_reuse_address = True

    server_thread = threading.Thread(target=server.serve_forever)

    server_thread.daemon = True
    server_thread.start()

    print("Server started on " + str(server.server_address) + "!")

    # Now let the main thread just wait...
    while True:
        sleep(10)


if __name__ == "__main__":
    main()
```
To summarize their encryption process, the flag is divided into 3 parts with length = 16 each. Each part is then used as an IV for the AES (mode CBC) encryption.  
We then have the choice to choose any part, then decrypt or encrypt any input.  
The vulnerability of this implementation is the fact that they use the flag itself for the IV. To understand how we can exploit this, first we have to understand how AES work.    
The way AES mode CBC encryption work is to divide the user input into blocks (padded in this case).  
Let's say we have i1, i2, i3 as the three input blocks.  
i1 will be xor-ed with the IV, then encrypted with the AES algorithm, which produce o1. o1 will then be used as the IV for i2, and so on.  
When decrypting, let's say we have i4, i5, i6 as the input, i4 will be decrypted with the AES algorithm, and then xor-ed with the IV. i4 will be used as the IV for i5 and so on.  
  
The fact that we can freely choose any input for the decryption function, means that we can find out IV by the following process:  
1. Choose i4 = i5 = i6.
2. Decrypt all the inputs, we then will have o4 = D(i4)^IV, o5 = D(i5)^i4, o6 = D(i6)^i5 where D() is AES decryption algorithm.
3. Since i4 = i5 = i6, D(i4) = D(i5) = D(i6), therefore o5 = o6.
4. If 3 holds, proceed to calculate o4^o5 = D(i4)^IV^D(i5)^i4 = D(i4)^D(i4)^i4^IV = i4^IV.
5. Retrieve the IV by calculating IV^i4^i4 = IV.
  
Since the implementation use part of the flag as IV, retrieving IV means we can retrieve part of the flag. Use that same process for all three parts and we will retrieve the flag.  
With that process in mind, I made a python script to retrieve the flag:
```
from pwn import *

conn = remote("challenge.ctf.games", 31738)

pieceSize = 16
inputBlock = "22"*pieceSize
inputString = inputBlock*3
flaghex = ''
for i in range(3):
    conn.recvuntil("triforce# ".encode())
    conn.send(str(i + 1).encode())
    conn.recvuntil("select# ".encode())
    conn.send("2".encode())
    conn.recvuntil("decrypt> ".encode())
    conn.send(inputString.encode())
    conn.recvuntil("SPOKEN: \n".encode())
    out = conn.recvlineS(keepends=False)
    print(f"o{i+1}0= {out}")
    conn.recvuntil("select# ".encode())
    
    o1 = out[:pieceSize*2]
    print(f"o{i+1}1= {o1}")
    o2 = out[pieceSize*2:pieceSize*4]
    print(f"o{i+1}2= {o2}")
    o3 = out[pieceSize*4:pieceSize*6]
    print(f"o{i+1}3= {o3}")
    f = str(hex(int(o1,16)^int(o2,16)^int(inputBlock, 16)))[2:]
    print(f"f{i+1}=  {f}")
    flaghex+=f
    print()

    conn.send("3".encode())

conn.close()
print("The flag is: " + bytearray.fromhex(flaghex).decode())
```
Executing it gave the output:
```
$ python3 solve.py
[+] Opening connection to challenge.ctf.games on port 31738: Done
o10= 84c8feba8b02d89fce005c8738e1d1d2c086bdffd218cb848a1b1a9d7efbc0c7c086bdffd218cb848a1b1a9d7efbc0c7
o11= 84c8feba8b02d89fce005c8738e1d1d2
o12= c086bdffd218cb848a1b1a9d7efbc0c7
o13= c086bdffd218cb848a1b1a9d7efbc0c7
f1=  666c61677b3831396639643864383337

o20= 375657616eea8e1f51bb44a890781bab2745142078ab980941fb57bc87635fba2745142078ab980941fb57bc87635fba
o21= 375657616eea8e1f51bb44a890781bab
o22= 2745142078ab980941fb57bc87635fba
o23= 2745142078ab980941fb57bc87635fba
f2=  32316163346334343262313635396633

o30= e452f17b089cd4342f23d4baa222812cf014b56b4ec3d6362d21d6b8a020832ef014b56b4ec3d6362d21d6b8a020832e
o31= e452f17b089cd4342f23d4baa222812c
o32= f014b56b4ec3d6362d21d6b8a020832e
o33= f014b56b4ec3d6362d21d6b8a020832e
f3=  36646632647d20202020202020202020

[*] Closed connection to challenge.ctf.games port 31738
The flag is: flag{819f9d8d83721ac4c442b1659f36df2d}
```
The flag is: 
```
flag{819f9d8d83721ac4c442b1659f36df2d}
```
