import socket
from sys import argv, exit

LHOST = "192.168.1.1"


def scanPort (alvo, portInitial, portEnd):
    for port in range(portInitial, portEnd):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = s.connect_ex ((alvo, port))
        if result == 0:
            print(f"Port {port} is open")
        else:
            pass



if __name__ == "__main__":

    alvo = (argv[1])
    portInitial = int(argv[2])  
    portEnd = int(argv[3])
    scanPort(alvo, portInitial, portEnd)



