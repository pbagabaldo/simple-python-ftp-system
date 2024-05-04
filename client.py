#client.py

import socket

# Server details
server_name = 'localhost'
server_port = 1234

class ServerConnection:
    def __init__(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((server_name, server_port))
    
    def send_command(self, command):
        """ Sends a command to the server and prints the server's response. """
        self.client_socket.send(command.encode('utf-8'))

        response = self.client_socket.recv(4096).decode('utf-8')  
        print(response)

    def close_connection(self):
        """ Closes the connection to the server. """
        self.client_socket.close()

def main():
    connection = ServerConnection()
    try:
        while True:
            cmd = input("Enter command (LS, GET <filename>, PUT <filename>, EXIT): ")
            if cmd == "LS":
                connection.send_command("LS")
            elif cmd.startswith("GET "):
                filename = cmd.split(" ")[1]
                connection.send_command(f"GET:{filename}")
            elif cmd.startswith("PUT "):
                filename = cmd.split(" ")[1]
                connection.send_command(f"PUT:{filename}")
            elif cmd == "EXIT":
                connection.send_command("EXIT")
                break
            else:
                print("Unknown command")
    finally:
        connection.close_connection()
        print("Connection closed.")

if __name__ == "__main__":
    main()