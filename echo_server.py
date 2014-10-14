import socket

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
		if clientmessage == 'exit' or clientmessage == 'quit':
			print 'exiting...'
			break
		else:
			print clientmessage
		if __name__ == '__main__' or __name__ == '__builtin__':
			message = raw_input("What would you like to respond with?\n: ")
		else:
			message = clientmessage
		conn.sendall(message)

	## end loop
	conn.close()
	server_socket.close()
