import math
import numpy as np
import matplotlib.pyplot as plt

from system_energy import *
from spinenergy import *
from magnet import *

def initialize_b(m,n,p):
	if p == 1:
		sx = 0.0*np.random.rand(m,n)
		sy = 0.0*np.random.rand(m,n) + 1.0

		return sx,sy

	if p > 1:
		sx = 0.0*np.random.rand(m,n)
		sy = 0.0*np.random.rand(m,n) + 1.0
		sz = 0.0*np.random.rand(m,n) 
		
		return sx,sy,sz

def benchmark_i(jv,qv,m,n,p,d,temperature,beta):

	if temperature == 0.0 and qv == 0.0:
		return 0.0,1.0


	total_states = 2**(m*n*p)
	
	H = [0.0]*total_states
	M = [0]*total_states
	Ms = [0]*total_states
	prob_M = 0.0
	prob_Ms = 0.0
	
	partition_f = 0.0

	r0 = initialize_b(m,n,p)
	
	sx = r0[0]
	sy = r0[1]
	
	if p > 1:
		sz = r0[2]
	
	for i in range(total_states):
		state = bin(i)
		state = state[2:]
	
		for j in range(len(state)):
			row = j/n
			column = j%m
			if state[j] == '0':
				sy[row][column] = 1.0
			if state[j] == '1':
				sy[row][column] = -1.0
		if p == 1:
			d = '2d'
			H[i] = system_energy_1(sx,sy,m,n,jv,qv)	
			r1 = magnet(sx,sy,0.0,m,n,p,d)
	
		if p > 1:
			d = '3d'
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