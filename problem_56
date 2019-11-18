#!/usr/bin/env python

def sum_digits(n):
	r = 0
	while n:
		r, n = r + n % 10, n // 10
	return r

total = 0

for a in range(1, 100):
	for b in range(1, 100):
		s = sum_digits(a ** b)
		if total < s:
			total = s

print(total)
