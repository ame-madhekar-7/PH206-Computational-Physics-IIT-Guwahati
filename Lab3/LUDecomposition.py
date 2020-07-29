
a11 = float(input())
a12 = float(input())
a13 = float(input())
b1 = float(input())

a21 = float(input())
a22 = float(input())
a23 = float(input())
b2 = float(input())

a31 = float(input())
a32 = float(input())
a33 = float(input())
b3 = float(input())

l11 = float(input())
l22 = float(input())
l33 = float(input())


A = [[a11, a12, a13], [a21, a22, a23], [a31, a32, a33]]
b = [b1, b2, b3]


u11 = A[0][0] / l11
u12 = A[0][1] / l11
u13 = A[0][2] / l11

l21 = A[1][0] / u11
u22 = (A[1][1] - l21 * u12) / l22
u23 = (A[1][2] - l21 * u13) / l22

l31 = A[2][0] / u11
l32 = (A[2][1] - l31 * u12) / u22
u33 = (A[2][2] - l31 * u13 - l32 * u23) / l33


L = [[l11, 0, 0], [l21, l22, 0], [l31, l32, l33]]
U = [[u11, u12, u13], [0, u22, u23], [0, 0, u33]]

print( )
print(L[0][0], L[0][1], L[0][2])
print(L[1][0], L[1][1], L[1][2])
print(L[2][0], L[2][1], L[2][2])
print( )
print(U[0][0], U[0][1], U[0][2])
print(U[1][0], U[1][1], U[1][2])
print(U[2][0], U[2][1], U[2][2])
print( )

detL = l11 * l22 * l33
detU = u11 * u22 * u33
print('Determinanant of L : ', detL)
print('Determinanant of U : ', detU)

detA = a11 * (a22 * a33 - a23 * a32) - a12 * (a21 * a33 - a23 * a31) + a13 * (a21 * a32 - a22 * a31)
print('Determinanant of A : ', detA)
print( )


y1 = b[0] / l11
y2 = (b[1] - l21 * y1) / l22
y3 = (b[2] - l31 * y1 - l32 * y2) / l33

y = [y1, y2, y3]


x3 = y3 / u33
x2 = (y2 - u23 * x3) / u22
x1 = (y1 - u12 * x2 - u13 * x3) / u11

print('x = ', x1)
print('y = ', x2)
print('z = ', x3)










