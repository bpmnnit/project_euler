#!/usr/bin/env python

import math

f = str(math.factorial(100))
total = 0
for i in f:
	total += int(i)
print(total)