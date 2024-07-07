#!/usr/bin/python
from string import ascii_uppercase as au, digits as ds

band_name= input()

f= open ("list.txt", "w")

for l in au:
	for d in ds:
		for n in band_name:
			f.write("{}{}{}\n".format(l, d, n))
f.close()
