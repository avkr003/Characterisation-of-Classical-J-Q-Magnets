import os
import math
import numpy as np
import matplotlib.pyplot as plt

from system_energy import *
from spinenergy import *
from magnet import *

def benchmark_h(jv,qv,m,n,p,d,temperature,beta):

	if temperature == 0.0 and qv == 0.0:
		return 0.0,1.0

	if temperature < 1.0:
		iterate = 5*int(math.pow(10,6))
	else:
		iterate = int(math.pow(10,6))

	H = [0.0]*iterate
	M = [0]*iterate
	Ms = [0]*iterate
	prob_M = 0.0
	prob_Ms = 0.0
	
	partition_f = 0.0
	
	for i in range(iterate):

		if i%1000.0 == 0.0:
			np.random.seed(int(os.urandom(4).encode('hex'), 16))

		if p == 1:
			d = '2d'

			phi = 2.0*np.pi*np.random.rand(m,n)
			sx = np.cos(phi)
			sy = np.sin(phi)

			H[i] = system_energy_1(sx,sy,m,n,jv,qv)	
			r1 = magnet(sx,sy,0.0,m,n,p,d)
		
		if p > 1:
			d = '3d'

			theta = np.pi*np.random.rand(p,m,n)
			phi = 2.0*pi*np.random.rand(p,m,n)

			sx = np.sin(theta)*np.cos(phi)
			sy = np.sin(theta)*np.sin(phi)
			sz = np.cos(theta)

			H[i] = system_energy_p(sx,sy,sz,m,n,p,jv,qv)
			r1 = magnet(sx,sy,sz,m,n,p,d)	
	
		M[i] = r1[0]
		Ms[i] = r1[1]
	
		prob = np.exp(-H[i]*beta)
	
		partition_f += prob
	
		prob_M += M[i]*prob
		prob_Ms += Ms[i]*prob
	
	M = prob_M/partition_f
	Ms = prob_Ms/partition_f
	
	return M, Ms