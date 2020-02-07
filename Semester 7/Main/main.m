syms sx sy sz;
syms m n;

jv(1) = 1;
jv(2) = 0.8;

m = 4;
n = 4;

iterations = 1000;

[sx,sy,sz] = spin(jv, iterations,m,n);

syms k;
k = 1;
q1 = ones(m,1);
q2 = ones(n,1);

for i = -m/2+1 : 1 : m/2
    q1(k) = i/m;
    k=k+1;
end
k = 1;
for i = -n/2+1 : 1 : n/2
    q2(k) = i/n;
    k=k+1;
end

figure;
hold;

for i = 1:m
    for j = 1:n
        z = spin_fourier(sx,sy,sz, q1(i),q2(j));
        plot3(q1(i),q2(j),z, '*');
        grid on;
    end
end

        
        
        
        
        
        
        
        
        
        
        
        
        
        