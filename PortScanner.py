import socket

ip = input("Insert the IP adress that you want to scan: ")

for port in range(1, 65535):

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(5)

    result = sock.connect_ex((ip, port))

    if result == 0:
        print(f"The port {port} is open.")
        sock.close()