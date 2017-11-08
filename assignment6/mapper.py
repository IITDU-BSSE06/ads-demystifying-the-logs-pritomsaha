#!/usr/bin/python
from urlparse import urlparse
import sys
for line in sys.stdin:
	data = line.strip().split("]")
	if len(data) == 2:
		data2 = data[0].strip().split(":")
		year = data2[0].split("/")[-1]
		if year in ["2009", "2010", "2011"]:
			print year
