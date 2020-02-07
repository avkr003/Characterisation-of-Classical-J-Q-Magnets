import os
import math
import time
import numpy as np
import random as rand
import matplotlib.pyplot as plt

from gs import *
from system_energy import *

pi = np.pi

def spin_gs(jv,qv,iterations,m,n,p,d):

	np.random.seed(int(time.time()))

	if p == 1:
		theta = 2.0*pi*np.random.rand(m,n)

		sx = np.cos(theta)
		sy = np.sin(theta)
	elif p > 1:
		theta = pi*np.random.rand(p,m,n)
		phi = 2.0*pi*np.random.rand(p,m,n)

		sx = np.sin(theta)*np.cos(phi)
		sy = np.sin(theta)*np.sin(phi)
		sz = np.cos(theta)

	print 'sx:',sx
	print 'sy:',sy

	E = [0.0]*iterations

	rand.seed(int(os.urandom(4).encode('hex'), 16))

	for t in range(iterations):
		i = rand.randint(0,m-1)
		j = rand.randint(0,n-1)
		k = rand.randint(0,p-1)
		'''
		if d == '3d':
			E1 = spinenergy_p(sx,sy,sz,i,j,k,jv,qv,m,n,p)

			z0 = np.copy(sz)

			E2 = spinenergy_p(x0,y0,z0,i,j,k,jv,qv,m,n,p)
		'''

		if d == '2d':
			E[t] = system_energy_1(sx,sy,m,n,jv,qv)
			
			r0 = gs1(sx,sy,i,j,jv,qv,m,n)

			sx[i][j] = r0[0]
			sy[i][j] = r0[1]	
		
	x = range(iterations)

	plt.figure()
	plt.plot(x, E, 'b-o') 
	plt.title('E vs T')
	plt.savefig('E vs T.jpg')

	print 'sx:', sx
	print '\nsy:', sy

	return

