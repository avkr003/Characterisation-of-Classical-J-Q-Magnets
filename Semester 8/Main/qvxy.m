function [qx,qy] = qvxy(t,m,n)   %for given index (1:m*n), it gives crystal momentum components
r = ones(m*n,2);

[x,y] = qxqy(m,n);

p = 1;

for i = 1:m:m*n
    k = 1;
    for j = i:1:i+m-1
        r(j,1) = x(p);
        r(j,2) = y(k);
        k = k + 1;
    end
    p = p + 1;
end
%disp(r);
qx = r(t,1);
qy = r(t,2);

end