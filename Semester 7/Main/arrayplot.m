function y = arrayplot(x,y,z)
    [m,n] = size(x);
        
    zp = ones(m,n);

    figure;
    %hold on;
    quiver3(zp,flipud(x),flipud(y),flipud(z));   
end
