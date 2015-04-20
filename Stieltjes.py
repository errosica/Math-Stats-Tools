import math

def compute(intervals):
	sum=0
	endpoints = list()
	for i in range(0,intervals+1):
		endpoints.append(endpoint(0,10,float(intervals),i))
		sum = sum + endpoints[i]*(a(endpoints[i])-a(endpoints[i-1]))
		# a check on floating pt error
		print endpoints[i-1], endpoints[i], (a(endpoints[i])-a(endpoints[i-1])), i
		#if (endpoints[i] == 10):  
			#print "TRUE"
		#print 10-endpoints[i]
	return sum

def endpoint(a,b,n,p):
	# interval = [a,b]
	# n is number of subintervals, must be a float
	# returns end of the pth subinterval (0th endpoint marks end of first interval)
	z=0
	for i in range(0,p): #range(0,0) does not execute loop, hence 0th endpoint (beginning of whole interval) is fixed to a
		z = z+ b/n
	a = round(a + z,10)  
	#neccessary to avoid folating point problems with the floor fn
	#as if a+z is even a tiny bit smaller than 10, the fn "a" (which contains the floor fn) will round it to 9. 
	return a

def a(x):
	return x+math.floor(x)


""" This program computes the Reimann-Stieltjes sum as an approximation to the integral 
of the same name defined as 

Lim Sum(f(yi)*[a(ti)-a(ti-1)])
n -> inf

Here f(yi) = yi, and a(x) = x+math.floor(x)

the number of intervals is entered as the parameter to the fn compute,
and the intermediate partitions, or sample points are set at the end of the intervals.
(note that if the integral converges, the distance between sample points at the beginning
and end of the intevals should be epsilon close)."""


