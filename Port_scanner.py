import socket

open_ports = []
#costruiamo la nostra funzione
def scan_ports(target, start_port, end_port):

#ciclo per controllo ogni porta in range

	for port in range(start_port, end_port + 1):
	
#creazione oggetto socket per la connessione
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  

#restituisce un output in base alla porta e IP target
		result = sock.connect_ex((target, port)) 

		if result == 0:
			print(f"Porta {port} - Aperta")
		else : 
			print(f"Porta {port} - Chiusa")
#chiusura socket
		sock.close()

	return 0
#utente inserisce IP Target
target_host = input("Inserisci l'indirizzo IP del target: ")
#utente inserisce la prima porta
start_port = int(input("Inserisci la porta iniziale dello scan: "))
#utente inserisce l'ultima porta
end_port = int(input("Inserisci la porta finale dello scan: "))

scan_ports(target_host, start_port, end_port)
# in base al risultato della scansione mostra la lista porte aperte o nessuna lista
if not open_ports:
	print(f"Nessuna porta aperta trovata su {target_host}")
	open_ports.append(port)
else:
    print(open_ports)

