import requests
import time
import sys
import os
import whois
import string
from string import punctuation
import random
import zipfile
import urllib
from urllib.request import urlopen
from bs4 import BeautifulSoup
from random import randint
from datetime import datetime
import socket
import urllib3
                            # AdminPageFinder by @Coroxx on Github, Github.com/Coroxx/TheSmartool #


COLORS = {\
"black":"\u001b[30;1m",
"red": "\u001b[31;1m",
"green":"\u001b[32m",
"lightgreen" : "\u001b[38;5;82m",
"lightyellow" : "\u001b[38;5;226m",
"yellow":"\u001b[33;1m",
"blue":"\u001b[34;1m",
"magenta":"\u001b[35m",
"cyan": "\u001b[36m",
"white":"\u001b[37m",
"yellow-background":"\u001b[43m",
"black-background":"\u001b[40m",
"cyan-background":"\u001b[46;1m",
}

def colorText(text):
    for color in COLORS:
        text = text.replace("[[" + color + "]]", COLORS[color])
    return text

url = 'https://www.google.com'

try : 
    os.system('clear')
    request = requests.get(url, timeout = 5)
    print(colorText('[[lightgreen]][+] Connected !\n[+] Connected ! '))
    time.sleep(3)
    os.system('clear')
except (TimeoutError, requests.Timeout, requests.ConnectTimeout, requests.ConnectionError) as exception : 
    os.system('clear')
    print(colorText('[[red]][-] You\'re not connected to internet :('))
    print(colorText('\n\n[-] Exiting...'))
    time.sleep(3)
    os.system('clear')
    sys.exit()


def banner():
     file = open('Banner/adminpagebanner.txt', 'r')
     ascii = "".join(file.readlines())
     print(colorText(ascii))

def hub() :
    global url1
    os.system('clear')
    banner()
    time.sleep(2)
    url1 = input(colorText('[[yellow]][ ? ] Url (Format : https://www.xxxxx.com) : '))
    if 'https://' in url1 :
        pass
    elif 'http://' in url1 : 
        pass
    else : 
        print(colorText('[[red]]\n[!] Wrong format !'))
        hub()
    print(colorText('[[yellow]]\n[!] Checking if your site is alive...'))
    time.sleep(2)
    global request
    try : 
        request = requests.get(url1, timeout = 5)
        print(colorText('[[lightgreen]]\n[+] Good !\n'))
    except (TimeoutError,requests.ConnectTimeout, requests.ConnectionError) as exception :
        print(colorText('[[red]]\n[-] Your site is dead !\nAborting...'))
        time.sleep(3)
        hub()
    time.sleep(2)
    now = datetime.now()
    currentime = now.strftime("%H:%M:%S")
    result = '[[white]]' + '[' + currentime + ']' + '[[lightgreen]]' + '[' + 'DEBUG : INFO' + ']' + '[[lightyellow]]' + ':'+ '[[lightyellow]]'+ ' Starting. '
    print(colorText(result))
    time.sleep(1)
    now = datetime.now()
    currentime = now.strftime("%H:%M:%S")
    result = '[[white]]' + '[' + currentime + ']' + '[[lightgreen]]' + '[' + 'DEBUG : INFO' + ']' + '[[lightyellow]]' + ':'+ '[[lightyellow]]'+ ' Starting.. '
    print(colorText(result))
    time.sleep(1)
    now = datetime.now()
    currentime = now.strftime("%H:%M:%S")
    result = '[[white]]' + '[' + currentime + ']' + '[[lightgreen]]' + '[' + 'DEBUG : INFO' + ']' + '[[lightyellow]]' + ':'+ '[[lightyellow]]'+ ' Starting...\n '
    print(colorText(result))
    time.sleep(1)
    print(colorText('[[red]]\n[!] If the site requires a user login, the scan may fail\n'))
    time.sleep(1)

hub()

d = open('adminlink.txt', 'r')
dam = open('adminlink.txt').read().split("\n")
longueur = len(dam)
resultt = []


for i in range(longueur - 1) :
    global req 
    url = url1 + '/' + dam[i]
    req = urllib.request.Request(url, None, {'User-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'})
    now = datetime.now()
    currentime = now.strftime("%H:%M:%S")
    result = '[[white]]' + '[' + currentime + ']' + '[[lightgreen]]' + '[' + 'DEBUG : INFO' + ']' + '[[lightyellow]]' + ':'+ '[[lightyellow]]'+ ' Trying : ' + url
    print(colorText(result))
    request = requests.get(url, timeout = 3)
    try :
        html = urllib.request.urlopen(req).read()
        now = datetime.now()
        currentime = now.strftime("%H:%M:%S")
        result = '[[white]]' + '[' + currentime + ']' + '[[lightgreen]]' + '[' + 'DEBUG : RESULT' + ']' + '[[lightgreen]]' + ':'+  '[[lightgreen]]' + ' Pannel found ! : ' + url
        print(colorText(result))
        resultt.append(url)
    except (requests.HTTPError, urllib.error.HTTPError, socket.timeout, requests.exceptions.ReadTimeout, urllib3.exceptions.ReadTimeoutError, socket.gaierror) :
        now = datetime.now()
        currentime = now.strftime("%H:%M:%S")
        result = '[[white]]' + '[' + currentime + ']' + '[[lightgreen]]' + '[' + 'DEBUG : INFO' + ']' + '[[red]]' + ':'+ ' Fail... : ' + url
        print(colorText(result))


def fin() : 
    bons = len(resultt)
    if bons >= 1 :
        for liness in resultt : 
            if 'wp-login.php' in liness :
                result = '[[white]]' + '\n[' + currentime + ']' + '[[lightgreen]]' + '[' + 'DEBUG : INFO' + ']' + '[[yellow]]' + ':'+ 'The script detected that this site could be a wordpress site due to the login page \'wp-login.php\', do you want to use a WordpressBruteForce tool ? y/n : '
                reult = input(colorText(result))
                if reult != 'y' and reult != 'n' : 
                    print(colorText('[[red]][!] Wrong answer !'))
                    fin()
                elif reult == 'y' :
                    print(colorText('\n Unfortunately, I haven\'t developed the bruteforcer yet, be patient :)'))
                    time.sleep(3)
                elif reult == 'n' : 
                    print('')
            else : 
                pass 
    else :
        print(colorText('[[red]]\n\nEnd... Page found : 0 :('))
        time.sleep(3)
        print(colorText('[[red]][-] Exiting....'))
        time.sleep(1)
        sys.exit
    print(colorText('[[lightgreen]]\n\nSucces ! Page(s) found : {}\n').format(bons))
    for i in range(bons) :
        print(resultt[i],"\n")
fin()



# By Coroxx on Github




    

