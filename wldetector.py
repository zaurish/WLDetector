#!/usr/bin/python3

import sys
from scapy.all import *

print("Welcome to wldetector v0.1")

try:
	ip = input("Select the target IP adress (Ex: 192.168.1.1)--> ")
except:
	print("Incorrect values have been entered")
	sys.exit()

input("Press Enter to start scan")

request = sr1(IP(dst=ip)/ICMP(), verbose = 0, timeout = 1)

if request == None:
	print("No answer")
elif int(request[IP].ttl) <= 64:
	print("This is Linux")
else:
	print("This is Windows")