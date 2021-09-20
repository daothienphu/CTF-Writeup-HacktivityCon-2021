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
print(intro.decode())
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
