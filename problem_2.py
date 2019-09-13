#!/usr/bin/env python

first = 1
second = 2
third = first + second

total = 0
while third <= 4000000:
	if (third & 1) == 0:
		total += third
	first = second
	second = third
	third = first + second

print total + 2		