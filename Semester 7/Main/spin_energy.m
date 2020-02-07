function r = spin_energy(a,b,jv,x,y,z)
    [m,n] = size(x);
    syms r1 r2 c1 c2;
    
    if a == 1 
        r1  = m;
    else
        r1 = a - 1;
    end
    %%%%%%%%%%%%%%%%%%%%%%%%%   
    if b == 1 
        c1  = n;
    else
        c1 = b - 1;
    end
    %%%%%%%%%%%%%%%%%   
    if b == n 
        c2  = 1;
    else
        c2 = b + 1;
    end
    %%%%%%%%%%%%   
    if a == m 
        r2  = 1;
    else
        r2 = a + 1;
    end
    %%%%%%%%%%%%%
    
    sumx1 = x(a,c1) + x(a,c2) + x(r1,b) + x(r2,b);
    sumy1 = y(a,c1) + y(a,c2) + y(r1,b) + y(r2,b);
    sumz1 = z(a,c1) + z(a,c2) + z(r1,b) + z(r2,b);
    
    sumx2 = x(r1,c1) + x(r1,c2) + x(r2,c1) + x(r2,c2);
    sumy2 = y(r1,c1) + y(r1,c2) + y(r2,c1) + y(r2,c2);
    sumz2 = z(r1,c1) + z(r1,c2) + z(r2,c1) + z(r2,c2);
    
    sumx = jv(1)*sumx1 + jv(2)*sumx2;
    sumy = jv(1)*sumy1 + jv(2)*sumy2;
    sumz = jv(1)*sumz1 + jv(2)*sumz2;
    
    r = x(a,b)*sumx + y(a,b)*sumy + z(a,b)*sumz;
end