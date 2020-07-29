h = 0.2
itr=100

x = []
for i in range(itr+1):
	x.append(h*i)
y = []
for i in range(itr+1):
	y.append(i)
	
u = []
for i in range(itr+1):
	u.append(i)
	

def F(y, u, x):
	return (-u - y)	

y[0] = 1.0
u[0] = 0.5

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
	



for i in range(itr):
	print(x[i], y[i])


print(y[10])
