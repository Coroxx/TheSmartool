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


os.system("pip install requests")
os.system("clear")




url = "https://google.com"
try : 
    request = requests.get(url, timeout = 5)
    print(colorText("\n[[green]]Successfuly connected !\nSuccessfuly connected ! "))
    time.sleep(3)
    os.system("clear")
except (requests.ConnectionError, requests.Timeout) as exception : 
    print(colorText("\n[[red]] You're not connected to internet ! "))
    print(colorText("\n[[red]] You're not connected to internet ! ")) 
    time.sleep(3)
    sys.exit() 



print(colorText("[[green]] Installation in progress..."))
os.system("clear")
os.system("sudo bash cmd.sh")





