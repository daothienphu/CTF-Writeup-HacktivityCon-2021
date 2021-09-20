# CTF Name: Challenge name
 
![warmup category](https://img.shields.io/badge/Category-Warmups-brightgreen.svg)  
![score](https://img.shields.io/badge/Score_after_CTF-50-blue.svg)  
![solves](https://img.shields.io/badge/Solves-249-lightgrey.svg) 

## Description
Can you hit a moving target?

**Note, this flag contains only 24 hexadecimal characters.**

## Attached files
- target_practice.gif

## Summary
Split the gif into 22 images and pass them through a MaxiCode decoder.

## Flag
```
flag{385e3ae5d7b2ca2510be8ef4}
```

## Detailed solution
The gif (/ɡif/ not /jif/) contains MaxiCode images. To split the gif into several pngs I used imagemagick:
````
$ convert target_practice.gif %02d.png
```
I then manually ran each of them through https://zxing.org/w/decode.jspx , the sixteenth image contains the flag: 
```
nualopohofozqjvbppzbayiihremwd
estaggvnmimpbcvtlrxortjqynieue	
nfltdablbnpzhruspiwekpinumtecc
ksdbwgcqbdbovofguzxfhpdhvwofje
ylfjdbcwtnwdakudxdocztpnsyhwuy
msywbrkuifxoiipkncgaprqkqwkagb
lftpxrgwvkvacbuzxlxahwbgixjlgj
ohtqbjogozzngudcnthdryiiqmsacj
syqixjbncbhbtofakbnpmodydssjgd
ygxcklwuzdwckmsmgztenvpfgbuvfw
gaufepfyqfrsfpskkwjsrpumevymdv
ygxcklwuzdwckmsmgztenvpfgbuvfw
syqixjbncbhbtofakbnpmodydssjgd
ohtqbjogozzngudcnthdryiiqmsacj
lftpxrgwvkvacbuzxlxahwbgixjlgj
flag{385e3ae5d7b2ca2510be8ef4}
```
The flag is:
```
flag{385e3ae5d7b2ca2510be8ef4}
```
