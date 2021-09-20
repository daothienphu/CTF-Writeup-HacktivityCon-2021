# H@cktivityCon: Tsunami
 
![warmup category](https://img.shields.io/badge/Category-Warmups-brightgreen.svg)  
![score](https://img.shields.io/badge/Score_after_CTF-50-blue.svg)  
![solves](https://img.shields.io/badge/Solves-733-lightgrey.svg) 

## Description
Woah! It's a natural disaster! But something doesn't seem so natural about this big wave...

## Attached files
- tsunami

## Summary
The file is a wav file containing the flag in its spectrogram.

## Flag
```
flag{f8fbb2c761821d3af23858f721cc140b}
```

## Detailed solution
Running ```file``` on the file revealed that it's a wav file. 
```
$ file tsunami
tsunami: RIFF (little-endian) data, WAVE audio, Microsoft PCM, 16 bit, stereo 44100 Hz
```
Viewing the spectrogram image of the file in Audacity revealed the flag:
<p align="center">
  <img src="https://user-images.githubusercontent.com/55624202/133950398-87e1a09c-3ae0-4a33-89ed-437fc7d6151f.png"/>
</p>
  
The flag is:
```
flag{f8fbb2c761821d3af23858f721cc140b}
```
