import socket

open_ports = []

def scan_ports(target, start_port, end_port):

    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
	    #utilizzo protocollo tcp perchè l'udp è un protocollo connectionless e di conseguenza 
	    #non è possibile verificare la risposta della porta

        result = sock.connect_ex((target, port)) 

        if result == 0:
            print(f"Porta {port} - Aperta")
	else : 
	    print(f"Porta {port} - Chiusa")
		
	sock.close()

    return 0

target_host = input("Inserisci l'indirizzo IP del target: ")
start_port = int(input("Inserisci la porta iniziale dello scan: "))
end_port = int(input("Inserisci la porta finale dello scan: "))

scan_ports(target_host, start_port, end_port)

if not open_ports:
        print(f"Nessuna porta aperta trovata su {target_host}")
