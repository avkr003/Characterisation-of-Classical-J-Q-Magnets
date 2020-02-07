import numpy as np

x = np.random.rand(3,3)
y = np.random.rand(3,3)

print 'y',id(y)

y = np.copy(x)

y[1][1] = -y[1][1]

y[0][1] = 2
print 'x11',x[0][1]
print 'y01',y[0][1]
print y[1][1]+x[1][1]

print 'x',id(x)
print 'y',id(y)

if id(x) == id(y):
	print 'true'
else:
	print 'false'
