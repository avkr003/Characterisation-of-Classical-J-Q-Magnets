function r = system_energy(jv,qv,m,n,x,y,z)

r = 0;

for i = 1:m
    parfor j = 1:n
        r = r + spin_energy(i,j,jv,qv,x,y,z);
    end
end

r = r/2;
end