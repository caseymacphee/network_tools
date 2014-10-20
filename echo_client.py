import socket

def run_client():
	client_socket = socket.socket(
		socket.AF_INET,
		socket.SOCK_STREAM,
		socket.IPPROTO_IP
		)
	client_socket.connect(('127.0.0.1', 50000))
	print __name__
	if __name__ == '__builtin__' or __name__ == '__main__' or __name__ == 'echo_client':
		message = raw_input("What would you like to send? ('quit' to shutdown server)\n: ")
		client_socket.sendall(message)
		client_socket.shutdown(socket.SHUT_WR)
		print client_socket.recv(32)
		client_socket.close()
	else:
		message = 'test'
		client_socket.sendall(message)
		#client_socket.shutdown(socket.SHUT_WR)
		callback = client_socket.recv(32)
		client_socket.sendall('quit')
		client_socket.shutdown(socket.SHUT_WR)
		print callback
		client_socket.close()

		return callback
