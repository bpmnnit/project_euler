#!/usr/bin/env python

m = 999
n = 999
flag = False
while m > 100:
	while n > 100:
		p = str(m * n)
		rev_p = p[::-1]
		if p == rev_p:
			print(p)
			flag = True
			break
		n -= 1
	if flag:
		break
	m -= 1