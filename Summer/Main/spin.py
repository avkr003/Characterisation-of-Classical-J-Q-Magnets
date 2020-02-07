import os
import math
import numpy as np
import random as rand
import matplotlib.pyplot as plt

from autocorrelation import *
from initializer import *
from spinenergy import *
from jacknife import *
from perturb import *
from magnet import *

def autoerror(r,q):
	n = len(r)
	e = 0.0
	for i in range(1,n-q):
		e += math.pow(r[i],2)
	err = math.pow((1.0 + 2.0*e)/n,0.5)
	return err

def spin(jv,qv,iterations,m,n,p,d,temperature,tp,step,temp_step,innerloop,beta):

	print "Temperature: ",temperature	

	r0 = initializer(tp,d,m,n,p)
	sx = np.copy(r0[0])
	sy = np.copy(r0[1])
	if d == '3d':
		sz = np.copy(r0[2])
		r1 = magnet(sx,sy,sz,m,n,p,d)
	elif d == '2d':
		r1 = magnet(sx,sy,0.0,m,n,p,d)

	print "Intial Values: Ferromagnetic Moment, M: ", r1[0]
	print "Anti-ferromagnetic Moment, Ms: ", r1[1]

	rj = 0.0						#Rejectance

	n0 = int(iterations/step - 1)

	data_M = [0.0]*n0
	data_Ms = [0.0]*n0

	f = 0

	rand.seed(os.urandom(8))

	for t1 in range(iterations):
		for t2 in range(innerloop):
			i = rand.randint(0,m-1)
			j = rand.randint(0,n-1)
			k = rand.randint(0,p-1)
				
			x0 = np.copy(sx)
			y0 = np.copy(sy)

			if d == '3d':
				E1 = spinenergy_p(sx,sy,sz,i,j,k,jv,qv,m,n,p)

				z0 = np.copy(sz)

				r2 = perturb(x0[k][i][j],y0[k][i][j],z0[k][i][j],d,tp)
				x0[k][i][j] = r2[0]
				y0[k][i][j] = r2[1]
				z0[k][i][j] = r2[2]

				E2 = spinenergy_p(x0,y0,z0,i,j,k,jv,qv,m,n,p)

			if d == '2d':
				E1 = spinenergy1(sx,sy,i,j,jv,qv,m,n)

				r2 = perturb(x0[i][j],y0[i][j],0.0,d,tp)

				x0[i][j] = r2[0]
				y0[i][j] = r2[1]
				
				E2 = spinenergy1(x0,y0,i,j,jv,qv,m,n)
			
			dE = E2 - E1

			prob = np.random.rand()

			if dE < 0 or prob < np.exp(-dE*beta):
				sx = np.copy(x0)
				sy = np.copy(y0)
				
				if d == '3d':
					sz = np.copy(z0)
			else:
				#E2 = E1
				rj += 1
####################	Measurement    ##########################
		if float(t1)%float(step) == 0.0 and t1 != 0:
			if d == '3d':
				r3 = magnet(sx,sy,sz,m,n,p,d)

			elif d == '2d':
				r3 = magnet(sx,sy,0.0,m,n,p,d)

			np.random.seed(int(os.urandom(4).encode('hex'), 16))
			rand.seed(os.urandom(8))

			data_M[f] = r3[0]
			data_Ms[f] = r3[1]
			
			f += 1

	#M = np.mean(data_M,dtype=np.float64)
	#Ms = np.mean(data_Ms,dtype=np.float64)
	
	print "Data values for current Temperature:"
	print "Ferromagnetic Moment, M: ", data_M
	print "Anti-ferromagnetic Moment, Ms: ", data_Ms,"\n"

	ac_M = autocorrelation(data_M,temperature,int(temperature/temp_step))
	ac_Ms = autocorrelation(data_Ms,temperature,int(temperature/temp_step))
	
	#M_std = np.std(data_M,dtype=np.float64,ddof = 1)
	#Ms_std = np.std(data_Ms,dtype=np.float64,ddof = 1)
	#M_err1 = M_std/math.pow(n0,0.5)
	#Ms_err1 = Ms_std/math.pow(n0,0.5)


	#M_err2 = autoerror(ac_M,0)	#	n-q is point which correlation coeeicient is 0. Taking max possible to be on safe side
	#Ms_err2 = autoerror(ac_Ms,0)	# This increases error though

	#print 'Ms_err1', Ms_err1
	#print 'Diff: Ms_err1 - Ms_err2', Ms_err1 - Ms_err2

	r4 = jacknife(data_M)
	r5 = jacknife(data_Ms)
	M = r4[0]
	Ms = r5[0]
	M_err = r4[1]
	Ms_err = r5[1]

	return M,Ms,M_err,Ms_err,rj
