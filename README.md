# simple-python-ftp-system
We are tasked in creating a mini-version of a File Transfer Protocol system as our final programming project for our Computer Communications Class in Cal State Fullerton. (CPSC-471)

### Protocol Design ###

#### Message Types: ####
- **RequestFile**
- **SendFile**
- **FileNotFound**
- **Acknowledge**

#### Format of Messages: ####
- Each message consists of a **Header** and a **Payload**.

#### Message Exchanges for Setting up a File Transfer Channel: ####
1. **Client Sends RequestFile:**
   - The client sends a **RequestFile** message with the name of the desired file.

2. **Server Receives Request and Responds:**
   - The server receives the request and checks if the requested file exists.
   - If the file exists, the server responds with **SendFile**.
   - If the file does not exist, the server responds with **FileNotFound**.

3. **Client Recieves File Data or Error**
   - **Acknowledge** message.

#### TCP Buffer Management ####
   - Implement flow control mechanisms to avoid overflowing TCP buffers.
   - Utilize techniques such as windowing and congestion control to manage the flow of data between the client and server.

#### Starting and Stopping File Transfer ####
   - The server initiates the file transfer by sending the **SendFile** message.
   - Upon receiving the **SendFile** message, the client begins to receive the file data.
   - File data transmission from the server halts once the entire file has been sent.
   - The client ceases to receive file data upon completion of file transmission.

#### Error Handling ####
   - Use error messages to communicate error conditions between client and server.