import socket
from sys import argv, exit


def scan_Port (alvo, portInitial, portEnd):
    for port in range(portInitial, portEnd):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = s.connect_ex ((alvo, port))
        if result == 0:
            print(f"Porta {port} ta abrida")
        else:
            pass

if __name__ == "__main__":
    if len(argv) != 4:
        print("Uso: python portscan.py <alvo> <porta inicial> <porta final>. porta max 65535")
        exit()
    print(argv)

    alvo = (argv[1])
    portInitial = int(argv[2])  
    portEnd = int(argv[3])

    scan_Port(alvo, portInitial, portEnd)



