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
