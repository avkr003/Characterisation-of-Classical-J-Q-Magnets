function [x,y,z,m,n] = spin(jv, iterations,m,n)
syms ox1 oy1 oz1 c0 c1 b1;
syms tener minenergy c b;
syms x y z;
syms brk;

rand;                                           %first random number of matlab is not random so to call it for start

%p = ones(iterations + 1,1);                         % plotting points

theta = (pi/2)*rand(m,n);                          %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%33
phi = 2 * pi * rand(m,n);

x = sin(theta).*cos(phi);
y = sin(theta).*sin(phi);
z = cos(theta);

p(1,1) = system_energy(jv,x,y,z);

for k = 1: iterations
    i = irandom(m);
    j = irandom(n);

    [x(i,j), y(i,j), z(i,j)] = component(i, j, jv, x, y, z);   %c
    
    p(k+1,1) = system_energy(jv,x,y,z);
    
    if k > 201 && p(k,1) - p(k-100,1) <= 0.001
        break;       
    end
    
end

q = 1:1:k + 1;
figure;
scatter(q,p,130,'.');
arrayplot(x,y,z);
end

                