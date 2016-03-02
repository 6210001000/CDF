#!/usr/bin/python
print "Content-type: text/html\n\n"

# Super Large Number (over 1 million digits in length)           

# Remove all digits '0' and '9' from super large number
def nreplace(n):
	w = n.replace('0','').replace('9','')
	return w

# Process super large number down to its single digit (core) recursively
def coreDigit(n):
	nreplace(n)
	core = sum(map(int,n))
	while(len(str(core)) > 1):
		core = sum(map(int,str(core)))
	return core

# Find digit difference between modified and original numbers
ldiff = len(largeNumber) - len(nreplace(largeNumber))

# Simple HTML Output for displaying the results
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