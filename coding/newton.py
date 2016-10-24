# newton
x=9999999999999999999.0
n=0

def y_1(x):
	y=4*x**3+1
	return y

def y_0(x):
	y=x**4+x-10
	return y

def x_0(x):
	y=x-y_0(x)/y_1(x)
	return y

while n<180:
	x=x_0(x)
	print n , x
	n=n+1

