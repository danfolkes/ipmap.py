import urllib2
import sys

i = 0
help = """
	Made by Daniel Folkes
==============================
	Usage: 
		python ipmap.py 74.125.45.100 all
	Args:
		all =	Prints all details
		nomap = Gets All, no map
		loc = 	Gets: Country, Region, City
"""
alen = len(sys.argv)
argz = sys.argv

if alen<=1 or alen>3:
	print help
	quit()

elif alen == 2:
        ip = argz[1]
	comm = "all"
elif alen == 3:
	ip = argz[1]
        comm = argz[2]; #ahrd

req = urllib2.Request("http://www.ipmap.com/"+ip)
response = urllib2.urlopen(req)
pg = response.read()

pg = pg[pg.find('<table'):pg.find('<div id="footer"')]


st = pg.find('<td>')
st2 = pg.find('&nbsp;')
ed = pg.find('</tr')
info0 = pg[st+4:st2]

pg = pg[ed+4:]

st = pg.find('<td>')
st2 = pg.find('&nbsp;')
ed = pg.find('</tr')
info1 = pg[st+4:st2]


pg = pg[ed+4:]

st = pg.find('<td>')
st2 = pg.find('&nbsp;')
ed = pg.find('</tr')
info2 = pg[st+4:st2]

pg = pg[ed+4:]

st = pg.find('<td>')
st2 = pg.find('&nbsp;')
ed = pg.find('</tr')
info3 = pg[st+4:st2]


pg = pg[ed+4:]

st = pg.find('<td>')
st2 = pg.find('&nbsp;')
ed = pg.find('</tr')
info4 = pg[st+4:st2]

pg = pg[ed+4:]

st = pg.find('<td>')
st2 = pg.find('&nbsp;')
ed = pg.find('</tr')
info5 = pg[st+4:st2]


pg = pg[ed+4:]

st = pg.find('<td>')
st2 = pg.find('&nbsp;')
ed = pg.find('</tr')
info6 = pg[st+4:st2]

pg = pg[ed+4:]

st = pg.find('<img src="http://maps.google.com')
st2 = pg.find('"/>')
#ed = pg.find('')
info7 = pg[st:st2+3]


retval = ""
sep = ","
if comm == "nomap":
	retval += info0
	retval += sep
	retval += info1
	retval += sep
	retval += info2
	retval += sep
	retval += info3
	retval += sep
	retval += info4
	retval += sep
	retval += info5
	retval += sep
	retval += info6
elif comm == "loc":
        retval += info3
        retval += sep
        retval += info4
        retval += sep
        retval += info5
else:
        retval += info0
        retval += sep
        retval += info1
        retval += sep
        retval += info2
        retval += sep
        retval += info3
        retval += sep
        retval += info4
        retval += sep
        retval += info5
        retval += sep
        retval += info6
        retval += sep
        retval += info7

print retval
