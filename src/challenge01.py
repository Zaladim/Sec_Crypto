#!/usr/bin/env python3

import sys
import base64
from errors import *

b64_index_table = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

def encode64(input):
	output = ""

	bits = list("".join([bin(byte)[2:].zfill(8) for byte in input]))
	blocks = [bits[i:i+6] for i in range(0, len(bits), 6)]

	for block in blocks:
		block = "".join(block)

		if len(block) == 2:
			if "1" in block:
				block += "0000"
				output += b64_index_table[int(block, 2)] + "=="
			else:
				output += "=="
		elif len(block) == 4:
			if "1" in block:
				block += "00"
				output += b64_index_table[int(block, 2)] + "="
			else:
				output += "="
		elif len(block) == 6:
			output += b64_index_table[int(block, 2)]
	return output

def main():
	try:
		file = checkFile(1)
		str = file.read()
		str = str.rstrip("\r\n")
		print(base64.b64encode(bytes.fromhex(str)).decode().upper())
		# print(encode64(bytes.fromhex(str)).upper())
	except ValueError:
		fileError()

if __name__ == "__main__":
	main()