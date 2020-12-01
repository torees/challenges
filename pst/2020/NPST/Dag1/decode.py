#!/usr/bin/python
# -*- coding: utf8 -*-
import os, sys, codecs

scrambled = "RUVJgkJqPåGtFgvLwnKilgp"
diff = -2
def main():
	unscrambled=""
	for char in range(len(scrambled)):
			
			newchar = chr(ord(scrambled[char])+ diff)
			unscrambled = unscrambled + newchar

	print(unscrambled) 

main()
