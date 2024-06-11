import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.settimeout(1)

try:
    client.connect(("127.0.0.1", 4422 ))
    client.send(b"MENSAGEM\n")
    receivedPackets = client.recv(1024).decode()
    print(receivedPackets)
except Exception as error:
    print("Um erro aconteceu")
