import numpy as np
from math import sqrt 
err = 1e-3
a = [[4, 3, 0], [3, 1, -1], [0, -1, 1]]
A = np.matrix(a)


def Polly(n, L, A) :
	if n == 0:
		return 1
	if n == 1:
		return (A[0, 0] - L)
	else:
		dn = A[n-1, n-1]
		fn = A[n-2, n-1]
		return (((dn-L) * Polly(n-1, L, A) - fn * fn * Polly(n-2, L, A)))
		
l = len(A)
		
		
def parity(l) :
	if l % 2 == 0:
		return 0
	else:
		return 1	


def printRoot(a, b, err, flag) :
	mid = (a + b) / 2
	while(abs(Polly(l, mid, A)) > err) :
		if Polly(l, mid, A) > 0 and flag == -1:
			b = mid
			mid = (a + b) / 2
		elif Polly(l, mid, A) < 0 and flag == -1:
			a = mid
			mid = (a + b) / 2
		elif Polly(l, mid, A) > 0 and flag == 1:
			a = mid
			mid = (a + b) / 2
		elif Polly(l, mid, A) < 0 and flag == 1:
			b = mid
			mid = (a + b) / 2
	
	print(mid)		
			
#print(Polly(l, mid, A))
#print(mid)
#print()


def rootFind(err, A, l) :
	if Polly(l, -500, A) < 0 :
		flag = -1
	else : 
		flag = 1
		
	rangeofsearch = 500
	spacing = 0.1
	i = - rangeofsearch
	
	while (i < rangeofsearch) : 
		if (Polly(l, i, A) * flag) < 0 :
			a = i - spacing
			b = i
			printRoot(a, b, err, flag)
			flag = flag * (-1)
		i += spacing
		
		
rootFind(err, A, l)
		



		
		
		
























	
			
			
			
			
			
			
