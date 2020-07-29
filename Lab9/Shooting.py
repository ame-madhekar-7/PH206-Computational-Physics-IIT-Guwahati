import numpy as np

def F(y, u, x):
	return (-4*y)
	


def rk(x0, m):
	x = []
	for i in range(itr+1):
		x.append(h*i)
	y = []
	for i in range(itr+1):
		y.append(i)
	u = []
	for i in range(itr+1):
		u.append(i)
		
	y[0] = 1.0
	u[0] = m
	
	for i in range(itr):
		m1 = h*u[i]
		k1 = h * F(y[i], u[i], x[i])
	
		m2 = h*(u[i] + 0.5*k1)
		k2 = h * F(y[i] + 0.5 * m1, u[i] + 0.5 * k1, x[i] + 0.5 * h)
	
		m3 = h*(u[i] + 0.5*k2)
		k3 = h * F(y[i] + 0.5 * m2, u[i] + 0.5 * k2, x[i] + 0.5 * h)
	
		m4 = h*(u[i] + k3)
		k4 = h * F(y[i] + m3, u[i] + k3, x[i] + h)
	
		u[i+1] = u[i] + (1.0 / 6.0) * (k1 + 2*k2 + 2*k3 + k4)
		y[i+1] = y[i] + (1.0 / 6.0) * (m1 + 2*m2 + 2*m3 + m4)
		
	return y
	
	
h = 0.01
m1 = -10.0
m2 = 25.0
x0 = 0
xf = np.pi/4
yf = 4
itr = int((xf-x0)/h)

v1 = rk(x0, m1)
#print(v1)
v2 = rk(x0, m2)
#print(v2)

M = m1 + ((m2 - m1)*(yf - v1[-1])) / (v2[-1] - v1[-1])

def rk1(x0, m):
	x = []
	for i in range(itr+1):
		x.append(h*i)
	y = []
	for i in range(itr+1):
		y.append(i)
	u = []
	for i in range(itr+1):
		u.append(i)
		
	y[0] = 1.0
	u[0] = m
	
	for i in range(itr):
		m1 = h*u[i]
		k1 = h * F(y[i], u[i], x[i])
	
		m2 = h*(u[i] + 0.5*k1)
		k2 = h * F(y[i] + 0.5 * m1, u[i] + 0.5 * k1, x[i] + 0.5 * h)
	
		m3 = h*(u[i] + 0.5*k2)
		k3 = h * F(y[i] + 0.5 * m2, u[i] + 0.5 * k2, x[i] + 0.5 * h)
	
		m4 = h*(u[i] + k3)
		k4 = h * F(y[i] + m3, u[i] + k3, x[i] + h)
	
		u[i+1] = u[i] + (1.0 / 6.0) * (k1 + 2*k2 + 2*k3 + k4)
		y[i+1] = y[i] + (1.0 / 6.0) * (m1 + 2*m2 + 2*m3 + m4)
		
	return y

itr = 3*itr
Y = []
Y = rk1(x0, M)




x = []
for i in range(itr+1):
	x.append(h*i)
	
for i in range(itr):
	print(x[i], Y[i])








