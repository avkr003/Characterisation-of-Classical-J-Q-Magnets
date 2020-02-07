function y = spin_fourier(sx,sy,sz, qx,qy)

[m,n] = size(sx);

syms sq sqx sqy sqz;
sqx = 0;
sqy = 0;
sqz = 0;

for i = 1:m
    for j = 1:n
        sqx = sqx + sx(i,j)*exp(-2i*pi*(qx*(i-1) + qy*(j-1))); 
        sqy = sqy + sy(i,j)*exp(-2i*pi*(qx*(i-1) + qy*(j-1))); 
        sqz = sqz + sz(i,j)*exp(-2i*pi*(qx*(i-1) + qy*(j-1)));
    end
end

sq = (sqx + sqy + sqz)/power(m*n,0.5);

y = sq * conj(sq);
end