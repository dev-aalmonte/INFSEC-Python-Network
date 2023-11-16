import socket
import ssl

def createTLSSocket(serverIP, serverPort):
    TCPSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    TCPSocket.connect((serverIP, serverPort))

    SSLContent = ssl.create_default_context(
        ssl.Purpose.SERVER_AUTH,
        cafile="ca.ctf"
    )

    return SSLContent.wrap_socket(TCPSocket, server_hostname='client')

serverIP = "127.0.0.1"
serverPort = 9999

data = input("Enter a message: ").encode('utf-8')

serverTCPSocket = createTLSSocket(serverIP, serverPort)
serverTCPSocket.send(data)

data = serverTCPSocket.recv(1024)
print(f"Received: {data}")

serverTCPSocket.close()