# server.py
import socket
from command import HandleGet, HandlePut, HandleLs, HandleExit

# the port on which to listen
listen_port = 1234

# create welcome socket
welcome_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Allow the socket to reuse the address (optional, helps avoid issues when restarting)
welcome_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# bind socket to the port
welcome_sock.bind(('', listen_port))

# start listening on the socket
welcome_sock.listen(1)

print('Server is listening on port', listen_port)

def handle_request(client_socket):
    try:
        while True:
            command = client_socket.recv(1024).decode('utf-8')
            if not command:
                break  

            print('Requests Received:', command)
            
            if command.startswith('GET'):
                filename = command.split(':')[1]
                HandleGet(client_socket, filename)
            elif command.startswith('PUT'):
                filename = command.split(':')[1]
                HandlePut(client_socket, filename)
            elif command.startswith('LS'):
                HandleLs(client_socket)
            elif command.startswith('EXIT'):
                HandleExit(client_socket)
                return True
            else:
                client_socket.send(f"Error:UnknownCommand:{command}".encode('utf-8'))
    finally:
        client_socket.close()  # Ensure socket is always closed properly

while True:
    print('Waiting for connections...')
    
    # Accept connections
    client_socket, addr = welcome_sock.accept()
    
    print(f'Accepted connection from client: {addr}')
    
    # Handle requests in a loop until closed by client or an EXIT command
    if handle_request(client_socket):
        welcome_sock.close()
        print('Connection closed with', addr)
        break