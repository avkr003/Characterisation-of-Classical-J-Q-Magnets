from spinenergy import *

def system_energy_1(sx,sy,m,n,jv,qv):
	
	r = 0.0

	for i in range(m):
		for j in range(n):
			r += spinenergy1(sx,sy,i,j,jv,qv,m,n)

	r = r/2.0

	return r

def system_energy_p(sx,sy,sz,m,n,p,jv,qv):

	r = 0.0

	for i in range(m):
		for j in range(n):
			for k in range(p):
				r += spinenergy_p(sx,sy,sz,i,j,k,jv,qv,m,n,p)

	r = r/2.0

	return r