#!/usr/bin/env python

import math

def getDivisors(n) :
	divisors = []
	# Note that this loop runs till square root 
	i = 1
	while i <= math.sqrt(n): 
		if (n % i == 0) : 
			# If divisors are equal, get only one 
			if (n / i == i) : 
				divisors += [i], 
			else : 
				# Otherwise get both 
				divisors += [i, n/i] 
		i = i + 1
	return divisors

if __name__ == '__main__':
	i = 1
	while True:
		if(len(getDivisors(i)) == 500):
			break
		i += 1
	print(i)		