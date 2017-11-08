#!/usr/bin/python
from urlparse import urlparse
import sys
for line in sys.stdin:
	data = line.strip().split('"')
	if len(data) == 3:
		file_path = data[1].split()
		if file_path:
			print str(urlparse(file_path[1]).path)
