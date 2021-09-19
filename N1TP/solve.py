from pwn import *
from binascii import unhexlify

def xorHex(h1, h2):
    return hex(int(h1,16)^int(h2, 16))


conn = remote("challenge.ctf.games", 31575)

conn.recvuntil("look!\n".encode())
flag = conn.recvlineS(keepends=False).lstrip()
conn.recvuntil("> ".encode())

inp = "a"*(len(flag)//2)
conn.send(inp.encode())

conn.recvuntil("something?\n".encode())
out = conn.recvlineS(keepends=False).lstrip()

conn.close()

inp = inp.encode().hex()

key = xorHex(inp, out)
flag = xorHex(key, flag)

print("The flag is: " + unhexlify(str(flag)[2:]).decode())
