function sq = msq2(sx,sy,sz,qx,qy)

[m,n] = size(sx);

sqx = 0;
sqy = 0;
sqz = 0;

for i = 1:m
    t = exp(-2i*pi*qx*(i-1));
    for j = 1:n
        u = exp(-2i*pi*qy*(j-1));
        sqx = sqx + sx(i,j)*t*u/((m*n)^0.5);
        sqy = sqy + sy(i,j)*t*u/((m*n)^0.5);
        sqz = sqz + sz(i,j)*t*u/((m*n)^0.5);
    end
end

sq = (sqx*conj(sqx) + sqy*conj(sqy) + sqz*conj(sqz));


end