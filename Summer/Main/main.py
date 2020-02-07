import sys
import math
import threading
sys.path.append('/home/abhinav/Desktop/Academics/Summer/Python')
import numpy as np
import matplotlib.pyplot as plt
import time

from spin import *
from benchmark_ising import *
from benchmark_data_h import *
from benchmark_heisenberg import *

kb = 1.0

m = 4
n = 4
p = 1 

if p > 1:
	d = '3d'
elif p == 1:
	d = '2d'

tp = 'heisenberg'

qv = 0.0
jv = [0.0]*3
jv[0] = 1.0

iterations = 500000
step = 5000
innerloop = int(2*m*n*p)

print "Model: ",tp
print "J:", jv
print "Q:", qv
print "Total Iterations: ", iterations
print "Measurement Step: ", step
print "Inner Loop (Iterations within each Iterations): ", (innerloop/(m*n*p)),"* Total Lattice Points"

temp_i = 0.0
temp_step = 0.25
temp_f = 6.0

n0 = int((temp_f - temp_i)/temp_step)

M = [0.0]*n0
b_M = [0.0]*n0
Ms = [0.0]*n0
b_Ms = [0.0]*n0
M_error = [0.0]*n0
Ms_error = [0.0]*n0
rj = [0.0]*n0
Difference = [0.0]*n0

start_time = time.time()

for i in range(n0):
#def simulation(i):
	temperature = temp_i + i*temp_step
	if temperature == 0.0:
		beta = math.pow(10.0,50)
	else:
		beta = 1.0/(temperature*kb)

	r1 = spin(jv,qv,iterations,m,n,p,d,temperature,tp,step,temp_step,innerloop,beta)
	
	if tp == 'ising':
		benchmark = benchmark_i(jv,qv,m,n,p,d,temperature,beta)
	elif tp == 'heisenberg':
		benchmark = benchmark_data_h(temperature, temp_i,temp_f,temp_step)
		#benchmark = benchmark_h(jv,qv,m,n,p,d,temperature,beta)
	
	M[i] = r1[0]
	Ms[i] = r1[1]

	b_M[i] = benchmark[0]
	b_Ms[i] = benchmark[1]

	M_error[i] = r1[2]
	Ms_error[i] = r1[3]

	rj[i] = r1[4]
	Difference[i] = M[i] - Ms[i]

'''for i in range(0,n0,2):
	t1 = threading.Thread(target=simulation, args=(i,))
	t2 = threading.Thread(target=simulation, args=(i+1,))

	t1.start()
	t2.start()
	
	t1.join()
	t2.join()
'''
x = np.arange(temp_i,temp_f,temp_step)


print "\n-----------------------------------------------\n\nFinal Values for all Temperatures:"
print "Ferromagnetic Moment, M: ", M
print "Anti-ferromagnetic Moment, Ms: ", Ms

plt.figure()
plt.errorbar(x, Ms, yerr=Ms_error, fmt='-o', uplims=True, lolims=True)
plt.plot(x, b_Ms, 'r-o') 
plt.title('Ms vs T')
plt.savefig('Ms vs T.jpg')

plt.figure()
plt.errorbar(x, M, yerr=M_error, fmt='-o', uplims=True, lolims=True)
plt.plot(x, b_M, 'r-o')
plt.title('M vs T')
plt.savefig('M vs T.jpg')

plt.figure()
plt.plot(x,rj,'b-o')
plt.title('Rejectance')
plt.savefig('Rejectance.jpg')

plt.figure()
plt.plot(x,Difference,'bo')
plt.title('Difference b/w M and Ms')
plt.savefig('Difference.jpg')

print "\nRuntime: %s seconds" % (time.time() - start_time)
