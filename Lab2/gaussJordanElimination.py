import numpy as np


C = [[1.0, 2.0, 3.0, 1.0], [2.0, 5.0, 3.0, 6.0], [1.0, 0.0, 8.0, -6.0]]



I = [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]
A = np.hstack([C, I])

print(A)


a = A[0][0]
for j in range(7):
	A[0][j] /= a

b = A[1][0] / A[0][0]
for j in range(7):
	A[1][j] -= b * A[0][j]
c = A[2][0] / A[0][0]
for j in range(7):
	A[2][j] -= c * A[0][j]

print(A)

d = A[1][1]
for j in range(7):
	A[1][j] /= d

e = A[0][1] / A[1][1]
for j in range(7):
	A[0][j] -= e * A[1][j]
f = A[2][1] / A[1][1]
for j in range(7):
	A[2][j] -= f * A[1][j]

print(A)

g = A[2][2]
for j in range(7):
	A[2][j] /= g

h = A[0][2] / A[2][2]
for j in range(7):
	A[0][j] -= h * A[2][j]
i = A[1][2] / A[2][2]
for j in range(7):
	A[1][j] -= i * A[2][j]

print(A)


x = A[0][3]
y = A[1][3]
z = A[2][3]

print('x = ', x)
print('y = ', y)
print('z = ', z)


B = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

B[0][0] = A[0][4]
B[0][1] = A[0][5]
B[0][2] = A[0][6]
B[1][0] = A[1][4]
B[1][1] = A[1][5]
B[1][2] = A[1][6]
B[2][0] = A[2][4]
B[2][1] = A[2][5]
B[2][2] = A[2][6]

print(B)











