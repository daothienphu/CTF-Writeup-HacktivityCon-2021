# CTF Name: Challenge name
 
![warmup category](https://img.shields.io/badge/Category-Warmups-brightgreen.svg)  
![score](https://img.shields.io/badge/Score_after_CTF-50-blue.svg)  
![solves](https://img.shields.io/badge/Solves-963-lightgrey.svg) 

## Description
It, uh... looks like someone bass-boosted this? Can you make any sense of it?

## Attached files
- bass64

## Summary
The file is an ASCII file with the ASCII art of a base64 code of the flag.

## Flag
```
flag{07cfdc16935bcdd93f14a70f1cb19951}
```

## Detailed solution
Running ```file``` on the file revealed that it's an ASCII file. 
```
$ file bass64
bass64: ASCII text, with very long lines
```

Opening the file revealed it content, which appeared to be an ASCII art of a base64 code.
```
 _____               _     __________              _   _ ____  _   _            _________ __  __      _   _  _ _         _   ___        __  _ _ _________   ___  ____  __  __ ______   __     _   _  ____ _____ _____ __  __  ______   __     __   ______  ___       ___ _____ _    _ __  ____  _____        
|__  /_ __ ___ __  _| |__ |__  /___ / _____      _| \ | |___ \| \ | |_ __ ___  |__  / ___|  \/  |_  _| \ | |(_) | __ ___| \ | \ \      / / | (_)__  / ___| / _ \| ___||  \/  |___ \ \ / /_  _| \ | |/ ___| ____|___ /|  \/  |/ ___\ \ / /__  _\ \ / /___ \|_ _|_  __/ _ \_   _| | _/ |  \/  \ \/ / _ \ _____ 
  / /| '_ ` _ \\ \/ / '_ \  / /  |_ \/ __\ \ /\ / /  \| | __) |  \| | '_ ` _ \   / / |  _| |\/| \ \/ /  \| || | |/ /|_  /  \| |\ \ /\ / /  | | | / / |  _ | | | |___ \| |\/| | __) \ V /\ \/ /  \| | |  _|  _|   |_ \| |\/| | |  _ \ V / \ \/ /\ V /  __) || |\ \/ / | | || | | |/ / | |\/| |\  / | | |_____|
 / /_| | | | | |>  <| | | |/ /_ ___) \__ \\ V  V /| |\  |/ __/| |\  | | | | | | / /| |_| | |  | |>  <| |\  || |   <  / /| |\  | \ V  V / |_| | |/ /| |_| || |_| |___) | |  | |/ __/ | |  >  <| |\  | |_| | |___ ___) | |  | | |_| | | |   >  <  | |  / __/ | | >  <| |_| || | |   <| | |  | |/  \ |_| |_____|
/____|_| |_| |_/_/\_\_| |_/____|____/|___/ \_/\_/ |_| \_|_____|_| \_|_| |_| |_|/____\____|_|  |_/_/\_\_| \_|/ |_|\_\/___|_| \_|  \_/\_/ \___// /____\____| \__\_\____/|_|  |_|_____||_| /_/\_\_| \_|\____|_____|____/|_|  |_|\____| |_|  /_/\_\ |_| |_____|___/_/\_\\___/ |_| |_|\_\_|_|  |_/_/\_\___/       
                                                                                                          |__/                             |__/                                                                                          
```

I manually wrote down the corresponding letters of the code. However, there are certain parts of the code that are intelligible to me. So I typed my version of the code into https://patorjk.com/software/taag/#p=display&f=Standard&t= , which is an ASCII art generator, and compared its output with the content of the file.  
I managed to get ```ZmxhZ3swN2NmZGMxNjkzNWJjZGQ5M2YxNGE3MGYxY2IxOTk1MX0=```, (```0``` and ```O``` is the same after generated, so I tried different permutations until I got the right one).

Plug it into the code:
```
from base64 import b64decode

print(b64decode("ZmxhZ3swN2NmZGMxNjkzNWJjZGQ5M2YxNGE3MGYxY2IxOTk1MX0=").decode())
```
revealed the flag:
```
flag{07cfdc16935bcdd93f14a70f1cb19951}
```
