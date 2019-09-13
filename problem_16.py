#!/usr/bin/env python

s = str(2**1000)

sum_of_digits = 0
for i in s:
	sum_of_digits = sum_of_digits + int(i)

print sum_of_digits	