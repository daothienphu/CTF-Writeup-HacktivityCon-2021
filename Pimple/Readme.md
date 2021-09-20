# H@cktivityCon: Pimple
 
![warmup category](https://img.shields.io/badge/Category-Warmups-brightgreen.svg)  
![score](https://img.shields.io/badge/Score_after_CTF-50-blue.svg)  
![solves](https://img.shields.io/badge/Solves-791-lightgrey.svg) 

## Description
This challenge is simple, it's just a pimple!

## Attached files
- pimple

## Summary
The file is a GIMP file containing the flag

## Flag
```
flag{9a64bc4a390cb0ce31452820ee562c3f}
```

## Detailed solution
Running ```file``` on the file revealed that it's a GIMP file. 
```
$ file pimple
pimple: GIMP XCF image data, version 011, 1024 x 1024, RGB Color
```
Openning it in GIMP revealed 10 layers of images:
<p align="center">
  <img src="https://user-images.githubusercontent.com/55624202/133950012-360ae19f-2da5-44d4-8c20-678e6f3eac33.png">
</p>
The seventh layer contains the flag:
<p align="center">
  <img src="https://user-images.githubusercontent.com/55624202/133950091-d2048435-4ff1-4415-8675-47a87f330d6f.png">
</p>  
  
The flag is:  
```
flag{9a64bc4a390cb0ce31452820ee562c3f}
```
