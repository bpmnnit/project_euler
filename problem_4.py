#!/usr/bin/env python3

n = 0
for a in range(999, 100, -1):
	for b in range(a, 100, -1):
		x = a * b
		if x > n:
			s = str(x)
			if s == s[::-1]:
				n = x
print(n)
