#!/usr/bin/python
import sys
dic = {}
for line in sys.stdin:
	method = line.strip()
	dic[method] = dic.get(method, 0) + 1

for method in dic:
	print method+"\t"+str(dic.get(method, 0))
