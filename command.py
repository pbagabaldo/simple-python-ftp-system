# command.py
#This Module is intended to encapsulate the functionalities related to processing commands received by the FTP server
import os

#This function handles the 'GET' command (Sends the file from server to client)
def HandleGet(client_socket, filename):
    files_in_directory = os.listdir('.')

    if filename in files_in_directory:
        client_socket.send(f"SendFile:{filename}".encode('utf-8'))
        with open(filename,'rb') as f:
            while True:
                bytes_read = f.read(1024)
                if not bytes_read:
                    break
                client_socket.send(bytes_read)
    else:
        client_socket.send(f"FileNotFound::{filename}".encode('utf-8'))

#This function handles the 'PUT' command (Client sends file to be stored to server)
def HandlePut(client_socket, filename):
    client_socket.send("Acknowledge:ReadyForFileData".encode('utf-8'))
    data = client_socket.recv(1024)
    with open(filename, 'wb') as f:
        f.write(data)

#This function lists the contents of the server's current directory and sends it back to client
def HandleLs(client_socket):
    files = ' '.join(os.listdir('.'))
    client_socket.send(f"Acknowledge:{files}".encode('utf-8'))

#Exit Command
def HandleExit(client_socket):
    client_socket.send("Bye!".encode('utf-8'))
    client_socket.close()