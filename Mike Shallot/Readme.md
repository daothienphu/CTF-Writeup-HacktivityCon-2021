# H@cktivityCon: Mike Shallot
 
![warmup category](https://img.shields.io/badge/Category-OSINT-brightgreen.svg)  
![score](https://img.shields.io/badge/Score_after_CTF-411-blue.svg)  
![solves](https://img.shields.io/badge/Solves-90-lightgrey.svg) 

## Description
Mike Shallot is one shady fella. We are aware of him trying to share some specific intel, but hide it amongst the corners and crevices of internet. Can you find his secret?

## Attached files
- None

## Summary
I found him on Pastebin using Sherlock (https://github.com/sherlock-project/sherlock), then followed the onion link to Stronghold Paste and got the flag.

## Flag
```
flag{6e57a4c0be1656f9bc873647f49b9cdc}
```

## Detailed solution
I used Sherlock and found some websites that had the user mikeshallot:
```
$ python3 sherlock mikeshallot
[*] Checking username mikeshallot on:
[+] Facebook: https://www.facebook.com/mikeshallot
[+] Pastebin: https://pastebin.com/u/mikeshallot
[+] Quizlet: https://quizlet.com/mikeshallot
[+] forum_guns: https://forum.guns.ru/forummisc/blog/mikeshallot
```
The user has one paste called Shallot's Summon:
```
This site is not as safe as we need it to be. 
Meet me in the dark and I will share my secret with you.

Find me in the shadows, these may act as your light:

strongerw2ise74v3duebgsvug4mehyhlpa7f6kfwnas7zofs3kov7yd

pduplowzp/nndw79
```
The content and the clue from the name Shallot (Onion) both suggested that it's an onion link, so I used Tor browser to access http://strongerw2ise74v3duebgsvug4mehyhlpa7f6kfwnas7zofs3kov7yd.onion/pduplowzp/nndw79

The link led to a Stronghold Paste's paste named Shallot's Secrets with the following content:
```
You have met me in the shadows, and you seem to know your way around the dark. I will share my secret with you:
  
flag{6e57a4c0be1656f9bc873647f49b9cdc}
```
The flag is:
```
flag{6e57a4c0be1656f9bc873647f49b9cdc}
```
