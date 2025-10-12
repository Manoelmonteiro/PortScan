import socket
import csv
from sys import argv, exit

def abre_arquivo_csv(nome_arquivo):
    porta_desc= []

    with open(nome_arquivo, mode='r') as file:
        tabela = csv.reader(file)
        for row in tabela:
            if len(row) >= 4 and row[0] != 'NA':
                try:
                    porta = int(row[0])               # converte porta para int
                except ValueError:
                    continue                          # pula linhas com porta inválida
                porta_desc.append((porta, row[1], row[2], row[3]))
    return porta_desc



def scan_Port (alvo, portInitial, portEnd):
    print("Iniciando o scan de portas...")
    print("Port	             |  Protocol   |  Service	  |   Description\n")
    porta_desc = abre_arquivo_csv('ports_services.csv')
    for port in range(portInitial, portEnd):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        try:
            result = s.connect_ex ((alvo, port))
            if result == 0:
                for i in porta_desc:
                    if (i[0]) == port:
                        print(f"Porta {port} esta aberta | {i[1]} |  {i[2]} |  {i[3]}")
                        break
                else:
                    print(f"Porta {port} esta aberta | Desconhecido | Desconhecido | Desconhecido")
                    pass
        except exception as e:
            print(f"Erro ao checar porta {port}: {e}")
            pass
        finally:
            s.close()


if __name__ == "__main__":
    if len(argv) != 4:
        print("Uso: python portscan.py <alvo> <porta inicial> <porta final>. porta max 65535")
        exit()
    print(argv)

    alvo = (argv[1])
    portInitial = int(argv[2])  
    portEnd = int(argv[3])

    scan_Port(alvo, portInitial, portEnd)



