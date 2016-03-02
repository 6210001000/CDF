#!/usr/bin/python
print "Content-type: text/html\n\n"
               

def nreplace(n):
	w = n.replace('0','')
	v = w.replace('9','')
	return v

def coreDigit(n):
	nreplace(n)
	core = sum(map(int,n))
	while(len(str(core)) > 1):
		core = sum(map(int,str(core)))
	return core

ldiff = len(largeNumber) - len(nreplace(largeNumber))

print "<!DOCTYPE html>\n<html>\n<head>\n\t<title>Python Core Digit Finder</title>\n</head>\n<body>\n"	
print "<h3>Core Digit Finder (Python)</h3><p><strong>Current Benchmark</strong>: 480 million digits of Pi<br/>Process code is only 6 lines and highly efficient!</p>"
print "Input Number: " + largeNumber + "<br/>"
print "Input Length: ", len(largeNumber) ," digits<br/><br/>"
print "Modified Number: "
print(nreplace(largeNumber))
print "<br/>Modified Length: ", len(nreplace(largeNumber)) ," digits<br/><br/>"
print "Length Difference <small>(saves on computation time)</small>: " + str(ldiff) + " digits<br/>"
print "<br/><strong>Core Digit is: "
print(coreDigit(largeNumber))
print "</strong><br/><br/>"
print "</body>\n</html>"

# Mersenne Primes (44)
mp_ = [2,3,5,7,
       13,17,19,31,61,89,
       107,127,521,607,
       1279,2203,2281,3217,4253,4423,9689,9941,
       11213,19937,21701,23209,44497,86243,
       110503,132049,216091,756839,859433,
       1257787,1398269,2976221,3021377,6972593,
       13466917,20996011,24036583,25964951,30402457,32582657]
mpc_ = [2,3,5,7,4,8,1,4,7,8,8,1,8,4,1,7,4,4,5,4,5,5,8,2,2,7,1,5,1,1,1,2,5,1,2,2,5,5,1,1,4,5,7,2]
# Mersenne Primes where p is Prime in 2^p - 1 (first 12 numbers in sequence)
mp = ['3','7','31','127','8191','131071','524287','2147483647','2305843009213693951','618970019642690137449562111','162259276829213363391578010288127','170141183460469231731687303715884105727']
mpc = ['3','7','4','1','1','4','1','1','1','4','4','1']
mpdc = ['1','1','2','3','4','6','6','10','19','27','33','39']
mpdco = ['0','1','1','1','2','0','4','9','8','6','6']