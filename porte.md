import socket

def scan_ports(target, start_port, end_port):
    open_ports = []

    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        result = sock.connect_ex((target, port)) #

        if result == 0:
            open_ports.append(port)

        sock.close()

    return open_ports

target_host = "192.168.50.101" #input("Inserisci l'indirizzo IP del target: ")
start_port = int(input("Inserisci la porta iniziale dello scan: "))
end_port = int(input("Inserisci la porta finale dello scan: "))

open_ports = scan_ports(target_host, start_port, end_port)

if open_ports:
	print(f"Porte aperte su {target_host}: {open_ports}")
else:
        print(f"Nessuna porta aperta trovata su {target_host}")
