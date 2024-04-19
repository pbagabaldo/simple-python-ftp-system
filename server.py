import socket

# the port on which to listen
listen_port = 1234

# create welcome socket
welcome_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind socket to the port
welcome_sock.bind(('', listen_port))

# start listening on the socket
welcome_sock.listen(1)

while True:
    print('Waiting for connections...')
    
    # accept connections
    client_socket, addr = welcome_sock.accept()
    
    print(f'Accepted connection from client: {addr}')
    print('\n')
    
    # close the connection
    client_socket.close()
