import numpy as np
import math

A = np.array([[2, 3, 1], [3, 2, 2], [1, 2, 1]])

n = len(A)
eps = 1e-4
rot = np.identity(n)

def Jack(A, Rot):
	k=0
	l=0
	max=0
	
	for i in range(n):
		for j in range(n):
			if i!=j:
				if abs(A[i][j]) > max:
					max = abs(A[i][j])
					k = i
					l = j
					
	t = 0.5 * math.atan(2 * A[k][l] / abs(A[l][l] - A[k][k]))
	
	c = math.cos(t)
	s = math.sin(t)
	
	R = np.zeros([n, n], dtype = float)
	
	R[k][k] = c
	R[l][l] = c
	R[k][l] = -s
	R[l][k] = s
	
	for i in range(n):
		if i != k and i != l:
			R[i][i] = 1.0
			
	Rinv = np.transpose(R)
	
	D = np.dot(np.dot(Rinv, A), R)
	Rot = np.dot(Rot, R)
	
	print(D)
	print(Rot)
	
	if max > eps :
		Jack(D, Rot)
		

ans = Jack(A, rot)
print(ans)
	
	
	
	
	
	
	
	
	
