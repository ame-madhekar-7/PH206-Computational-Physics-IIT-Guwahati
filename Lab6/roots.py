from math import pow
err = 1e-3

def Polly(x) :
	pow(x, 6) - x - 1

def printRoot(a, b, err, flag) :
	mid = (a + b) / 2
	while(abs(Polly(x)) > err) :
		if Polly(x) > 0 and flag == -1:
			b = mid
			mid = (a + b) / 2
		elif Polly(x) < 0 and flag == -1:
			a = mid
			mid = (a + b) / 2
		elif Polly(x) > 0 and flag == 1:
			a = mid
			mid = (a + b) / 2
		elif Polly(x) < 0 and flag == 1:
			b = mid
			mid = (a + b) / 2
	
	print(mid)
	
	
def rootFind(err) :
	if Polly(x) < 0 :
		flag = -1
	else : 
		flag = 1
		
	rangeofsearch = 500
	spacing = 0.1
	i = - rangeofsearch
	
	while (i < rangeofsearch) : 
		if (Polly(x) * flag) < 0 :
			a = i - spacing
			b = i
			printRoot(a, b, err, flag)
			flag = flag * (-1)
		i += spacing
		
		
rootFind(err)
