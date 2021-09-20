# H@cktivityCon: Oddball
 
![warmup category](https://img.shields.io/badge/Category-Warmups-brightgreen.svg)  
![score](https://img.shields.io/badge/Score_after_CTF-103-blue.svg)  
![solves](https://img.shields.io/badge/Solves-189-lightgrey.svg) 

## Description
Well this file sure is... odd...

## Attached files
- oddball

## Summary
The file is an octal dump of the flag.

## Flag
```
flag{2a522c26c87af3192b42c34fd326385b}
```

## Detailed solution
Running ```file``` on the file revealed that it's an ASCII file.
```
$ file oddball
oddball: ASCII text
```
The content of the file appeared to be an octal dump of the flag. 
```
0000000 067531 020165 067165 067543 062566 062562 020144 064164
0000020 020145 062563 071143 072145 066440 071545 060563 062547
0000040 035440 005051 072516 061155 071145 020163 067151 071040
0000060 067141 062547 030040 033455 020077 066510 066555 020041
0000100 067510 020167 062157 005041 063012 060554 075547 060462
0000120 031065 061462 033062 034143 060467 031546 034461 061062
0000140 031064 031543 063064 031544 033062 034063 061065 005175
0000160
```
I failed to find any tool to reverse octal dump, so I wrote my own.  
To understand how to turn data into octal numbers, let's take an example input 
```
"abcd"
``` 
which in binary is 
```
"01100001 01100010 01100011 01100100"
```
As the name suggests, octal dump works with octal numbers 0 - 7 (000 - 111). Therefore, each octal number can hold a maximum 3 bits of data.  
Since a byte has 8 bits, 2 bytes are encrypted together with a padding P (00) to make up 2\*8+2 = 18 bits = 6 octal numbers.  
Octal dump also works on little-endian systems, so we have to reverse those 2 bytes.  
The input when encoded: 
```
"PbaPdc"
```
or 
```
"00 01100010 01100001 00 01100100 01100011"
```
Grouping them into groups of threes: 
```
"000 110 001 001 100 001 000 110 010 001 100 011"
```
Convert each group into an octal number: 
```
"0 6 1 1 4 1 0 6 2 1 4 3"
``` 
or
```
"061141 062143"
```
Knowing that rule, I wrote the code to reverse the process:
```
def bin2text(b):
	return ''.join(chr(int(''.join(x), 2)) for x in zip(*[iter(b)]*8))

o = ''
lines = ''
with open("oddball.txt") as f:
    lines = f.readlines()
for line in lines:
    o += ''.join(line.rstrip().split(' ')[1:])

s = ''
for i in o:
    s += "{0:03b}".format(int(i))

j = 0
txt = ''
while j < len(s):
    j += 2
    txt += s[(j+8):(j+16)]
    txt += s[j:j+8]
    j += 16

print(bin2text(txt))
```
Executing the code revealed the flag:
```
You uncovered the secret message ;)
Numbers in range 0-7? Hmmm! How od!

flag{2a522c26c87af3192b42c34fd326385b}
```
The flag is:
```
flag{2a522c26c87af3192b42c34fd326385b}
```
