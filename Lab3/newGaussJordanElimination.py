import numpy as np

C = [[1.0, 2.0, 3.0, 1.0], [2.0, 5.0, 3.0, 6.0], [1.0, 0.0, 8.0, -6.0]]



I = [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]
A = np.hstack([C, I]


for j in range(3):
	a = A[j][j]
	for i in range(7):
		A[j][i] /= a
	
	for k in range(3):
		if k!=j:
			for l in range(7):
				A[k][l] -= A[k][j] * A[j][l]
				



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
