import http.client
def richiesta(verbo):
    connection = http.client.HTTPConnection(host, port)
    connection.request(verbo, '/')
    response = connection.getresponse()
    print(f"Metodo richiesto: {verbo} - stato:",response.status)
    connection.close()

host = input("inserire host/IP del sistema target: ") 
port = input("inserire la porta del sistema target (default:80): ")
path = "/" + (input("Inserire eventuale path: ")) + "/" #Concatenzione del path

if(port == ""):
    port = 80
    
try: #Esecuzione dei vari tipi di richieste al server
    richiesta("GET")
    richiesta("HEAD")
    richiesta("DELETE")
    richiesta("POST")
    richiesta("OPTIONS") 
except ConnectionRefusedError:
    print("Connessione fallita")
