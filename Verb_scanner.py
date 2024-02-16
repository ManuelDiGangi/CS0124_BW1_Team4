# Importo libreria http.client
import http.client 
# Inserimento IP target e Porta	
host = input("inserire host/IP del sistema target: ") 
port = input("inserire la porta del sistema target (default:80): ") 
path = "/" + (input("Inserire eventuale path: ")) + "/" 

def richiesta(verbo):
    	# Gestice la connessione verso l'host passando come parametri indirizzo host e porta
    	# Creo l'oggetto connection
    connection = http.client.HTTPConnection(host, port)
    	# Effettua richiesta al server
     connection.request(verbo, path)
	# Viene utilizzato per ottenere l'oggetto di risposta dalla connessione http
     response = connection.getresponse()
     print(f"Metodo richiesto: {verbo} - stato:",response.status)
	# Chiude la connessione
    connection.close()

#print(path)
# Se la porta è vuota verrà utilizzata la porta di default -> 80 
if(port == ""):
    port = 80
   # Eseguiamo i vari tipi di richieste al server utilizzando i verbi: 
# "get", "post", "delete", "head" e "options". 
try: #Esecuzione dei vari tipi di richieste al server
    richiesta("GET")
    richiesta("HEAD")
    richiesta("DELETE")
    richiesta("POST")
    richiesta("OPTIONS")
# Stampa a video messaggio diconnessione fallita, qualora la connessionevenga rifiutata dal server
except ConnectionRefusedError:
    print("Connessione fallita")
# In questo caso il server può non essere in ascolto sulla porta specificata 
# oppure potrebbero esserci problemi di connessione. 
# L'utente viene avvissato del mancato collegamento. 



