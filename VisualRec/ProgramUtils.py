import subprocess
import socket
import datetime
import random
import string

def getVersion():
    return 0.1

def getName():
    return "VisualRec 2021 Live"


# DO NOT SHOW THIS
discordWenhook = "https://discord.com/api/webhooks/1254875582911741995/IzPENTnDLg7HR_JqHznS-ZBgkijR4Rj4B0MeaYbWjGmPqszZmtMUILRYMAdapnww0WpM"

def clearScreen():
    subprocess.run("cls", shell=True)

def getMyLocalIP():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('192.255.255.255', 1))
        ip = s.getsockname()[0]
    except:
        ip = '127.0.0.1'
    finally:
        s.close()
    return ip

def getCurrentTime():
  now = datetime.datetime.now()
  currentTime = now.isoformat()
  return currentTime

def setConsoleTitle(Text):
    subprocess.run(f"title {Text}", shell=True)

def webUrl():
    return "https://visualrec.github.io/2021-data/"

def URL():
    return "pr5ndkrl-27614.use.devtunnels.ms"

def DataURL():
    return "pr5ndkrl-9873.use.devtunnels.ms"

def randomString(length=30):
  string1 = ''
  for _ in range(length):
    string1 += random.choice(string.ascii_lowercase + string.digits)
  return string1