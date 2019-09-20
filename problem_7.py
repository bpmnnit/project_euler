#!/usr/bin/env python

import math

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

n = 33
while len(primes) < 10001:
	flag = True
	for i in range(int(math.sqrt(n))):
		if n % primes[i] == 0:
			flag = False
			break
	if flag:
		primes += [n]
	n += 2

print(primes[-1])