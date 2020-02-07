function r = jv_fourier(jv,m,n,qx,qy)

syms jvq;

jvq = 0;

t1 = jv(1);
t2 = jv(2);

for i1 = 1:m*n
   jvq = jvq + t1*(exp(-2i*pi*qx) + exp(2i*pi*qx) + exp(-2i*pi*qy) + exp(2i*pi*qy)) + t2*(exp(-2i*pi*(qx+qy)) + exp(2i*pi*(qx+qy)) + exp(-2i*pi*(qx-qy)) + exp(2i*pi*(qx-qy)));                     
end
jvq = jvq/2;

r = jvq;
end