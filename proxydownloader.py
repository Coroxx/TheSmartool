import requests
import socket 
import socketserver
import urllib
from urllib.request import urlopen
try : 
    import wget
except (ImportError, ImportWarning, ModuleNotFoundError):
    pass
import os
import sys
import time


os.system('clear')

# PROXY DOWNLOADER BY @COROXX ON GITHUB !

COLORS = {\
"black":"\u001b[30;1m",
"red": "\u001b[31;1m",
"green":"\u001b[32m",
"yellow":"\u001b[33;1m",
"blue":"\u001b[34;1m",
"magenta":"\u001b[35m",
"lightgreen" : "\u001b[38;5;82m",
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
    request = requests.get(url, timeout = 5)
    os.system("clear")
    print(colorText("[[green]][+] Connected !\n[+] Connected ! "))
    time.sleep(3)
    os.system("clear")
except (TimeoutError, requests.ConnectionError, requests.ConnectTimeout) as exception : 
    print(colorText("[[red]][-] You're connected to internet ! Exiting..."))
    time.sleep(3)
    os.system("clear")
    sys.exit()


if os.geteuid()==0:
      print ("[+] Running as root (No reboot required). \n")
else:
  print ("[-] You didn't launch this script with the root privileges ! ")
  time.sleep(5)
  sys.exit()

def iscorrectchoice(result, fonction) :
    try : 
        global correct
        correct = int(result)
    except ValueError : 
        print(colorText("\n[[red]][!] Invalid choice !\n "))
        fonction()

def cleanup() : 
    print(colorText("[[red]][!] Warning ! After typing \"y\" all the folder's content will be deleted ! (Your choice will not have consequences for the first usage)"))
    result = input("\ny/n : ")
    if result != 'y' and result != 'n' : 
        print(colorText("\n[[red]][!] Invalid choice !\n"))
        cleanup()
    elif result == 'y' : 
        os.system('mkdir Proxy')
        os.system('rm -r Proxy*')
        os.system('mkdir Proxy')
        os.system('mkdir Proxy/http')
        os.system('mkdir Proxy/socks4')
        os.system('mkdir Proxy/socks5')
        os.system('clear')
    elif result == 'n' : 
        print(colorText("[[red]]Exiting..."))
        time.sleep(3)
        os.system('clear')
        sys.exit()

cleanup()

def hub():
    result1 = input(colorText("[[yellow]]What type of fresh proxies ? :\n\n[ 1 ] HTTP PROXIES\n[ 2 ] SOCKS4 PROXIES\n[ 3 ] SOCKS5 PROXIES\n\n[ 99 ] Exit \n\n[ ? ] Choice ? : "))
    iscorrectchoice(result1, hub)
    if correct == 99 :
        print(colorText("[[red]]\n[-]Exiting..."))
        time.sleep(3)
        os.system("clear")
        sys.exit()
    if correct >= 4 :
        print(colorText("\n[[red]][!] Invalid choice !\n"))
        hub()
    if correct == 1 :
        anonchoice = input(colorText("\n[[red]]Choose your anonymity\n\n[ 1 ] Elite (Strong anonymity, slower) \n[ 2 ] Anonymous (The middle way)\n[ 3 ] Transparent (Worst anonymity, faster)\n[ 99 ] Back \n\n[ ? ] Choice ? : ")) 
        iscorrectchoice(anonchoice, hub)
        if correct == 99 :
            hub()
        if correct == 1 :
            url ='https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=elite&simplified=true'
            urllib.request.urlretrieve(url, 'Proxy/http/httpelite.txt')
            print(colorText("\n\n[[lightgreen]][+] Succes ! File location : Proxy/http/httpelite.txt\n"))
            time.sleep(2)
            hub()
        elif correct == 2 : 
            url = 'https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=anonymous&simplified=true'
            urllib.request.urlretrieve(url, 'Proxy/http/httpanonymous.txt')
            print(colorText("\n\n[[lightgreen]][+] Succes ! File location : Proxy/http/httpanonymous.txt\n"))
            time.sleep(2)
            hub()
        elif correct == 3 : 
            url = 'https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=transparent&simplified=true'
            urllib.request.urlretrieve(url, 'Proxy/http/httptransparent.txt')
            print(colorText("\n\n[[lightgreen]][+] Succes ! File location : Proxy/http/httptransparent.txt\n"))
            time.sleep(2)
            hub()
    elif correct == 2 : 
        url = 'https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks4&timeout=10000&country=all&simplified=true'
        urllib.request.urlretrieve(url, 'Proxy/socks4/socks4.txt')
        print(colorText("\n\n[[lightgreen]][+] Succes ! File location : Proxy/socks4/socks4.txt\n"))
        time.sleep(2)
        hub()
    elif correct == 3 :
        url = 'https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=10000&country=all'
        urllib.request.urlretrieve(url, 'Proxy/socks5/socks5.txt')
        print(colorText("\n\n[[lightgreen]][+] Succes ! File location : Proxy/socks5/socks5.txt\n"))
        time.sleep(2)
        hub()

hub()

# By Coroxx on github
