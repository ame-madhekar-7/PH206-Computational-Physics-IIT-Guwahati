h = 0.2
itr=100

x = []
for i in range(itr+1):
	x.append(h*i)
y = []
for i in range(itr+1):
	y.append(i)
	
def dydx(x, y):
	return x*x + 1	

y[0] = 2.0

for i in range(itr):
	k1 = h * dydx(x[i], y[i])
	k2 = h * dydx(x[i] + 0.5 * h, y[i] + 0.5 * k1)
	k3 = h * dydx(x[i] + 0.5 * h, y[i] + 0.5 * k2)
	k4 = h * dydx(x[i] + h, y[i] + k3)
	y[i+1] = y[i] + (1.0 / 6.0) * (k1 + 2*k2 + 2*k3 + k4)
	



for i in range(itr):
	print(x[i], y[i])


print(y[10])
