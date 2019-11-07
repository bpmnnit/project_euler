#!/usr/bin/env python

num = 0
for i in range(1, 1001):
    num += i**i
s = str(num)
print(s[-10:])
