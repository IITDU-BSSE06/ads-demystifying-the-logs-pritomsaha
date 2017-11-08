#!/usr/bin/python
import sys
dic = {}
years = ["2009", "2010", "2011"]
for line in sys.stdin:
	year = line.strip()
	dic[year] = dic.get(year, 0) + 1
max_hitted_year = max(dic, key=dic.get)
for year in years:
	print year+"\t"+str(dic.get(year, 0))
print "most hitted year and number of hit: "+str(max_hitted_year)+"\t"+ str(dic[max_hitted_year])
