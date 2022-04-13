#!/usr/bin/python

# - - - - - - - - - - - - - - - - - - - - -
# > IMPORT MODULES
# - - - - - - - - - - - - - - - - - - - - -
import math
import os
import shutil
import time

class CoreDigit:
	lower = '0'
	upper = '9'
	e = ''

	def __init__(self, n):
		self.n = n

	def reduction(self):
		nr = self.n
		nr.replace(CoreDigit.lower,CoreDigit.e)
		nr.replace(CoreDigit.upper,CoreDigit.e)
		return nr

	def removePairs(self):
		digitize = self.n
		max = 5
		digit_list = [int(y) for y in str(digitize)]

		for i in range(1,max):
			list_x = digit_list.count(i)
			list_y = digit_list.count(9 - i)
			lo = str(i)
			hi = str(9 - i)
			if(list_x > list_y):
				digitize.replace(lo,CoreDigit.e,list_y)
				digitize.replace(hi,CoreDigit.e,list_y)
			elif(list_y > list_x):
				digitize.replace(hi,CoreDigit.e,list_x)
				digitize.replace(lo,CoreDigit.e,list_x)
			else:
				digitize.replace(lo,CoreDigit.e,list_x)
				digitize.replace(hi,CoreDigit.e,list_y)

		return digitize

	def finder(self):
		self.reduction()
		self.removePairs()
		core = sum(map(int,self.n))
		while(len(str(core)) > 1):
			core = sum(map(int,str(core)))
		return core

with open('mersenne-primes-cores/M2203.txt', 'r') as processor:
	n = processor.read().replace('\n', '')

num = CoreDigit(n)
print(num.finder())