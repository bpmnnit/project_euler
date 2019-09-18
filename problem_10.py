#!/usr/bin/env python

import math

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

n = 33
while primes[-1] < 2000000:
	flag = True
	for i in range(int(math.sqrt(n))):
		if n % primes[i] == 0:
			flag = False
			break
	if flag:
		primes += [n]
	n += 2

total = 0
for i in range(len(primes) - 1):
	total += primes[i]
print(total)