#!/usr/bin/python
import sys

for line in sys.stdin:
	data = line.strip().split("- -")
	if len(data) == 2:
		print str(data[0].strip())

