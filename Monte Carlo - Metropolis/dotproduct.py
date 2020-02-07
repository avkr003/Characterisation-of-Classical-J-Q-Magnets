
def dotproduct1(x,y,i1,j1,i2,j2):
	r =  x[i1][j1]*x[i2][j2] + y[i1][j1]*y[i2][j2]
	return r

def dotproduct_p(x,y,z,i1,j1,k1,i2,j2,k2):
	r =  x[k1][i1][j1]*x[k2][i2][j2] + y[k1][i1][j1]*y[k2][i2][j2] + z[k1][i1][j1]*z[k2][i2][j2]
	return r


