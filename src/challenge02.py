#!/usr/bin/env python3

import sys
import base64
from errors import *

def xor_byte(input1, input2):
	return bytes([b1 ^ b2 for b1, b2 in zip(input1, input2)])

def main():
	try:
		file = checkFile(2)
		str1 = file.readline()
		str1 = bytes.fromhex(str1.rstrip("\r\n"))
		str2 = file.readline()
		str2 = bytes.fromhex(str2.rstrip("\r\n"))
		print(xor_byte(str1, str2).hex().upper())
	except ValueError:
		fileError()

if __name__ == "__main__":
	main()