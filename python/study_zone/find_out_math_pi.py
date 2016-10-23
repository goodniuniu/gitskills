# program for find out what happen in math.pi
from def_my import *
x=move(1,1,1,0)
result =[x,0]
for i in range(361):
	r=move(1,1,1,i*math.pi/180)
	result=[r,i]
	print (result)
	# if (r[0]<0.00000000000001) & int(r[1]==1):
	# print (r[0])
	#if r[0]<=x[0]:
	#	x=r
	#	result =[x,i]	
		# print(x)
		# print (int(r[1]))
	#else:
	#	pass
