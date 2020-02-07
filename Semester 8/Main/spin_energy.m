function r = spin_energy(a,b,jv,qv,x,y,z)
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
    
    j_energy = (jv(1)-qv)*(dot_product(x,y,z,a,b,a,c1) + dot_product(x,y,z,a,b,a,c2)...
                    + dot_product(x,y,z,a,b,r1,b) + dot_product(x,y,z,a,b,r2,b)) +...
               jv(2)*(dot_product(x,y,z,a,b,r1,c1) + dot_product(x,y,z,a,b,r1,c2)...
                    + dot_product(x,y,z,a,b,r2,c1) + dot_product(x,y,z,a,b,r2,c2));
    
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    s2s5 =  dot_product(x,y,z, a,c1, r1,c1);
    s4s6 =  dot_product(x,y,z, a,c2, r1,c2);        % (s0s1)*[(s2s5) + (s4s6)]         
                                          
    s0s1 =  dot_product(x,y,z, a,b, r1,b);
    energy1 = qv * s0s1 * (s2s5  + s4s6);
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    s3s7 =  dot_product(x,y,z, r2,b, r2,c1);
    s1s5 =  dot_product(x,y,z, r1,b, r1,c1);        % (s0s2)*[(s3s7) + (s1s5)] 
    
    s0s2 =  dot_product(x,y,z, a,b, a,c1);
    energy2 = qv * s0s2 * (s3s7 + s1s5);
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    s2s7 =  dot_product(x,y,z, a,c1, r2,c1);
    s4s8 =  dot_product(x,y,z, a,c2, r2,c2);        % (s0s3)*[(s2s7) + (s4s8)] 
    
    s0s3 =  dot_product(x,y,z, a,b, r2,b);
    energy3 = qv * s0s3 * (s2s7 + s4s8);
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    s1s6 =  dot_product(x,y,z, r1,b, r1,c2);
    s3s8 =  dot_product(x,y,z, r2,b, r2,c2);        % (s0s4)*[(s1s6) + (s3s8)] 
    
    s0s4 =  dot_product(x,y,z, a,b, a,c2);
    energy4 = qv * s0s4 * (s1s6 + s3s8);
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    energy5 = qv * ((s2s5) + (s4s6) + (s3s7) + (s1s5) + (s2s7) + (s4s8) + (s1s6) + (s3s8));
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    r = j_energy + energy1 + energy2 + energy3 + energy4 - energy5 + qv;
end