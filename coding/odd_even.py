# author husuisheng
def Odd_num(n):
	n=3*n+5
	return n
'''
def Even_num(n):
	k=1
	n=n/2^k
	return n
'''


 def main():
        n=449
        i=201
        while (i>0) :
                n=Odd_num(n)
                i=i-1
                print (n,i)            
        print (n)

