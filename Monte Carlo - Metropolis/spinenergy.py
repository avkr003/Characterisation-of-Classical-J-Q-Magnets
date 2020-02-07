from dotproduct import *

def spinenergy1(sx,sy,i,j,jv,qv,m,n):
	r1 = (i+m-1)%m
	c1 = (j+n-1)%n
	r2 = (i+1)%m
	c2 = (j+1)%n

	jenergy = (jv[0]*(dotproduct1(sx,sy,i,j,i,c1) + dotproduct1(sx,sy,i,j,i,c2) 
				+ dotproduct1(sx,sy,i,j,r1,j) + dotproduct1(sx,sy,i,j,r2,j))
				+ jv[1]*(dotproduct1(sx,sy,i,j,r1,c1) + dotproduct1(sx,sy,i,j,r1,c2) 
				+ dotproduct1(sx,sy,i,j,r2,c1) + dotproduct1(sx,sy,i,j,r2,c2)))

	s2s5 =  dotproduct1(sx,sy, i,c1, r1,c1)
	s4s6 =  dotproduct1(sx,sy, i,c2, r1,c2)        # (s0s1)*[(s2s5) + (s4s6)]   
										  
	s0s1 =  dotproduct1(sx,sy, i,j, r1,j)		
	energy1 = qv * s0s1 * (s2s5  + s4s6)

	s3s7 =  dotproduct1(sx,sy, r2,j, r2,c1)
	s1s5 =  dotproduct1(sx,sy, r1,j, r1,c1)        # (s0s2)*[(s3s7) + (s1s5)] 
	
	s0s2 =  dotproduct1(sx,sy, i,j, i,c1)
	energy2 = qv * s0s2 * (s3s7 + s1s5)
	
	s2s7 =  dotproduct1(sx,sy, i,c1, r2,c1)
	s4s8 =  dotproduct1(sx,sy, i,c2, r2,c2)        # (s0s3)*[(s2s7) + (s4s8)] 
	
	s0s3 =  dotproduct1(sx,sy, i,j, r2,j)
	energy3 = qv * s0s3 * (s2s7 + s4s8)
 
	s1s6 =  dotproduct1(sx,sy, r1,j, r1,c2)
	s3s8 =  dotproduct1(sx,sy, r2,j, r2,c2)        # (s0s4)*[(s1s6) + (s3s8)] 
	
	s0s4 =  dotproduct1(sx,sy, i,j, i,c2)
	energy4 = qv * s0s4 * (s1s6 + s3s8)
	
	r = jenergy + energy1 + energy2 + energy3 + energy4

	return r


def spinenergy_p(sx,sy,sz,i,j,k,jv,qv,m,n,p):
	r1 = (i+3)%4
	c1 = (j+3)%4
	h1 = (k+3)%4

	r2 = (i+1)%4
	c2 = (j+1)%4
	h2 = (k+1)%4

	jenergy = (jv[0]*(dotproduct_p(sx,sy,sz,i,j,k,i,c1,k) + dotproduct_p(sx,sy,sz,i,j,k,i,c2,k)
				+ dotproduct_p(sx,sy,sz,i,j,k,r1,j,k) + dotproduct_p(sx,sy,sz,i,j,k,r2,j,k)
				+ dotproduct_p(sx,sy,sz,i,j,k,i,j,h1) + dotproduct_p(sx,sy,sz,i,j,k,i,j,h2))
			+ jv[1]*(dotproduct_p(sx,sy,sz,i,j,k,r1,c1,k) + dotproduct_p(sx,sy,sz,i,j,k,r1,c2,k)
				+ dotproduct_p(sx,sy,sz,i,j,k,r2,c1,k) + dotproduct_p(sx,sy,sz,i,j,k,r2,c2,k)
				+ dotproduct_p(sx,sy,sz,i,j,k,i,c1,h1) + dotproduct_p(sx,sy,sz,i,j,k,i,c1,h2)
				+ dotproduct_p(sx,sy,sz,i,j,k,i,c2,h1) + dotproduct_p(sx,sy,sz,i,j,k,i,c2,h2)
				+ dotproduct_p(sx,sy,sz,i,j,k,r1,j,h1) + dotproduct_p(sx,sy,sz,i,j,k,r1,j,h2)
				+ dotproduct_p(sx,sy,sz,i,j,k,r2,j,h1) + dotproduct_p(sx,sy,sz,i,j,k,r2,j,h2))
			+ jv[2]*(dotproduct_p(sx,sy,sz,i,j,k,r1,c1,h1) + dotproduct_p(sx,sy,sz,i,j,k,r1,c2,h1)
				+ dotproduct_p(sx,sy,sz,i,j,k,r2,c1,h1) + dotproduct_p(sx,sy,sz,i,j,k,r2,c2,h1)
				+ dotproduct_p(sx,sy,sz,i,j,k,r1,c1,h2) + dotproduct_p(sx,sy,sz,i,j,k,r1,c2,h2)
				+ dotproduct_p(sx,sy,sz,i,j,k,r2,c1,h2) + dotproduct_p(sx,sy,sz,i,j,k,r2,c2,h2)))
