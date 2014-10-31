import pytest
import socket
from gevent.pool import Pool

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
	callback2 = client_socket.recv(32)
	callback3 = client_socket.recv(32)
	client_socket.close()
	return callback + callback2 + callback3

def test_send():
	callback = run_client("HTTP/1.1 / GET\r\n\r\n")
	assert '200 OK' in callback

def test_bad_call():
	callback = run_client("HTTP/1.0 /GET\r\n")
	assert '403 Bad Request' in callback

def test_non_get():
	callback = run_client("HTTP / 1.1 /\r\n\r\n")
	assert 'Bad Request' in callback

def test_headers():
	callback = run_client("HTTP/1.1 /content1 GET\r\n\r\n")
	headers = '-Type:text/html; charset=UTF-8'
	assert headers in callback
	assert 'Content-Length:127' in callback
	callback = run_client("HTTP/1.1 / GET\r\n\r\n")
	assert 'Content-Length:188' in callback

def test_multi_request():
	pool = Pool(5)
	pool.map(_multi_request, "HTTP/1.1 /content1 GET \r\n\r\n")

def _multi_request(request_type):
	callback = run_client(request_type)
	assert '200 OK' in callback