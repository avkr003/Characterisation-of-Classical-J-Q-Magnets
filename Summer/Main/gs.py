import math
from dotproduct import *

def gs1(sx,sy,i,j,jv,qv,m,n):
	r1 = (i+m-1)%m
	c1 = (j+n-1)%n
	r2 = (i+1)%m
	c2 = (j+1)%n

	srx = (jv[0]*(sx[i][c1] + sx[i][c2] + sx[r1][j] + sx[r2][j])
			+ jv[1]*(sx[r1][c1]+ sx[r1][c2] + sx[r2][c1] + sx[r2][c2]))

	sry = (jv[0]*(sy[i][c1] + sy[i][c2] + sy[r1][j] + sy[r2][j])
			+ jv[1]*(sy[r1][c1] + sy[r1][c2] + sy[r2][c1] + sy[r2][c2]))



	s2s5 =  dotproduct1(sx,sy, i,c1, r1,c1)
	s4s6 =  dotproduct1(sx,sy, i,c2, r1,c2)        # (s0s1)*[(s2s5) + (s4s6)]   
										  	
	srx += qv * sx[r1][j] * (s2s5  + s4s6)
	sry += qv * sy[r1][j] * (s2s5  + s4s6)

	s3s7 =  dotproduct1(sx,sy, r2,j, r2,c1)
	s1s5 =  dotproduct1(sx,sy, r1,j, r1,c1)        # (s0s2)*[(s3s7) + (s1s5)] 
	
	srx += qv * sx[i][c1] * (s3s7 + s1s5)
	sry += qv * sy[i][c1] * (s3s7 + s1s5)
	
	s2s7 =  dotproduct1(sx,sy, i,c1, r2,c1)
	s4s8 =  dotproduct1(sx,sy, i,c2, r2,c2)        # (s0s3)*[(s2s7) + (s4s8)] 
	
	srx += qv * sx[r2][j] * (s2s7 + s4s8)
	sry += qv * sy[r2][j] * (s2s7 + s4s8)
 
	s1s6 =  dotproduct1(sx,sy, r1,j, r1,c2)
	s3s8 =  dotproduct1(sx,sy, r2,j, r2,c2)        # (s0s4)*[(s1s6) + (s3s8)] 
	
	srx += qv * sx[i][c2] * (s1s6 + s3s8)
	sry += qv * sy[i][c2] * (s1s6 + s3s8)
	
	sumv = math.pow((math.pow(srx,2.0) + math.pow(sry,2.0)), 0.5)

	srx = -srx/sumv
	sry = -sry/sumv

	return srx,sry


