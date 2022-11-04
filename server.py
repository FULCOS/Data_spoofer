import socket

port = 53

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    test = s.bind(('', port))

    print(test)