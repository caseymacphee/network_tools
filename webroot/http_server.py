import datetime
from make_time import *
from gevent.server import StreamServer



def handle(socket, address):
	
	print 'Listening...'
	clientmessage = socket.recv(32)
	HTTPmessage = clientmessage.split('\r\n')

	HTTPargs = HTTPmessage[0].split(' ')
	for i, arguments in enumerate(HTTPargs):
		HTTPargs[i] = arguments.rstrip()

	if 'GET' not in HTTPargs:
		print 'inside bad request'
		message = throw_error('GET')
		socket.sendall(message)
	else:
		if 'HTTP/1.1' in HTTPargs:
			clientmessage = socket.recv(32)

			if HTTPargs[1] == '/content1':
				header = get_header(HTTPargs[1])
			elif HTTPargs[1] == '/content2':
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
	if arg == '/content1':
		content = "This could be the path to the content in file 1"
	elif arg == '/content2':
		content = "this could be the path to the content in file 2"
	else:
		time = datetime.datetime.now().isoformat()
		print_time()
		file = open('a_web_page.html', 'r')
		htmlcontent = file.read()
		file.close()
		newhtmlcontent = htmlcontent.format(time)
	header = """

HTTP/1.0 200 OK

{}


"""
##.format(newhtmlcontent)

	return header

def throw_error(errortype):
	if errortype == 'GET':
		return """

HTTP/1.1 400 Bad Request

<html><body>
<h2>Request must be a GET request</h2>
</body></html>

"""
	elif errortype =='HTTP':
		return """

HTTP/ 400 Bad Request

<html><body>
<h2>HTTP request must be of type 1.1</h2>
</body></html>

"""
if __name__ == '__main__':
	server = StreamServer(('127.0.0.1', 5000), handle)
	server.serve_forever()
