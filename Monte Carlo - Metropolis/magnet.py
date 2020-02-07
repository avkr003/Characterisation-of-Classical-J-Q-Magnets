import math
import numpy as np

def magnet(sx,sy,sz,m,n,p,d):
	
	Mx = np.sum(sx)
	My = np.sum(sy)
	if d == '3d':
		Mz = np.sum(sz)

	Msx = 0.0
	Msy = 0.0
	if d == '3d':
		Msz = 0.0
		
		for k in range(p):
			for j in range(n):
				for i in range(m):
					Msx += math.pow(-1,(i+j+k))*sx[k][i][j]
					Msy += math.pow(-1,(i+j+k))*sy[k][i][j]
					Msz += math.pow(-1,(i+j+k))*sz[k][i][j]

		M = (math.pow(Mx,2) + math.pow(My,2) + math.pow(Mz,2))
		Ms = (math.pow(Msx,2) + math.pow(Msy,2) + math.pow(Msz,2))			

	elif d == '2d':
		
		for i in range(m):
			for j in range(n):
				Msx += math.pow(-1,(i+j))*sx[i][j]
				Msy += math.pow(-1,(i+j))*sy[i][j]
								
		M = math.pow(math.pow(Mx,2) + math.pow(My,2),0.5)/(m*n*p)
		Ms = math.pow(math.pow(Msx,2) + math.pow(Msy,2),0.5)/(m*n*p)	
	
	

	return M,Ms