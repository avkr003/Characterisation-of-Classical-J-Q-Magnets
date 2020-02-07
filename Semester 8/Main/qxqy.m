function [qx,qy] = qxqy(m,n)

syms k;
k = 1;
qx = ones(m,1);
qy = ones(n,1);

for i = -m/2+1 : 1 : m/2
    qx(k) = i/m;
    k=k+1;
end
k = 1;
for i = -n/2+1 : 1 : n/2
    qy(k) = i/n;
    k=k+1;
end
end