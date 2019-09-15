#!/usr/bin/env python

import math

def properDivisorsSum(n):
	divisors = []
	for i in range(1, int(math.sqrt(n) + 1)):
		if n % i == 0:
			divisors += [i]
			if i > 1 and int(n / i) not in divisors:
				divisors += [int(n / i)]
	total = 0
	for i in divisors:
		total += i
	return total, divisors
			
amicable_numbers = {}

for j in range(100, 10001):
	# d(n) = sum of all proper divisors
	# if d(a) = b and d(b) = a, where a != b, then a and b are amicable numbers
	a, d = properDivisorsSum(j)
	b, e = properDivisorsSum(a)
	if j == b and b != a:
		if a not in amicable_numbers:
			amicable_numbers[a] = d
		if b not in amicable_numbers:
			amicable_numbers[b] = e	
t = 0 # sum of amicable pairs
for i in amicable_numbers:
	t += i
print(amicable_numbers, t)