function r = t_hamiltonain_f(sx,sy,sz,jv,qv)

[m,n] = size(sx); 
h =  0;

if jv(1) > 0
    [qx1,qy1] = qxqy(m,n);
    figure('Name','J*Sq*Sq');
    hold;
    for i = 1:m
        t1 = qx1(i);
        for j = 1:n
            t = jv_fourier(jv,m,n,t1,qy1(j)) * sq2(sx,sy,sz,t1,qy1(j));

            plot3(t1,qy1(j),t, '*');
            title('Jq|Sq1 vs qx1 & qy1');
            xlabel('qx1'); 
            ylabel('qy1'); 
            zlabel('Jq|Sq1|');
            h = h + t;
        end
    end
end
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
if qv > 0
    figure('Name','Q*Sq*Sq*Sq*Sq');
    hold;
    u1 = ones(m*n,m*n);
    for i = 1:m*n
        [qx2,qy2] = qvxy(i,m,n);
       for j = 1:m*n
            [qx3,qy3] = qvxy(j,m,n);
            sq2(sx,sy,sz, qx2,qy2);
            u1(i,j) = sq2(sx,sy,sz, qx2,qy2) * sq2(sx,sy,sz, qx3,qy3);
            u = qv_fourier(i,j,qv,m,n) * u1(i,j);
        
            plot3(i,j,u, '*');
            title('Q|Sq1|Sq2 vs qx1 & qy1');
            xlabel('i'); 
            ylabel('j'); 
            zlabel('Q|Sq1|Sq2|');
                
            h = h + u;
        end
    end


    figure('Name','Sq*Sq');
    hold;
    for i = 1:m*n
        for j = 1:m*n
            plot3(i,j,u1(i,j), '*');
            title('Sq1|Sq2 vs qx1 & qy1');
            xlabel('i'); 
            ylabel('j'); 
            zlabel('Sq1|Sq2|');
        end
    end
end

r =  h;

end
