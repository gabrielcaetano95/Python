#!/usr/bin/python3

import sys

def main():

	command = sys.argv[1].lower()
	message = sys.argv[2].lower()

	print(command, message)

if __name__ == '__main__':
	main()