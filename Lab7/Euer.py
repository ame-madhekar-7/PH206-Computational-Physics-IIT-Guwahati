import numpy as np

h = 1e-3

k=1
m=1
itr=10000

t = []
for i in range(itr):
	t.append(i)
	t[i] = (i+1) * h
	
phi = []
for i in range(itr):
	phi.append(i)
	
phi[0] = 0
dphi = 2

phi[1] = (h * dphi) + phi[0]

for i in range(2, itr):
	phi[i] = (2 - h*h*(k/m)*(k/m)) * phi[i-1] - phi[i-2]
	
y = []

for i in range(itr):
	y.append(i)
	y[i] = 2 * np.sin(t[i])
	
for i in range(itr):
	print(t[i], phi[i], y[i])


