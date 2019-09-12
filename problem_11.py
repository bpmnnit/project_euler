#!/usr/bin/env python

import pandas as pd

m = pd.read_csv('problem_11.txt', sep=" ", header=None)
n = 20 
product = 0
for i in range(n):
	for j in range(n - 3):
		if (m[i][j] * m[i][j + 1] * m[i][j + 2] * m[i][j + 3]) > product:
			product = (m[i][j] * m[i][j + 1] * m[i][j + 2] * m[i][j + 3])
for i in range(n):
	for j in range(n - 3):
		if (m[j][i] * m[j + 1][i] * m[j + 2][i] * m[j + 3][i]) > product:
			product = (m[j][i] * m[j + 1][i] * m[j + 2][i] * m[j + 3][i])
p = 1
for i in range(3, n):
	y = 0
	x = i
	for j in range(p):
		if (m[x][y] * m[x - 1][y + 1] * m[x - 2][y + 2] * m[x - 3][y + 3]) > product:
			product = (m[x][y] * m[x - 1][y + 1] * m[x - 2][y + 2] * m[x - 3][y + 3])
		x -= 1
		y += 1
	p += 1
p = n - 1
for i in range(1, n):
	y = i
	x = n - 1
	for j in range(p - 3):
		if (m[x][y] * m[x - 1][y + 1] * m[x - 2][y + 2] * m[x - 3][y + 3]) > product:
			product = (m[x][y] * m[x - 1][y + 1] * m[x - 2][y + 2] * m[x - 3][y + 3])
		x -= 1
		y += 1
	p -= 1
p = 1
for i in range(3, n):
	y = i
	x = n - 1
	for j in range(p):
		if (m[x][y] * m[x - 1][y - 1] * m[x - 2][y - 2] * m[x - 3][y - 3]) > product:
			product = (m[x][y] * m[x - 1][y - 1] * m[x - 2][y - 2] * m[x - 3][y - 3])
		x -= 1
		y -= 1
	p += 1
p = n - 1
for i in range(1, n):
	x = 0
	y = i
	for j in range(p - 3):
		if (m[x][y] * m[x + 1][y + 1] * m[x + 2][y + 2] * m[x + 3][y + 3]) > product:
			product = (m[x][y] * m[x + 1][y + 1] * m[x + 2][y + 2] * m[x + 3][y + 3])
		x += 1
		y += 1
	p -= 1

print(product)	