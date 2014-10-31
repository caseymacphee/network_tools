import datetime
from make_time import *
from gevent.server import StreamServer
import os


def handle(socket, address):
	
	print 'Listening...'
	clientmessage = socket.recv(32)
	HTTPmessage = clientmessage.split('\r\n')

	HTTPargs = HTTPmessage[0].split(' ')
	for i, arguments in enumerate(HTTPargs):
		HTTPargs[i] = arguments.rstrip()

	if 'GET' not in HTTPargs:
		message = throw_error('GET')
		socket.sendall(message)
	else:
		if 'HTTP/1.1' in HTTPargs:
			clientmessage = socket.recv(32)

			if HTTPargs[1] == '/directory':
				header = get_header(HTTPargs[1])
			elif HTTPargs[1] == '/content1':
				header = get_header(HTTPargs[1])
			else:
				header = get_header()
			
			socket.sendall(header)
		else:
			message = throw_error('HTTP')
			socket.sendall(message)

	socket.close()
	#Outside the loop


def get_header(arg = None):
	if arg == '/directory1':
		newhtmlcontent = html_base(os.listdir("images"))
	elif arg == '/content1':
		file = open('sample.txt', 'r')
		txtcontent = file.read()
		file.close()
		newhtmlcontent = html_base(txtcontent)	
	else:
		time = datetime.datetime.now().isoformat()
		print_time()
		file = open('a_web_page.html', 'r')
		htmlcontent = file.read()
		file.close()
		newhtmlcontent = htmlcontent.format(time)
	
	contentlength = len(newhtmlcontent)
	doctype = "text/html; charset=UTF-8"

	header = """

HTTP/1.1 200 OK
Content-Type:{}
Content-Length:{}

{}


""".format(doctype, str(contentlength), newhtmlcontent)

	return header

def throw_error(errortype):
	if errortype == 'GET':
		return """

HTTP/1.1 403 Bad Request

<html><body>
<h2>Request must be a GET request</h2>
</body></html>

"""
	elif errortype =='HTTP':
		return """

HTTP/1.1 400 Bad Request

<html><body>
<h2>HTTP request must be of type 1.1</h2>
</body></html>

"""

def html_base(content):
	return """
<html><body>
	{}
</body></html>
""".format(content)

if __name__ == '__main__':
	server = StreamServer(('127.0.0.1', 5000), handle)
	server.serve_forever()
