# Matrix Algebra

import numpy

A = numpy.matrix('1 2 3; 2 7 4')
B = numpy.matrix('1 -1; 0 1')
C = numpy.matrix('5 -1; 9 1; 6 0')
D = numpy.matrix('3 -2 -1; 1 2 3')
u = numpy.matrix('6 2 -3 5')
v = numpy.matrix('3 5 -1 4')
w = numpy.matrix('1; 8; 0; 5')

# 1 answers: 1.1) 2x3, 1.2) 2x2, 1.3) 3x2, 1.4) 2x3, 1.5) 1x4, 1.6) 4x1
print(A.shape)
print(B.shape)
print(C.shape)
print(D.shape)
print(u.shape)
print(w.shape)

# 2 answers: 2.1) [9 7 -4 9], 2.2) [3 -3 -2 1], 2.3) [36 12 -18 30], 2.4) 51, 2.5) sqrt(74)
print(numpy.add(u, v))
print(numpy.add(u, -v))
print(6*u)
print(u*v.T)
print(numpy.linalg.norm(u))

# 3 answers: 3.1) None 3.2) [[-4 -7 -3], [4 6 4]], 3.3) [[14 3 3], [2 7 9]], 3.4) [[-1 -5 -1], [2 7 4]], 3.5) None
# error print(numpy.add(A, C))
print(numpy.add(A, -C.T))
print(numpy.add(C.T, 3*D))
print(B*A)
# error print(B*A.T)

# Optional answers: 1) None, 2) [[5 -6], [9 -8], [6 -6]], 3) [[1 -4], [0 1]], 4) [[14 28], [28 13]]
#                   5) [[10 -4 0], [-4 8 8], [0 8 10]]

# error print(B*C)
print(C*B)
print(B**4)
print(A*A.T)
print(D.T*D)
