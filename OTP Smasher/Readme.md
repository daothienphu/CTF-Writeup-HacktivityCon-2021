# H@cktivityCon: OTP Smasher
 
![warmup category](https://img.shields.io/badge/Category-Warmups-brightgreen.svg)  
![score](https://img.shields.io/badge/Score_after_CTF-283-blue.svg)  
![solves](https://img.shields.io/badge/Solves-141-lightgrey.svg) 

## Description
Your fingers too slow to smash, tbh.

## Attached files
- None

## Summary
Download the images, read the numbers with an ocr tool, then submit the numbers until we get the flag.

## Flag
```
flag{f994cd9c756675b743b10c44b32e36b6}
```

## Detailed solution
Openning the provided site, we can see an image with white text on black background and a counter on the top left corner. The title and clue suggested that we should submit the text from the image and the counter would go up. However, inputting manually is impossible since there is a timeout. 
<p align="center">
  <img src="https://user-images.githubusercontent.com/55624202/133945684-40c55af9-988e-44ae-9dc1-c126ad948fb3.png" />
</p>
Checking the website resource, we can see that the website only has one submit form, the numbers image and a hidden flag image.
<p align="center">
  <img src="https://user-images.githubusercontent.com/55624202/133948210-13a75757-9196-43ca-b78e-ea4bdcc377b3.png" />
</p>
 
My thought process for this challenge was first to download the image, run an OCR tool to read the number, then submit that number to the website.  
I obtained to code for downloading images from this blog: https://www.thepythoncode.com/article/download-web-page-images-python  
And the code for submitting forms from this blog: https://www.thepythoncode.com/article/extracting-and-submitting-web-page-forms-in-python  
After some testing, it turned out that ```tesseract```, the OCR tool I used, cannot read white text on black background, so before reading the numbers, I need to invert the image with ```imagemagick```.
```
$ convert otp.png -channel RGB -negate otp.png | tesseract otp.png otp --dpi 150
```
Since I had no idea how many OTP i need to smash, I left it in a while loop.
```
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import subprocess
from requests_html import HTMLSession

def getAllImages(url):
    soup = BeautifulSoup(requests.get(url).content, "html.parser")

    urls = []
    for img in soup.find_all("img"):
        img_url = img.attrs.get("src")
        if not img_url:
            continue
        
        img_url = urljoin(url, img_url)
        try:
            pos = img_url.index("?")
            img_url = img_url[:pos]
        except ValueError:
            pass
        
        urls.append(img_url)
    return urls

def download(url):
    response = requests.get(url, stream=True)
    filename = url.split("/")[-1]
    with open(filename, "wb") as f:
        f.write(response.content)
        
def readImg(filename):
    res = ""
    with open(filename) as f:
        res = f.readline()
    return res

def getSubmitForm(url):
    res = session.get(url)
    soup = BeautifulSoup(res.html.html, "html.parser")
    return soup.find("form")

def getFormDetails(form):
    details = {}
    action = form.attrs.get("action").lower()
    method = form.attrs.get("method", "get").lower()
    inputs = []
    for inputTag in form.find_all("input"):
        inputType = inputTag.attrs.get("type", "text")
        inputName = inputTag.attrs.get("name")
        inputValue =inputTag.attrs.get("value", "")
        inputs.append({"type": inputType, "name": inputName, "value": inputValue})
        
    details["action"] = action
    details["method"] = method
    details["inputs"] = inputs
    return details


url = "http://challenge.ctf.games:30336"
while True:
    imgs = getAllImages(url)
    for img in imgs:
        download(img)
        
    cmd = "convert otp.png -channel RGB -negate otp.png | tesseract otp.png otp --dpi 150"
    subprocess.call(cmd, shell=True)

    session = HTMLSession()
    submitForm = getSubmitForm(url)
    formDetails = getFormDetails(submitForm)
    data = {}
    for inputTag in formDetails["inputs"]:
        if inputTag["type"] == "text":
            value = readImg("otp.txt").rstrip()
            data[inputTag["name"]] = value
        elif inputTag["type"] != "submit":
            value = "Submit"
            data[input_tag["name"]] = value
            
    url = urljoin(url, formDetails["action"])

    res = session.post(url, data=data)
```
After leaving it for a while and reloading the page, I found the flag:
<p align="center">
  <img src="https://user-images.githubusercontent.com/55624202/133948121-2a9f6c95-5b3d-4af7-8ef3-7a62e179d331.png" />
</p>

The flag is:
```
flag{f994cd9c756675b743b10c44b32e36b6}
```
