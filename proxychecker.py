# All the imports : 
#coding: utf-8

import socket 
import requests
import socket 
import socketserver
import urllib
from urllib.request import urlopen
import os
import sys
import time


# PROXY CHECKER ENTIERELY DEVELOPED BY COROXX ON GITHUB


# For colors : 
COLORS = {\
"black":"\u001b[30;1m",
"red": "\u001b[31;1m",
"green":"\u001b[32m",
"yellow":"\u001b[33;1m",
"lightgreen" : "\u001b[38;5;82m",
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

# Check if the user is connected to internet 

try : 
    request = requests.get(url, timeout = 5)
    os.system("clear") #Clear is used to clear the user's terminal
    print (colorText("[[green]][+] Connected to internet !\n[+] Connected to internet !\n"))
    time.sleep(3)
    os.system('clear')
except (TimeoutError, requests.Timeout, requests.ConnectionError, requests.ConnectTimeout) : 
    os.system('clear')
    print(colorText("[[red]][-] You're not connected to internet ! Exiting..."))
    time.sleep(3)
    os.system('clear')
    sys.exit()

if os.geteuid()==0:
      print ("[+] Running as root (No reboot required). \n")
else:
  print (colorText("[[red]]\n[-] You didn't launch this script with the root privileges ! "))
  time.sleep(5)
  sys.exit()


def welcome(): # Welcome page
    global result1
    global x 
    result = input(colorText("[[red]]\n[!] Warning ! After typing \"y\" all the folder's content will be deleted ! (Your choice will not have consequences for the first usage)\n\ny/n : "))
    if result != 'y' and result != 'n' : 
        print(colorText("[[red]][!] Wrong choice !"))
        welcome()
    elif result == 'y' :
        try : 
            os.system('mkdir Results') 
        except : 
            pass
        os.system('rm -r -f Results*') #Delete all the old results
        os.system('clear')
        result1 = input(colorText('[[yellow]][ ? ] Proxy path file (If your text file is already in the \"Smartool\" file, just put : \"hisname.txt\", if your txt is in the \'Proxy\' folder, type "Proxy/http(or socks4...)/....txt  : '))
        if '.txt' in result1 : 
            pass
        else : 
            print(colorText('[[red]][!] Wrong format !'))
            time.sleep(3)
            welcome()
            os.system('clear')
        os.system('clear')
        x = input(colorText('[[yellow]][ ? ] How How many seconds of timeout ? (For example if you enter 3, slow proxies longer than 300 ms will be excluded, 5 is the default value) : '))
        os.system('mkdir Results')
        os.system('touch Results/working.txt') #Creating new txt results
        os.system('touch Results/notworking.txt')
        os.system('clear')
    elif result == 'n' :  #Exiting if the user type "n"
        print(colorText("[[red]][-] Exiting..."))
        time.sleep(3)
        os.system('clear')
        sys.exit()
welcome()


try : 
    global file
    file = open(result1,"r") 
except FileNotFoundError :
    print(colorText('[[red]][-] Your file doesn\'t exist ! Please ty again'))
    time.sleep(3)
    print(colorText('[[red]][-] Exiting...'))
    sys.exit()


host1 = []
port2 = []
result1 = []
port3 = []

# Here is some manipulations to split the port and ip in the user text file

for line in file :
    field = line.split(":")
    host = field[0]
    port = field[1]
    host1.append(host)
    port2.append(port)

for chain in port2 :
    chain = chain.replace('\n', '') # Delete the \n after port in each chain in the list. 
    port3.append(chain)



# Connect to the proxy 
def ping(host, port, af=socket.AF_INET, sock=socket.SOCK_STREAM):
    ping = socket.socket(af, sock)
    socket.setdefaulttimeout(int(x))
    try:
        ping.connect ((host, port))
    except ConnectionRefusedError:
        return False
    except (TimeoutError, socket.timeout, socket.gaierror):
        return False
    else:
        return True
    finally:
        ping.close()

longueur = len(host1) # Lenght of the ip string (how much try)


# Simple warning 
def attention() : 
    print(colorText("[[yellow]][!] Warning :\n\nPinging a proxy can take some time, so be patient, it also depends on your connection.\n[[red]]The script may take some time to launch\n"))
    time.sleep(3)
    input("\nPress enter to continue...")
    os.system("clear")

attention()
# PROXY CHECKER ENTIERELY DEVELOPED BY COROXX ON GITHUB

# Calculating time
def calcultimemin(longueur) :
    calc = longueur
    tot = calc // 20 
    return tot
def calcultimehour(longueur) :
    calc = longueur
    hour = 20 * 60 
    tot = calc // hour 
    return tot 

# And print the result
def timee():
    if longueur == 1 :
        print(colorText('[[cyann]][+] You have 1 proxy to check'))
    else : 
        print(colorText('[[cyan]][+] You have {} proxies to check ').format(longueur))
    print(colorText('[[green]][+] It will take approximately {} minutes / {} hours to finish the check ').format((calcultimemin(longueur)),(calcultimehour(longueur))))
        

timee()

mauvais = 0
bon = 0
tott = 0

unquart = longueur // 4 
deuxquart = unquart * 2
troisquart = unquart * 3


# Loop to check all proxies. 
for i in range(longueur) :
        if ping(host1[i], int(port3[i]), af=socket.AF_INET, sock=socket.SOCK_STREAM) : 
            print(colorText('[[green]]\n\n|IP : {}\n|Port : {}\n|Status : Working !').format(host1[i], port3[i]))
            fichier = open('Results/working.txt', 'a')
            chaine =  host1[i] + ":" + port3[i] + "\n" # Here we write the results into the text file
            fichier.write(chaine)
            fichier.close()
            bon += 1 # Count of 'Working !'
            tott += 1
            if tott == unquart : 
                print(colorText('[[lightgreen]]\nTotal check : 25 % !'))
            elif tott == deuxquart :
                print(colorText('[[lightgreen]]\nTotal check : 50 % !'))
            elif tott == troisquart : 
                print(colorText('[[lightgreen]]\nTotal check : 75 % !'))
            else : 
                pass
        else : 
            print(colorText('[[red]]\n\n|IP : {}\n|Port : {}\n|Status : Not working (or very slow) !').format(host1[i], port3[i]))
            fichier = open('Results/notworking.txt', 'a')
            chaine = host1[i] + ":" + port3[i] + '\n' # Here we write the results into the text file
            fichier.write(chaine)
            fichier.close()
            mauvais += 1 # Count of 'Not working'
            tott += 1
            if tott == unquart : 
                print(colorText('[[lightgreen]]\nTotal check : 25 % !'))
            elif tott == deuxquart :
                print(colorText('[[lightgreen]]\nTotal check : 50 % !'))
            elif tott == troisquart : 
                print(colorText('[[lightgreen]]\nTotal check : 75 % !'))
            else : 
                pass
        


print(colorText('[[yellow]]\n----------Succes ! Total : {} Working : {} Not working : {} ---------- ').format(longueur,bon,mauvais))
