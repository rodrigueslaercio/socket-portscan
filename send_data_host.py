import socket
from datetime import date, datetime

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = input("Host: ")
port = input("Port: ")
msg_send = input("Data to send: ")
client.connect((host, int(port)))
client.send(str.encode(msg_send))

response = client.recv(1024)

file = open(f"response_host_{date.today()}_{datetime.now().strftime('%H-%M-%S')}.txt", "w")
file.write(response.decode())
file.close()