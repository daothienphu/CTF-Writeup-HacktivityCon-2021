# H@cktivityCon: Six Four Over Two
 
![warmup category](https://img.shields.io/badge/Category-Warmups-brightgreen.svg)  
![score](https://img.shields.io/badge/Score_after_CTF-50-blue.svg)  
![solves](https://img.shields.io/badge/Solves-1075-lightgrey.svg) 

## Description
I wanted to cover all the bases so I asked my friends what they thought, but they said this challenge was too basic...

## Attached files
- six_four_over_two

## Summary
The file contains a base32 code of the flag

## Flag
```
flag{a45d4e70bfc407645185dd9114f9c0ef}
```

## Detailed solution
Running ```file``` on the file revealed that it's an ASCII file. 
```
$ file six_four_over_two.txt
six_four_over_two: ASCII text, with CRLF line terminators
```
The content of the file is a code, which the title (64/2) suggested that it's a base32 code of the flag.
```
EBTGYYLHPNQTINLEGRSTOMDCMZRTIMBXGY2DKMJYGVSGIOJRGE2GMOLDGBSWM7IK
```
I wrote a script to decode it:
```
from base64 import b32decode
print(b32decode("EBTGYYLHPNQTINLEGRSTOMDCMZRTIMBXGY2DKMJYGVSGIOJRGE2GMOLDGBSWM7IK").decode())
```
Executing it revealed the flag:
```
flag{a45d4e70bfc407645185dd9114f9c0ef}
```
