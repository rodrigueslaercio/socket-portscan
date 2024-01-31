import socket 
from datetime import date, datetime

host = input("Host: ")
ports = []
opens = []

while True:
    port = input("Ports (type q to quit): ")
    if port == 'q':
        break
    
    ports.append(int(port))

for port in ports:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(0.1)
    connection = client.connect_ex((host, port))
    
    if connection == 0:
        opens.append(port)    

file = open(f"open_portscan_{date.today()}_{datetime.now().strftime('%H-%M-%S')}.txt", "w")
file.write(f"Open ports: {opens}")
        
file.close()
        