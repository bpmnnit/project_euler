#!/usr/bin/env python3

import sys

gs = int(sys.argv[1])
grid = {}
for i in range(gs):
	grid[(i, gs)] = 1
	grid[(gs, i)] = 1

for i in range(gs - 1, -1, -1):
	for j in range(gs - 1, -1, -1):
		grid[(i, j)] = grid[(i + 1, j)] + grid[(i, j + 1)]

print(grid[(0, 0)])
