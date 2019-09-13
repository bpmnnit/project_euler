#!/usr/bin/env python

import math
sieve = [i for i in range(2, 1000000)]
len_sieve = len(sieve)
new_sieve = []
while(len(sieve) > len_sieve):
	new_sieve = new_sieve + [sieve.pop(0)] # list.pop(n) returns the nth indexed element from list and removes it from the list
	sieve = filter(lambda a: a % new_sieve[-1], sieve)

# New, sieve and new_sieve consists of prime numbers only
for i in reversed(new_sieve):
	if 600851475143 % i == 0:
		print i

# Answer: 6857