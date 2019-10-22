#!/usr/bin/env python3

import sys
import base64
from Crypto.Cipher import AES
from errors import *

def count(text, size):
	blocks = [text[i:i+size] for i in range(0, len(text), size)]
	rep = len(blocks) - len(set(blocks))
	return rep

def main():
	try:
		file = checkFile(8)
		text = [base64.b64decode(line.strip()) for line in file]
		# text = [bytes.fromhex(line.strip()) for line in file]
		reps = [count(cipher, 16) for cipher in text]

		max = 0
		line = 1
		for i in range(len(reps)):
			if (reps[i]> max):
				max = reps[i]
				line = i + 1

		print(line)

	except ValueError:
		fileError()



if __name__ == "__main__":
	main()