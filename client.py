import socket

# name and port number of the server
server_name = "localhost"
server_port = 1234

data = ''

# create socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to server
client_socket.connect((server_name, server_port))

# close socket
client_socket.close()
