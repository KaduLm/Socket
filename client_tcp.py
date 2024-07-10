import socket


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.settimeout(1)

try:
    client.connect(("127.0.0.1", 2266))
    client.send(b"Teste\n")
    pacotes_enviados = client.recv(1024).decode()
    print(pacotes_enviados)

except Exception as error:
    print("Ocorreu um erro:", error)