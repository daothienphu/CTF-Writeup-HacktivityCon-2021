import requests
import os
from tqdm import tqdm
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import subprocess
import time
from requests_html import HTMLSession
import webbrowser

def get_all_images(url):
    """
    Returns all image URLs on a single `url`
    """
    soup = BeautifulSoup(requests.get(url).content, "html.parser")

    urls = []
    for img in soup.find_all("img"):
        img_url = img.attrs.get("src")
        if not img_url:
            # if img does not contain src attribute, just skip
            continue
        # make the URL absolute by joining domain with the URL that is just extracted
        img_url = urljoin(url, img_url)
        try:
            pos = img_url.index("?")
            img_url = img_url[:pos]
        except ValueError:
            pass
        # finally, if the url is valid
        urls.append(img_url)
    return urls

def download(url):
    """
    Downloads a file given an URL
    """
    # if path doesn't exist, make that path dir
    # download the body of response by chunk, not immediately
    response = requests.get(url, stream=True)
    # get the total file size
    #file_size = int(response.headers.get("Content-Length", 0))
    # get the file name
    filename = url.split("/")[-1]
    # progress bar, changing the unit to bytes instead of iteration (default by tqdm)
    #progress = tqdm(response.iter_content(1024), f"Downloading {filename}", total=file_size, unit="B", unit_scale=True, unit_divisor=1024)
    with open(filename, "wb") as f:
        #for data in progress.iterable:
            # write data read to the file
        f.write(response.content)
            # update the progress bar manually
            #progress.update(len(data))

def readOcr(filename):
    res = ""
    with open(filename) as f:
        res = f.readline()
    return res

def get_all_forms(url):
    """Returns all form tags found on a web page's `url` """
    # GET request
    res = session.get(url)
    # for javascript driven website
    # res.html.render()
    soup = BeautifulSoup(res.html.html, "html.parser")
    return soup.find_all("form")

def get_form_details(form):
    """Returns the HTML details of a form,
    including action, method and list of form controls (inputs, etc)"""
    details = {}
    # get the form action (requested URL)
    action = form.attrs.get("action").lower()
    # get the form method (POST, GET, DELETE, etc)
    # if not specified, GET is the default in HTML
    method = form.attrs.get("method", "get").lower()
    # get all form inputs
    inputs = []
    for input_tag in form.find_all("input"):
        # get type of input form control
        input_type = input_tag.attrs.get("type", "text")
        # get name attribute
        input_name = input_tag.attrs.get("name")
        # get the default value of that input tag
        input_value =input_tag.attrs.get("value", "")
        # add everything to that list
        inputs.append({"type": input_type, "name": input_name, "value": input_value})
    # put everything to the resulting dictionary
    details["action"] = action
    details["method"] = method
    details["inputs"] = inputs
    return details


url = "http://challenge.ctf.games:30133"
count = 0
while True:
    # get all images
    imgs = get_all_images(url)
    for img in imgs:
        # for each image, download it
        download(img)
    cmd = "convert otp.png -channel RGB -negate otp.png | tesseract otp.png otp --dpi 150"
    subprocess.call(cmd, shell=True)

    # initialize an HTTP session
    session = HTMLSession()

    first_form = get_all_forms(url)[0]
    # extract all form details
    form_details = get_form_details(first_form)
    # the data body we want to submit
    data = {}
    for input_tag in form_details["inputs"]:
        if input_tag["type"] == "text":
            # if it's hidden, use the default value
            value = readOcr("otp.txt").rstrip()
            print(value)
            data[input_tag["name"]] = value
        elif input_tag["type"] != "submit":
            # all others except submit, prompt the user to set it
            value = "Submit"
            data[input_tag["name"]] = value
    # join the url with the action (form request URL)
    url = urljoin(url, form_details["action"])

    if form_details["method"] == "post":
        res = session.post(url, data=data)
    elif form_details["method"] == "get":
        res = session.get(url, params=data)
    count += 1
    print(count)


"""
# the below code is only for replacing relative URLs to absolute ones
soup = BeautifulSoup(res.content, "html.parser")
for link in soup.find_all("link"):
    try:
        link.attrs["href"] = urljoin(url, link.attrs["href"])
    except:
        pass
for script in soup.find_all("script"):
    try:
        script.attrs["src"] = urljoin(url, script.attrs["src"])
    except:
        pass
for img in soup.find_all("img"):
    try:
        img.attrs["src"] = urljoin(url, img.attrs["src"])
    except:
        pass
for a in soup.find_all("a"):
    try:
        a.attrs["href"] = urljoin(url, a.attrs["href"])
    except:
        pass

# write the page content to a file
open("page.html", "w").write(str(soup))

# open the page on the default browser
webbrowser.open("page.html")
"""