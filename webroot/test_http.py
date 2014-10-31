import pytest
import socket

### Must have http_server running in a seperate process ###
def run_client(message):
	client_socket = socket.socket(
		socket.AF_INET,
		socket.SOCK_STREAM,
		socket.IPPROTO_IP
		)
	client_socket.connect(('127.0.0.1', 5000))
	client_socket.sendall(message)
	client_socket.shutdown(socket.SHUT_WR)
	callback = client_socket.recv(32)
	client_socket.close()
	return callback

def test_send():
	callback = run_client("HTTP/1.1 / GET\r\n\r\n")
	assert '200 OK' in callback

def test_bad_call():
	callback = run_client("HTTP/1.0 /GET\r\n")
	assert '400 Bad Request' in callback

def test_non_get():
	callback = run_client("HTTP/1.1")
	assert '400 Bad Request' in callback

