import socket
import time

def recvTimeout(the_socket, oneline ,timeout=4):
    #make socket non blocking
    the_socket.setblocking(0)
    
    #total data partwise in an array
    total_data=[]
    data=''
    
    #beginning time
    begin=time.time()
    while 1:
        #if you got some data, then break after timeout
        if total_data and time.time()-begin > timeout:
            break
        
        #if you got no data at all, wait a little longer, twice the timeout
        elif time.time()-begin > timeout*2:
            break
        
        #recv something
        try:
            data = the_socket.recv(8192)
            if data:
                data = data.decode()
                total_data.append(data)
                #change the beginning time for measurement
                begin = time.time()
            else:
                #sleep for sometime to indicate a gap
                time.sleep(0.1)
        except:
            pass
    
    #join all parts to make final string
    if oneline:
        return ''.join(total_data)
    return total_data

def printData(data):
    for i in data:
        print(i, end="")

def getWord(data):
    return data[-1][:-4]

def getTable(data, secondTime=False):
    if secondTime:
        data = data[6:-3]
    else:
        data = data[3:-3]
    res = []
    for line in data:
        res.append(line[8:-1].split("   "))
    return res

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

                 

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#AF_INET for IPv4, SOCK_STREAM for TCP (as opposed to UDP).
sock.connect(('challenge.ctf.games', 31553))

#receive the initial introduction
intro = recvTimeout(sock, False)
printData(intro)

#send play
sock.send("play\n".encode())
print("play\n")


count = 0
while count < 30:
    time.sleep(5)
    #first time
    data = recvTimeout(sock, False)
    printData(data)

    data = data[-1].split("\n")
    if count > 0:
        table = getTable(data, True)
    else: 
        table = getTable(data)
    word = getWord(data)
    print(word)
    #printData(table)

    res = findWord(word, table)
    #time.sleep(7)
    if res:
        sock.send(res.encode())
    else:
        sock.send("hahaha".encode())
    print(res)
    

    for i in range(4):
        time.sleep(3)
        data = recvTimeout(sock, True)
        print(data, end="")

        word = data[:-4]
        print(word)
        res = findWord(word, table)
        #time.sleep(7)
        if res:
            sock.send(res.encode())
        else:
            sock.send("hahaha".encode())
        print(res)
        
    count += 1

#receive flag
flag = recvTimeout(sock, False)
printData(flag)