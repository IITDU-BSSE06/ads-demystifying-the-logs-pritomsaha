#!/usr/bin/python
import sys
for line in sys.stdin:
	data = line.strip().split('"')
	if len(data) == 3 and "HTTP" in data[1]:
		method = data[1].strip().split()
		if method:
			print method[0]
		
