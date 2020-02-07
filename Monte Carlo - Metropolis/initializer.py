import os
import time
import numpy as np
import random as rand

pi = np.pi

def binary():
	t = np.random.rand()
	if t < 0.5:
		return -1
	else:
		return 1

def initializer(tp,d,m,n,p):

	np.random.seed(int(os.urandom(4).encode('hex'), 16))

	if d == '2d':
		if tp == 'heisenberg':
			phi = 2.0*pi*np.random.rand(m,n)
			sx = np.cos(phi)
			sy = np.sin(phi)

		elif tp == 'ising':
			sx = 0.0*np.random.rand(m,n) + 1
			sy = 0.0*np.random.rand(m,n) + 1

			for i in range(m):
				for j in range(n):
					sx[i][j] = 0.0
					sy[i][j] = binary()

		return sx,sy
				
		

	if d == '3d':
		if tp == 'heisenberg':
			theta = pi*np.random.rand(p,m,n)
			phi = 2.0*pi*np.random.rand(p,m,n)

			sx = np.sin(theta)*np.cos(phi)
			sy = np.sin(theta)*np.sin(phi)
			sz = np.cos(theta)
		
		elif tp == 'ising':
			sx = 0.0*np.random.rand(p,m,n) + 1.0
			sy = 0.0*np.random.rand(p,m,n) + 1.0
			sz = 0.0*np.random.rand(p,m,n) + 1.0

			for k in range(p):
				for i in range(m):
					for j in range(n):
						t = binary()
						sx[k][i][j] = 0.0
						sy[k][i][j] = t
						sz[k][i][j] = 0.0

	return sx,sy,sz

