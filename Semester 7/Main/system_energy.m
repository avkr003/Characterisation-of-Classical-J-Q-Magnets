function r = system_energy(jv,x,y,z)

r = 0;

[m,n] = size(x);

for i = 1:m
    for j = 1:n
        r = r + spin_energy(i,j,jv,x,y,z);
    end
end

r = r/2;
end