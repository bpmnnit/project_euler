#!/usr/bin/env python3

data = []

f = open('p067_triangle.txt', 'r')
for line in f:
  data += [[int(i) for i in line.split()]]
f.close()

for i in range(len(data) - 2, -1, -1):
  for j in range(i + 1):
    data[i][j] += max(data[i + 1][j], data[i + 1][j + 1])

print(data[0][0])