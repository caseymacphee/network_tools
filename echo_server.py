import socket
import wsgiref.headers 

def run_server():
	server_socket = socket.socket(
		socket.AF_INET,
		socket.SOCK_STREAM,
		socket.IPPROTO_IP
		)
	server_socket.bind(('127.0.0.1', 50000))

	server_socket.listen(1)
	## listening loop
	while True:
		print 'Listening...'
		conn, addr = server_socket.accept()
		clientmessage = conn.recv(32)
		if clientmessage.rstrip() == 'exit' or clientmessage.rstrip() == 'quit':
			conn.close()
			print 'Exiting...'
			break
		else:
			print "the raw message is" + clientmessage 
			HTTPmessage = clientmessage.split('\r\n')
			print len(HTTPmessage)
			for requestlines in HTTPmessage:
				print requestlines

			HTTPargs = HTTPmessage[0].split('/')
			for i, arguments in enumerate(HTTPargs):
				HTTPargs[i] = arguments.rstrip()


			print HTTPargs
			if 'GET' not in HTTPargs or '/' not in HTTPargs:
				message = throw_error('GET')
			else:
				if '1.0' in HTTPargs:
					clientmessage = conn.recv(32)
					if clientmessage == '\r\n':
						message = 'HTTP/1.0 200 OK\r\n'
						conn.sendall(message)

				elif '1.1' in HTTPargs:
					clientmessage = conn.recv(32)
					if clientmessage == '\r\n':
						message = 'HTTP/1.1 200 OK\r\n'
				else:
					message = 'HTTP/ 200 OK\r\n'
					conn.sendall(message)
					conn.close
					print "Exiting..."
					break
		conn.close()
	#Outside the loop
	server_socket.close()

def throw_error(errortype):
	if errortype == 'GET':
		return 'HTTP 400 Bad Request\r\n'
