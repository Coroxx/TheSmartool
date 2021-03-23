# Programme développé par Corox, début du projet le 28/11.
#coding: utf-8

# Tous les imports : 
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
from getmac import get_mac_address as gma
from random import randint

COLORS = {\
"black":"\u001b[30;1m",
"red": "\u001b[31;1m",
"green":"\u001b[32m",
"yellow":"\u001b[33;1m",
"blue":"\u001b[34;1m",
"lightgreen" : "\u001b[38;5;82m",
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

# ------------------------------------------------------------- Début du Code -----------------------------------------------
print(colorText("       \n    [[yellow]][+] Checking your internet connection.\033[39m"))
time.sleep(1)
print(colorText("    [[yellow]][+] Checking your internet connection..\033[39m"))
time.sleep(1)
print(colorText("    [[yellow]][+] Checking your internet connection...\033[39m"))
url = "http://www.google.com" #Je définit l'url de test
timeout = 5 # Timeout de 5 secondes 

#Puis le test d'une requête sur l'url
try:
    os.system('clear')
    request = requests.get(url, timeout=timeout)
    b = open("Banner/connected.txt",'r')
    connected = "".join(b.readlines())
    print(colorText(connected))
    print(colorText("[[green]][!] This script must be run on full screen for optimal use. ! "))
    print(colorText("[[green]][!] This script must be run on full screen for optimal use. ! "))
    time.sleep(5)
    os.system("clear")
except (requests.ConnectionError, requests.Timeout) as exception:
    print(colorText('                 /-[[red]]Internet [NOT CONNECTED][[white]]-\ '))
    print(colorText('    [[green]] ✘ [[red]] You must be connected to internet to start this script [[green]] ✘'))
    time.sleep(5)
    sys.exit()


def phrase() :
    global phrasee
    a = randint(1,6)
    if a == 1 :
        phrasee = 'You died - Dark Souls'
    elif a == 2 :
        phrasee = 'I know kung fu - The Matrix'
    elif a == 3 : 
        phrasee = 'ꜰɪɴɪꜱʜ ʜɪᴍ! – ᴍᴏʀᴛᴀʟ ᴋᴏᴍʙᴀᴛ'
    elif a == 4  :
        phrasee = 'Ɛղժմɾҽ ąղժ ʂմɾѵìѵҽ. – Ͳհҽ Ꝉąʂէ օƒ Աʂ'
    elif a == 5 : 
        phrasee  = 'DEATH IS A PREFERABLE ALTERNATIVE TO COMMUNISM – Fallout 3'
    elif a == 6 : 
        phrasee = 'No Russian. – Call of Duty: Modern Warfare 2'
    return phrasee

phrase()



f = open("Banner/smarthub.txt","r")
ff = 'Banner/smarthub.txt'
ascii = "".join(f.readlines())
filee = ('Banner/banner.txt')

couleurs = ['red','yellow','green','magenta','cyan','blue']
long = len(couleurs)
x = randint(0, long-1)

file = open('Banner/banner.txt', 'w')
tot = '[[' + couleurs[x] + ']]' + '\n    ███████╗███╗   ███╗ █████╗ ██████╗ ████████╗ ██████╗  ██████╗ ██╗\n    ██╔════╝████╗ ████║██╔══██╗██╔══██╗╚══██╔══╝██╔═══██╗██╔═══██╗██║  [[red]]   Version 0.5' + '[[' + couleurs[x] + ']]' '\n    ███████╗██╔████╔██║███████║██████╔╝   ██║   ██║   ██║██║   ██║██║  [[magenta]]    By @Coroxx' + '[[' + couleurs[x] + ']]' + '\n    ╚════██║██║╚██╔╝██║██╔══██║██╔══██╗   ██║   ██║   ██║██║   ██║██║  [[magenta]]     Github.com/Coroxx/TheSmartool' + '[[' + couleurs[x] + ']]' + '\n    ███████║██║ ╚═╝ ██║██║  ██║██║  ██║   ██║   ╚██████╔╝╚██████╔╝███████╗\n The╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝  ' + phrasee + '\n\n'
file.write(tot)
file.close()

f = open("Banner/banner.txt","r")
ascii = "".join(f.readlines())

os.system('clear')


def conditions () : 
    result = input(colorText("[[yellow]][ ? ] Using this script for illegal activites ? \n\ny/n : "))
    if result != "y" and result != "n" : 
        print(colorText("[[red]]Wrong answer !!"))
        conditions()
    else : 
        if result == "y" :
            print(colorText("\n[[red]]This script is for educational use ONLY ! "))
            time.sleep(5)
            sys.exit()
        elif result == 'n':
            pass

conditions()
os.system('clear')
print(colorText(ascii))

# HUB PRINCIPAL
def lobby():
    
    d = open("Banner/banner-hub.txt","r")
    asciii = "".join(d.readlines())
    print(colorText(asciii))
    hub = input(colorText("[[cyan]][ 1 ] Information about an ip adress \n[ 2 ] Start Metasploit \n[ 3 ] Password  \n[ 4 ] View Mac Adress\n[ 5 ] SmartProxyDownloader (Download fresh proxies easily) \n[ 6 ] SmartProxyChecker\n[ 7 ] SmartAdminPageFinder (find easily the admin pannel of a website)\n\n[ 99 ] Exit \n\n[ ? ] Choice : "))
    try :
        val = int(hub)
    except ValueError :
        print(colorText("[[red]][-] Error, choose an option between 1 and 4 "))
        lobby()
    if val == 99 :
        print(colorText("[[red]]Exiting..."))
        time.sleep(3)
        os.system("clear")
        sys.exit()
    if val >= 8 :
        print(colorText("[[red]][-] Error, choose an option between 1 and 4"))
        lobby()
    if val == 1 :
        lobby1()
    elif val == 2 :
        os.system('clear')
        print(colorText("[[red]][+] LAUNCHING METASPLOIT... "))
        os.system('msfconsole')
    elif val == 3 : 
        lobby2()
    elif val == 4 :
        print("\n",gma(),'\n')
        lobby()
    elif val == 5 : 
        os.system("sudo python3 proxydownloader.py")
    elif val == 6 :
        os.system('sudo python3 proxychecker.py')
    elif val == 7 : 
        os.system('python3 adminpagefinder.py')
        os.system('clear')



# PREMIER CHOIX
def lobby1() : 
    a = open("Banner/ipbanner.txt","r")
    asciiii = "".join(a.readlines())
    print(colorText(asciiii))
    hub1 = input(colorText("[[cyan]][ 1 ] Expiration / Create date (Domain) \n[ 2 ] Domain alive ? \n[ 3 ] Ping an IP / Domain (ms) \n[ 4 ] What is my ip adress ?  \n[ 5 ] Back \n\n[ ? ] Choice : "))
    try :
        val1 = int(hub1)
    except ValueError :
        print(colorText("\n[[red]][-] Error, choose an option between 1 and 4"))
        lobby()
    if val1 >= 6 : 
        print(colorText("\n[[red]][-] Error, choose an option between 1 and 4"))
        lobby1()
    if val1 == 1 : 
        target = input("Website domain (ex google.com) : ")
        if 'https'in target :
            print(colorText('[[red]]\n[-] Wrong format ! (Correct format : xxxxx.fr'))
            lobby1()
        elif 'http' in target : 
            print(colorText('[[red]]\n[-] Wrong format ! (Correct format : xxxxx.fr'))
            lobby1()
        elif '/' in target : 
            print(colorText('[[red]]\n[-] Wrong format ! (Correct format : xxxxx.fr'))
            lobby1()
        domain = whois.query(target)
        print (colorText("[[green]][+] Domain expire date :"), domain.expiration_date)
        print (colorText("[[green]][+] Domain creation date :"), domain.creation_date)
        lobby1()
    if val1 == 2 : 
        target = input("Website domain (ex google.com) : ")
        response = os.system ("ping -c 1 -w2 " + target + " > /dev/null 2>&1")
        if response == 0 :
            print(colorText("\n[[green]][+] Website Up !\n "))
            lobby1()
        else :
            print(colorText("[[red]][-] Website down :( "))
            lobby1()
    if val1 == 3 : 
        ip = str(input("\nIp adress or domain (ex google.com) : "))
        print("\n")
        commande = ("ping -c 5 {}").format(ip)
        os.system(commande)
        lobby1()
    if val1 == 4 : 
        userip()
    if val1 == 5 : 
        lobby()
    
    
def password() :
    a48 = input("How many characters in length ? :")
    try : 
        longg = int(a48)
    except ValueError:
        print(colorText("[[red]][-] ERROR !  "))
        lobby2()
    chars = input("Special characters  (y/n) ? ")
    if chars != 'y' and chars != 'n':
        print(colorText("\n [[red]][-]ERROR ! Your choice must be : y or n !! \n"))
        password()
    if chars == 'y' :
        print (colorText("\n[[magenta]][+] Your Smart-Password is : "),''.join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase + string.punctuation, k=longg)))
    if chars == 'n' : 
        print (colorText("\n[[magenta]][+] Your Smart-Password is : "),''.join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase , k=longg)))
    continuee = input("[ ? ]Generate a new password ? y/n :  ")
    if continuee != "y" and continuee != "n" : 
        print(colorText("\n [[red]][-] ERROR ! Your choice must be : y or n !! \n"))
    if continuee == 'y' :
        password()
    elif continuee == 'n' : 
        lobby2()

