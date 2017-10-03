#Priority Queue (heap queue in Python)
#03/Oct/2017
#Ke

import math
import heapq

def cal_fn(list_a, n):
	res = 0
	for (a,i) in zip(list_a, range(7, -1, -1)):
		res += int(a)*math.pow(n, i)
	return res

#read in k
k = int(raw_input())

#create a k*8 matrix
matrix_a = [[0 for i in range(8)] for i in range(k)]
for i in range(k):
	 matrix_a[i] = raw_input().split()

#read in m
m = int(raw_input())

#creat a heapq and insert k tuple elements
h = []
for (i,_i) in zip(matrix_a, range(0, k)):
	heapq.heappush(h, (cal_fn(i, 1), 1, _i))

#output the mth smallest
for i in range(m):
	v, n, _id = heapq.heappop(h)
	heapq.heappush(h, (cal_fn(matrix_a[_id], n+1), n+1, _id))

print v


