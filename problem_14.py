#!/usr/bin/env python

import operator

collatz = {}

for i in range(2, 1000000):
	l = 0
	n = i
	while n > 1:
		if i in collatz:
			l += collatz[i]
			break
		else:	
			if n % 2 == 0:
				n = int(n / 2)
				l += 1
			else:
				n = int((3 * n) + 1)
				l += 1			
	collatz[i] = l + 1
print(max(collatz.items(), key=operator.itemgetter(1))[0])