#!/usr/bin/python
import sys
hit_num = 0
for line in sys.stdin:
	ip_address = line.strip()
	if ip_address == "10.99.99.186":
		hit_num += 1
print "number of hits were made to 10.99.99.186: "+str(hit_num)