#(s0s1)*[(s2s5) + (s4s6)]
	s2s5c =  dotproduct_p(sx,sy,sz, i,c1,k, r1,c1,k)
	s4s6c =  dotproduct_p(sx,sy,sz, i,c2,k, r1,c2,k)		 
  
	s2s5b =  dotproduct_p(sx,sy,sz, r2,j,k, r2,j,h2)
	s4s6b =  dotproduct_p(sx,sy,sz, r1,j,k, r1,j,h2)
  
	s2s5a =  dotproduct_p(sx,sy,sz, i,c1,k, i,c1,h2)
	s4s6a =  dotproduct_p(sx,sy,sz, i,c2,k, i,c2,h2)

#(s0s2)*[(s3s7) + (s1s5)]
	s3s7c =  dotproduct_p(sx,sy,sz, r2,j,k, r2,c1,k)
	s1s5c =  dotproduct_p(sx,sy,sz, r1,j,k, r1,c1,k)		
  
	s3s7b =  dotproduct_p(sx,sy,sz, i,j,h1, r2,j,h1)
	s1s5b =  dotproduct_p(sx,sy,sz, i,j,h2, r2,j,h2)
  
	s3s7a =  dotproduct_p(sx,sy,sz, i,j,h1, i,c1,h1)
	s1s5a =  dotproduct_p(sx,sy,sz, i,j,h2, i,c1,h2) 
 
#(s0s3)*[(s2s7) + (s4s8)] 
	s2s7c =  dotproduct_p(sx,sy,sz, i,c1,k, r2,c1,k)
	s4s8c =  dotproduct_p(sx,sy,sz, i,c2,k, r2,c2,k)		
  
	s2s7b =  dotproduct_p(sx,sy,sz, r2,j,k, r2,j,h1)
	s4s8b =  dotproduct_p(sx,sy,sz, r1,j,k, r1,j,h1)
  
	s2s7a =  dotproduct_p(sx,sy,sz, i,c1,k, i,c1,h1)
	s4s8a =  dotproduct_p(sx,sy,sz, i,c2,k, i,c2,h1)

#(s0s4)*[(s1s6) + (s3s8)]
	s1s6c =  dotproduct_p(sx,sy,sz, r1,j,k, r1,c2,k)
	s3s8c =  dotproduct_p(sx,sy,sz, r2,j,k, r2,c2,k)		
  
	s1s6b =  dotproduct_p(sx,sy,sz, i,j,h2, r1,j,h2)
	s3s8b =  dotproduct_p(sx,sy,sz, i,j,h1, r1,j,h1)
 
	s1s6a =  dotproduct_p(sx,sy,sz, i,j,h2, i,c2,h2)
	s3s8a =  dotproduct_p(sx,sy,sz, i,j,h1, i,c2,h1) 
  
  #
	s0s1 =  dotproduct_p(sx,sy,sz, i,j,k, r1,j,k)
	energy1 = qv * s0s1 * ((s2s5c + s4s6c) + (s1s6b + s3s8b))
  
	s0s2 =  dotproduct_p(sx,sy,sz, i,j,k, i,c1,k)
	energy2 = qv * s0s2 * ((s3s7c + s1s5c) + (s3s7a + s1s5a))
  
	s0s3 =  dotproduct_p(sx,sy,sz, i,j,k, r2,j,k)
	energy3 = qv * s0s3 * ((s2s7c + s4s8c) + (s3s7b + s1s5b))
  
	s0s4 =  dotproduct_p(sx,sy,sz, i,j,k, i,c2,k)
	energy4 = qv * s0s4 * ((s1s6c + s3s8c) + (s1s6a + s3s8a))
  
	s0s5 =  dotproduct_p(sx,sy,sz, i,j,k, i,j,h2)
	energy5 = qv * s0s5 * ((s2s5b + s4s6b) + (s2s5a + s4s6a))
  
	s0s6 =  dotproduct_p(sx,sy,sz, i,j,k, i,j,h1)
	energy6 = qv * s0s6 * ((s2s7b + s4s8b) + (s2s7a + s4s8a))
	
	r = jenergy + energy1 + energy2 + energy3 + energy4 + energy5 + energy6

	return  r


