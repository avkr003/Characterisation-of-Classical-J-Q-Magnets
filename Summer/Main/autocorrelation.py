import math
import numpy as np
import matplotlib.pyplot as plt

def autocorrelation(data,tenmperature,k):
#with open("/home/abhinav/Desktop/Academics/Summer/Python/data.txt","r") as f:
#	data = np.loadtxt(f,delimiter="\n")

	n = len(data)

	r = [0.0]*n

	mean = np.mean(data,dtype=np.float64)
	var = np.var(data,dtype=np.float64)
	t = n*var
	
	for i in range(n):
		for j in range(n-i):
			r[i] += (data[j] - mean)*(data[i+j] - mean)/t# ((n - i)*var		)

	x = range(n)

	plt.figure()
	plt.plot(x,r)
	plt.title(tenmperature)
	plt.savefig('auto {0}.jpg'.format(k))
	#plt.show()

	return r