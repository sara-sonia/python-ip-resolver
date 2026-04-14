import socket

hostname = "example.com"

ip_address = socket.gethostbyname(hostname)

print(f"Hello! The IP address of {hostname} is {ip_address}")
