import math
import numpy as np

def jacknife(data):

	n = len(data)
	mean = np.mean(data,dtype=np.float64)

	pseudo_data = [0.0]*n
	
	for i in range(n):
		mean_npp = (sum(data) - data[i])/(n-1) 	#i-th partial prediction
		
		pseudo_data[i] = n*mean - (n-1)*mean_npp

	jk_mean = np.mean(data,dtype=np.float64)

	jk_std = np.std(pseudo_data,dtype=np.float64,ddof = 1)

	jk_err = jk_std/math.pow(n,0.5)

	return jk_mean,jk_err