import numpy as np

D = 0.2
L = 1.2
b = 0.1
a = 0.1
t = 5
nl = int(L/a) + 2
nt = int(t/b) + 1
def ux0(x):
	return x*(L-x)
u = np.zeros((nl, nt))
al = (D*b) / (a*a)

temp = 0
for i in range(nl):
	u[i,0] = ux0(temp)
	temp += a
u[0,:] = 0
u[nl-1,:] = 0

for i in range(nt-1):
	mat = np.zeros((nl-2,nl-2))
	vec = np.zeros((nl-2,1))
	
	mat[0,0] = 1 + 2*al
	mat[0,1] = -al
	vec[0,0] = al*(u[0,i] + u[0,i+1] + u[2,i]) + (1-2*al)*u[1,i]
	
	mat[-1,-1] = 1 + 2*al
	mat[-1,-2] = -al
	vec[-1,0] = al*(u[nl-1,i+1] + u[nl-1,i] + u[nl-3,i]) + (1-2*al)*u[nl-2,i]
	
	for j in range(1,nl-3):
		mat[j,j] = 1 + 2*al
		mat[j,j-1] = -al
		mat[j,j+1] = -al
		vec[j,0] = al*(u[j-1,i] + u[j+1,i]) + (1-2*al)*u[j,i]
		
	u[1:nl-1, i+1] = (np.dot(np.linalg.inv(mat), vec)).T

for j in range(nt):
	for i in range(nl):
		print(a*i, u[i,j])
