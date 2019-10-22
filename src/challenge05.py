#!/usr/bin/env python3

import sys
import base64
from errors import *

def repeating_key_XOR(message, key):
	output = b''
	i = 0
	for byte in message:
		output += bytes([byte ^ key[i]])
		i = 0 if i + 1 == len(key) else i + 1
	return output

def main():
	try:
		file = checkFile(5)
		content = file.read().splitlines()
		key = bytes.fromhex(content[0])
		content.pop(0)
		message = bytes.fromhex("".join(content))
		if (not (message) or not (key)) :
			raise ValueError
		string = repeating_key_XOR(message, key)
		print(string.hex().upper())
	except ValueError:
		fileError()

if __name__ == "__main__":
	main()