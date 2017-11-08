#!/usr/bin/python
import sys
dic = {}
for line in sys.stdin:
	file_path = line.strip()
	dic[file_path] = dic.get(file_path, 0) + 1
max_hitted_file_path = max(dic, key=dic.get)
print max_hitted_file_path+"\t"+str(dic.get(max_hitted_file_path, 0))
