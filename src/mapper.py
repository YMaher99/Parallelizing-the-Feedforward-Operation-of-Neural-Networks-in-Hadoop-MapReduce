#!/usr/bin/env python

import sys

cache_info = open("cache.txt").readlines()[0].split(",")
row_a, col_b = map(int,cache_info)

for line in sys.stdin:
	matrix_index, row, col, value = line.rstrip().split(",")
	if matrix_index == "A":
		for i in range(0,col_b):
			key = row + "," + str(i)
			print (f"{key}\t{col}\t{value}")
	else:
		for j in range(0,row_a):
			key = str(j) + "," + col 
			print (f"{key}\t{row}\t{value}")

