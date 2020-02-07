import numpy as np
import random as rand

def perturb(x0,y0,z0,d,tp):
	if d == '3d':
		# Heisenberg Model
		if tp == "heisenberg":
			phi = 2.0*np.pi*np.random.rand()
			theta = np.pi*np.random.rand()
			x = np.cos(phi)*np.sin(theta)
			y = np.sin(phi)*np.sin(theta)
			z = np.cos(theta)

		# Ising Model
		if tp == "ising":
			x = -x0
			y = -y0
			z = -z0
			
		return x,y,z

	elif d == '2d':
		# Heisenberg Model
		if tp == "heisenberg":
			phi = 2.0*np.pi*np.random.rand()
			x = np.cos(phi)
			y = np.sin(phi)

		# Ising Model
		if tp == "ising":
			x = -x0
			y = -y0

		return x,y


