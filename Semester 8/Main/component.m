function [cx, cy, cz] = component(a, b, jv,qv, x, y, z) %e
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
    
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    s2s5 =  dot_product(x,y,z, a,c1, r1,c1);
    s4s6 =  dot_product(x,y,z, a,c2, r1,c2);        % (s0s1)*[(s2s5) + (s4s6)] 
    
    %s0s1 =  dot_product(x,y,z, a,b, r1,b);
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    s3s7 =  dot_product(x,y,z, r2,b, r2,c1);
    s1s5 =  dot_product(x,y,z, r1,b, r1,c1);        % (s0s2)*[(s3s7) + (s1s5)] 
    
    %s0s2 =  dot_product(x,y,z, a,b, a,c1);
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    s2s7 =  dot_product(x,y,z, a,c1, r2,c1);
    s4s8 =  dot_product(x,y,z, a,c2, r2,c2);        % (s0s3)*[(s2s7) + (s4s8)] 
    
    %s0s3 =  dot_product(x,y,z, a,b, r2,b);
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    s1s6 =  dot_product(x,y,z, r1,b, r1,c2);
    s3s8 =  dot_product(x,y,z, r2,b, r2,c2);        % (s0s4)*[(s1s6) + (s3s8)] 
    
    %s0s4 =  dot_product(x,y,z, a,b, a,c2);
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%    

    sumqx1 = x(r1,b)*(s2s5 + s4s6);
    sumqy1 = y(r1,b)*(s2s5 + s4s6);
    sumqz1 = z(r1,b)*(s2s5 + s4s6);
    
    sumqx2 = x(a,c1)*(s3s7 + s1s5);
    sumqy2 = y(a,c1)*(s3s7 + s1s5);
    sumqz2 = z(a,c1)*(s3s7 + s1s5);
    
    sumqx3 = x(r2,b)*(s2s7 + s4s8);
    sumqy3 = y(r2,b)*(s2s7 + s4s8);
    sumqz3 = z(r2,b)*(s2s7 + s4s8);
    
    sumqx4 = x(a,c2)*(s1s6 + s3s8);
    sumqy4 = y(a,c2)*(s1s6 + s3s8);    
    sumqz4 = z(a,c2)*(s1s6 + s3s8);
    
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    
    sumqx = sumqx1 + sumqx2 + sumqx3 + sumqx4;
    sumqy = sumqy1 + sumqy2 + sumqy3 + sumqy4;
    sumqz = sumqz1 + sumqz2 + sumqz3 + sumqz4;
    
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    
    sumx = (jv(1) - qv)*sumx1 + jv(2)*sumx2 + qv*sumqx;
    sumy = (jv(1) - qv)*sumy1 + jv(2)*sumy2 + qv*sumqy;
    sumz = (jv(1) - qv)*sumz1 + jv(2)*sumz2 + qv*sumqz;    
    
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    
    usum = power(power(sumx,2) + power(sumy,2) + power(sumz,2),1/2);  
    
    cx = -sumx/usum; 
    cy = -sumy/usum; 
    cz = -sumz/usum;
    
end
