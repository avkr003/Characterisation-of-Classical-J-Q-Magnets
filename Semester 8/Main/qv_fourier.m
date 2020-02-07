function r = qv_fourier(a,b,qv,m,n)
  
qvf = 0;

parfor k = 1:m*n
    [qx1,qy1] = qvxy(a,m,n);
    [qx2,qy2] = qvxy(b,m,n);
    qvf = qvf + qv*exp(-2i*pi*(qx1+qx2))+ qv*exp(2i*pi*(qx1+qx2)) + qv*exp(-2i*pi*(qy1+qy2)) + qv*exp(2i*pi*(qy1+qy2));
end

qvf = qvf/2;

r = qvf;
end
