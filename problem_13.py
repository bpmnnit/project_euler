#!/usr/bin/env python

f = open('problem_13.txt', 'r')

total_sum = 0
for line in f:
	print line
	total_sum = total_sum + int(line)

print total_sum