def lobby2():
    z = open("Banner/passwordbanner.txt","r")
    passs = "".join(z.readlines())
    print(colorText(passs))
    print("\n")
    hub2 = input("[ 1 ] Password generator \n[ 2 ] Smart FTP Bruteforcer\n[ 3 ] Smart SSH Bruteforcer \n[ 4 ] Back \n\n[ ? ] Choice : \n")
    try : 
        val2 = int(hub2)
    except ValueError : 
        print(colorText("\n[[red]][-] ERROR ! Choose an option between 1 and 4"))
        lobby2()
    if val2 >= 5 : 
        print(colorText("\n[[red]][-] ERROR ! Choose an option between 1 and 4"))
        lobby2()
    if val2 == 1 :
        password()
    if val2 == 2 :
        os.system('sudo python3 smartftpbruteforcer.py')
    if val2 == 3 :
        os.system('sudo python3 ssh-cracker.py')
    if val2 == 4 : 
        lobby()

def update():
    url = "https://gist.github.com/Coroxx/514d7e3953daa2fad0fd2d8f18722c60"
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, "html.parser")
    for script in soup(["script", "style"]):
        script.extract()    
    text = soup.get_text()
    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    text = '\n'.join(chunk for chunk in chunks if chunk)
    if "update required" in text :
        print(colorText("[[yellow]][+] There is an update on my Github Page !"))
    else : 
        print(colorText("[[green]][+] This script is running on the lastest version"))
    userip()

def userip():
    url = "https://ident.me"
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, "html.parser")
    for script in soup(["sript", "style"]):
        script.extract()
    text = soup.get_text()
    print(colorText('\n[[cyan]][+] Your IP Adress is :'), text)

if os.geteuid()==0:
  print (colorText("[[cyan]][+] Running as root (No reboot required). \n"))
else:
  print ("[-] You didn't launch this script with the root privileges ! ")
  time.sleep(5)
  sys.exit()

import signal
import sys






update()
lobby()

