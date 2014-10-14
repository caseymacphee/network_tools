import pytest
import socket
from echo_server import *
from echo_client import *
import threading
### The server must be running in another terminal 

def test_send():

	serverthread = threading.Thread(target=run_server)
	serverthread.start()

	callback = run_client()
	assert callback == 'test'
	try:
		serverthread.join(10000)
	except RuntimeError:
		pass


