network_tools
=============
The http server in webroot is a basic multi threaded server that can handle GET requests utilizing only the HTTP 1.1 protocol.
The unit testing must be done using a seperate process to run the http server.
The HTTP server has 3 paths / which prints the current time, /content1 which prints some content from the disk, and directory1 which prints the contents of a folder to the website.