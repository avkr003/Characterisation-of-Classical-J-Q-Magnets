function [x,y,z] = spin(jv,qv,iterations,limit,m,n,d,mit)
syms x y z x0 y0 z0;

rand;  

if d == '2d'
    theta = (pi/2)*ones(m,n);
else
    theta =(pi/2)*rand(m,n);
end
phi = 2 * pi * rand(m,n);

x = sin(theta).*cos(phi);
y = sin(theta).*sin(phi);
z = cos(theta);

zp = ones(m,n);

p(limit) = zeros;
%figure;

for k = 1: iterations
    i = irandom(m);
    j = irandom(n);
    %x0 = x;
    %y0 = y;
    %z0 = z;
    [x(i,j), y(i,j), z(i,j)] = component(i, j, jv,qv, x, y, z);   %c
    
    p(k+1) = system_energy(jv,qv,m,n,x,y,z);
    
    %quiver3(zp,flipud(x),flipud(y),flipud(z));
    %title(['Running Iteration: ',num2str(k)]);
    %view(0, 90);
    %pause(0.01);
    if p(k+1)- p(k) > 1000
        %arrayplot(x0,y0,z0);
        %arrayplot(x,y,z);
        disp(i);
        disp(j);
        disp(spin_energy(i,j,jv,qv,x0,y0,z0));
        disp(spin_energy(i,j,jv,qv,x,y,z));
        disp('true')
        %break;
    end
    
    if k > limit + 1 && p(k-limit) - p(k) <= 0.1
        disp(k); 
        break;       
    end
    
end

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%     

q = 1:1:k + 1;
evit = figure('Visible', 'on');
scatter(q,p,130,'.');
title('Energy vs Iterations');
xlabel('Iterations'); % x-axis label
ylabel('Energy'); % y-axis label

foldere = '/home/abhinav/Desktop/Week 10/Results/many_runs/Energy';
pngFileName = sprintf('energy_%d.fig', mit);
fullFileName = fullfile(foldere, pngFileName);
saveas(evit,fullFileName);
close(evit);

arr = figure('Visible', 'on');
quiver3(zp,flipud(x),flipud(y),flipud(z)); 
title('Final Configuration');
foldera = '/home/abhinav/Desktop/Week 10/Results/many_runs/Config';
pngFileName = sprintf('config_%d.fig', mit);
fullFileName = fullfile(foldera, pngFileName);
saveas(arr,fullFileName);
close(arr);

end

                