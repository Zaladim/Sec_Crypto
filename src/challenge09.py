#!/usr/bin/env python3

import sys
import base64
from Crypto.Cipher import AES
from errors import *

def ecb_decrypt(text, key):
	cipher = AES.new(key, AES.MODE_ECB)
	return (pad((cipher.decrypt(text)), AES.block_size))

def cbc_decrypt(text, key, iv):
	plain = b''
	prev = iv

	for i in range(0, len(text), AES.block_size):
		current = text[i:i + AES.block_size]
		decrypted = ecb_decrypt(current, key)
		plain += bytes([b1 ^ b2 for b1, b2 in zip(prev, decrypted)])
		prev = current
	return plain

def main():
	try:
		file = checkFile(9)
		# iv = b'\x00' * AES.block_size
		# key = b'YELLOW SUBMARINE'
		key = bytes.fromhex(file.readline().rstrip("\r\n"))
		iv = bytes.fromhex(file.readline().rstrip("\r\n"))
		text = pad(base64.b64decode(file.readline().rstrip("\r\n")), AES.block_size)
		if (not(key) or not(iv) or not(text)):
			raise ValueError
		print(encode64(cbc_decrypt(text, key, iv)).upper())


	except ValueError:
		fileError()


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


def pad(input, size):
	if len(input) == size:
		return input
	padding_length = size - len(input) % size
	padding = bytes([padding_length] * padding_length)
	return (input + padding)

def unpad(input):
	padding = input[-input[-1]:]
	if not all(padding[byte] == len(padding) for byte in range(0, len(padding))):
		return input
	return input[:-input[-1]]



if __name__ == "__main__":
	main()