function y = s2(sx,sy,sz)

[m,n] = size(sx);
syms s s1 s2y s3;
s1 = 0;
s2y = 0;
s3 = 0;

for i = 1:m
    parfor j = 1:n
        s1 = s1 + sx(i,j)*sx(i,j); 
        s2y = s2y + sy(i,j)*sy(i,j); 
        s3 = s3 + sz(i,j)*sz(i,j);
    end
end

y = s1 + s2y + s3;

disp(y);
end