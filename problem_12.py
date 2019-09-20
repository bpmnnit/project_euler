#!/usr/bin/env python

import math

n = 10
x = 5
div = {1: [1], 3: [1, 3], 6: [1, 2, 3, 6]}
while True:
	div[n] = []
	for i in range(1, int(math.sqrt(n))):
		if n % i == 0:
			if int(n / i) == i:
				div[n] = div[n] + [i]
			else:
				div[n] = div[n] + [int(n / i), i]			
	if len(div[n]) > 500:
		print(n)
		break			
	n = n + x
	x += 1