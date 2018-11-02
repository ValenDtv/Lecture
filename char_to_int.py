#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

import sys

s = sys.argv[1]
i = 0
num = 0
R = []
for ch in s[1:]:
	count = 0
	n = ord(ch)
	while n>0:
		n = n//10
		count += 1
	R.append(count)
while i < len(s):
	r = sum(R[i:])
	num += ord(s[i])*(pow(10,r))	
	i+=1
print(num)