import numpy as np

a = np.array([[1.0, 2.0, 3.0, 4.0], [0.0, 7.0, 8.0, 9.0], [0.0, 0.0, -10.0, 1.0], [0.0, 0.0, 0.0, -2.0]])
i = np.array([1.0, 2.0, 3.0, 4.0])

lam = 1
norm = 1
eps = 1e-5


def power(A, I, Lam, Norm) :
	
	print(Lam)
	print(I)

	if (((Lam - Norm) / Lam) > eps or Lam == Norm or ((Norm - Lam) / Lam) > eps) :
		lam = Norm
		a = np.copy(A)
		c = np.dot(A, I)
		d = np.abs(c)
		e = d.argmax()
		i = c / c[e]
		norm = np.abs(c[e])
		power(a, i, lam, norm)

print('The eigenvalue and the eigenvalue pair are : ')
ans = power(a, i, lam, norm)

