#!/usr/bin/env python

f = open('p022_names.txt', 'r')
s = ''
for line in f:
	s = sorted([i[1:-1] for i in line.split(',')])
d = {}
j = 1
for i in range(65, 91):
	d[chr(i)] = j
	j += 1
total = 0	
for name in s:
	t = 0
	for letter in name:
		t += d[letter]
	total += t * (s.index(name) + 1)
print(total)