#!/usr/bin/env python
first = 1
second = 1
third = first + second
index = 3
while len(str(third)) < 1000:
	first = second
	second = third
	third = first + second
	index += 1
print(index)	
