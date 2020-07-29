from math import exp







def sinh(x) :
	return (exp(x) - exp(-x)) / 2
	
def cosh(x) :
	return (exp(x) + exp(-x)) / 2
	
def tanh(x) :
	return sinh(x) / cosh(x)

def dx(fn, x, delta = 0.001) :
	return(fn(x + delta) - fn(x)) / delta
	
def d2x(fn, x, delta = 0.001) :
	return(dx(fn, (x + delta), delta) - dx(fn, x, delta)) / delta
	
x = 0.5

print()

a = dx(tanh(x), x)
print(a)
#print(f'first d of sinh(x) at {x} is {dx(tanh(x))})

#print(dx(sinh(x), x)) 

#print(f'The derivative of sinh(x) at {x} is : {dx(sinh(x))}')
print()
#print(f'The double derivative of sinh(x) at {x} is : {dx(sinh, x)}')
print()
#print(f'The derivative of sinh(x) at {x} is : {dx(tanh, x)}')
print()
#print(f'The double derivative of sinh(x) at {x} is : {dx(tanh(x)}')
print()
