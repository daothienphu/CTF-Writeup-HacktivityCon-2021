# H@cktivityCon: N1TP
 
![warmup category](https://img.shields.io/badge/Category-Cryptography-brightgreen.svg)  
![score](https://img.shields.io/badge/Score_after_CTF-50-blue.svg)  
![solves](https://img.shields.io/badge/Solves-300-lightgrey.svg) 

## Description
Nina found some new encryption scheme that she apparently thinks is really cool. She's annoying but she found a flag or something, can you deal with her?

## Attached files
- None

## Summary
The flag is encrypted with a XOR OTP, simply send an key-length input string and xor the result, the string with the ciphered flag to get the flag.

## Flag
```
flag{9276cdb76a3dd6b1f523209cd9c0a11b}
```

## Detailed solution
I connected to their container, which prompted:
```
NINA: Hello! I found a flag, look!
      bc555f7f5143372e768cd2be8a8e61910bbaf559285f601c1237057e1969a2a2bda26ec6e197
NINA: But I encrypted it with a very special nonce, the same length as
      the flag! I heard people say this encryption method is unbreakable!
      I'll even let you encrypt something to prove it!! What should we encrypt?
>
```
"nonce" (means "used once") and "the same length as the flag" suggested that it's encrypted with a one time pad encryption.
I then entered 2 identical strings to confirm my suspicion, and indeed its a padded one time pad.
```
> aaa
NINA: Ta-daaa!! I think this is called a 'one' 'time' 'pad' or something?
      bb585f794b1b6478218ed7bddcd961c30ebfa25a7858344f406454261b6cfaa0eca23e96e28b
NINA: Isn't that cool!?! Want to see it again?
      Sorry, I forget already -- what was it you wanted to see again?
> aaa
NINA: Ta-daaa!! I think this is called a 'one' 'time' 'pad' or something?
      bb585f794b1b6478218ed7bddcd961c30ebfa25a7858344f406454261b6cfaa0eca23e96e28b
NINA: Isn't that cool!?! Want to see it again?
      Sorry, I forget already -- what was it you wanted to see again?
```
Given that this challenge is tagged Easy, I guessed it's just a padded XOR OTP.  
Since they have already given us ```flag```^```key```, we only need to send any input string ```inp``` with the length of the key to get ```inp```^```key```.  
Then we XOR them together: ```flag```^```key```^```inp```^```key``` = ```flag```^```inp```.  
Finally we XOR it with ```inp``` to get the ```flag```: ```flag```^```inp```^```inp``` = ```flag```.
  
To connect with their container, I used the pwntools library which has the handy function ```recvuntil```.
```
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
```

Executing it revealed the flag:
```
$ python3 solve.py
[+] Opening connection to challenge.ctf.games on port 31575: Done
[*] Closed connection to challenge.ctf.games port 31575
The flag is: flag{9276cdb76a3dd6b1f523209cd9c0a11b}
```

The flag is:
```
flag{9276cdb76a3dd6b1f523209cd9c0a11b}
```
