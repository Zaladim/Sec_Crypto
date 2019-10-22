#!/usr/bin/env python3

import sys
import base64
from Crypto.Cipher import AES
from Crypto import Random
from errors import *

def main():
	print(sys.argv)
	size = get_block_size()

def key_randomizer(length):
	start = ord('\x20')
	end = ord('z')
	key = ''
	for i i range(length):
		key += cher(randint(start, end + 1))
	return key

def get_block_size(encrypt):

def encrypter(text):
	size = 16
	key = key_randomizer(16)
	plaintext = pad(text + base64.b64decode(), size)


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