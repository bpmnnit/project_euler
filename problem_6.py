#!/usr/bin/env python

sum_of_squares = 0
square_of_sum = 0
for i in range(1, 101):
	sum_of_squares += i*i
	square_of_sum += i
square_of_sum = square_of_sum * square_of_sum

print square_of_sum - sum_of_squares