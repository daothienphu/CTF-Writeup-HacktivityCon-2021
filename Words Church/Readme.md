# H@cktivityCon: Words Church
 
![warmup category](https://img.shields.io/badge/Category-Scripting-brightgreen.svg)  
![score](https://img.shields.io/badge/Score_after_CTF-407-blue.svg)  
![solves](https://img.shields.io/badge/Solves-93-lightgrey.svg) 

## Description
Tired of finding bugs and exploiting vulnerabilities? Want a classic brain buster instead? Why not play a wordsearch -- in fact, why not play thirty word searches!!

## Attached files
- None

## Summary
It's a normal game, still frustrated cuz of the poor backend tho.

## Flag
```
flag{ac670e1f34da9eb748b3f241eb03f51b}
```

## Detailed solution
The process is quite straight forward, they give us a table of 16x16 letters, then give us 5 words, we have to find the coordinates of consecutive letters that make up each word. The letters can be arranged in all 8 orientations and they can wrap around the table. Doing that 30 times and we get the flag. My code to find the words is probably one of the worst you have ever seen.
```
from pwn import *

def findWord(word, table):
    for k in range(16):
        for l in range(16):
            if table[k][l] == word[0]:
                #\ backward
                length = 0
                i,j = k,l
                while i >= 0 and i < 16 and j >= 0 and j < 16 and length < len(word):
                    if word[length] == table[i][j]:
                        length+= 1
                        if length == len(word):
                            break
                        i = (i - 1) % 16
                        j = (j - 1) % 16
                    else:
                        break
                if length == len(word):
                    res = []
                    i,j = k,l
                    for m in range(length):                      
                        res.append((j,i))
                        i-= 1
                        j-= 1
                    return str(res)
                
                #- backward
                length = 0
                i,j = k,l
                while i >= 0 and i < 16 and j >= 0 and j < 16 and length < len(word):
                    if word[length] == table[i][j]:
                        length+= 1
                        if length == len(word):
                            break
                        j = (j - 1) % 16
                    else:
                        break
                if length == len(word):
                    res = []
                    i,j = k,l
                    for m in range(length):
                        res.append((j,i))
                        j-= 1
                    return str(res)

                #/ backward
                length = 0
                i,j = k,l
                while i >= 0 and i < 16 and j >= 0 and j < 16 and length < len(word):
                    if word[length] == table[i][j]:
                        length+= 1
                        if length == len(word):
                            break
                        i = (i + 1) % 16
                        j = (j - 1) % 16
                    else:
                        break
                if length == len(word):
                    res = []
                    i,j = k,l
                    for m in range(length):
                        res.append((j,i))
                        i+= 1
                        j-= 1
                    return str(res)          
                
                #| backward
                length = 0
                i,j = k,l
                while i >= 0 and i < 16 and j >= 0 and j < 16 and length < len(word):
                    if word[length] == table[i][j]:
                        length+= 1
                        if length == len(word):
                            break
                        i = (i - 1) % 16
                    else:
                        break
                if length == len(word):
                    res = []
                    i,j = k,l
                    for m in range(length):
                        res.append((j,i))
                        i-= 1
                    return str(res)

                #- forward
                length = 0
                i,j = k,l
                while i >= 0 and i < 16 and j >= 0 and j < 16 and length < len(word):
                    if word[length] == table[i][j]:
                        length+= 1
                        if length == len(word):
                            break
                        j = (j + 1) % 16
                    else:
                        break
                if length == len(word):
                    res = []
                    i,j = k,l
                    for m in range(length):
                        res.append((j,i))
                        j+= 1
                    return str(res)   
                
                #| forward
                length = 0
                i,j = k,l
                while i >= 0 and i < 16 and j >= 0 and j < 16 and length < len(word):
                    if word[length] == table[i][j]:
                        length+= 1
                        if length == len(word):
                            break
                        i = (i + 1) % 16
                    else:
                        break
                if length == len(word):
                    res = []
                    i,j = k,l
                    for m in range(length):
                        res.append((j,i))
                        i+= 1
                    return str(res)
 
                #\ forward
                length = 0
                i,j = k,l
                while i >= 0 and i < 16 and j >= 0 and j < 16 and length < len(word):
                    if word[length] == table[i][j]:
                        length+= 1
                        if length == len(word):
                            break
                        i = (i + 1) % 16
                        j = (j + 1) % 16
                    else:
                        break
                if length == len(word):
                    res = []
                    i,j = k,l
                    for m in range(length):
                        res.append((j,i))   
                        i+= 1
                        j+= 1
                    return str(res)
                
                #/ forward
                length = 0
                i,j = k,l
                while i >= 0 and i < 16 and j >= 0 and j < 16 and length < len(word):
                    if word[length] == table[i][j]:
                        length+= 1
                        if length == len(word):
                            break
                        i = (i - 1) % 16
                        j = (j + 1) % 16
                    else:
                        break
                if length == len(word):
                    res = []
                    i,j = k,l
                    for m in range(length):
                        res.append((j,i))
                        i-= 1
                        j+= 1
                    return str(res)
                 
conn = remote("challenge.ctf.games", 32751)
intro = conn.recvuntil("> ".encode())
print(intro.decode(), end="")
conn.send("play".encode())
print("play")
count = 0
while count < 30:
    for i in range(5):
        if i == 0:
            print(conn.recvuntil("30:\n".encode()).decode(),end="")
            print(conn.recvlineS(),end="")
            print(conn.recvlineS(),end="")
            table = []
            for i in range(16):
                line = conn.recvlineS()
                print(line, end="")
                table += [line.rstrip()[8:].split("   ")]
            print(conn.recvlineS(),end="")
            print(conn.recvlineS(),end="")

        word = conn.recvuntil("> ".encode()).decode()
        print(word, end="")
        res = findWord(word[:-4], table)
        if res:
            conn.send(res.encode())
            print(res)
        else:
            print("Failed to find word due to poor backend and I'm very frustrated after 3 hours of just relying on luck.")
            exit(0)        
    count += 1

flag = conn.recvuntil("}".encode())
print(flag.decode())
```
Running the code revealed the flag:
```
$ python3 solve.py
[+] Opening connection to challenge.ctf.games on port 32751: Done
Words Church v1.0

Let's play a game of wordsearch! We will display the grid
and offer you words to find. Please submit the locations of
each word in the format [(X,Y), (X,Y), (X,Y), ...] for each letter.

Please enter 'example' if you would like to see an
example, or 'play' if you would like to get started.
> play
Wordsearch # 1/30:

...

Congratulations! You finished that word search!
Onto the next one!

WOW! You solved ALL THE wordsearches!
Here is your victory prize!
flag{ac670e1f34da9eb748b3f241eb03f51b}
```
The flag is:
```
flag{ac670e1f34da9eb748b3f241eb03f51b}
```
