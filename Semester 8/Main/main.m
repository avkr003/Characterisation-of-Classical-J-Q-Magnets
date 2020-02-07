syms sx sy sz;
syms m n;

jv(1) = 1;
jv(2) = 0;
qv = 1;

m = 4;
n = 4;

d = '2d';

iterations = 5000;
statistics = 50;
limit = 200;

sq2 = zeros(1,m*n);
f_sq = zeros(1,m*n);

tic;
for mit = 1:statistics
[sx,sy,sz] = spin(jv,qv, iterations,limit,m,n,d,mit);

sq = plot_sq2(sx,sy,sz,mit);                                                    %   BTP 1

for i = 1:m*n
    if sq(i) >= 0.001
        f_sq(i) = f_sq(i) + sq(i);
    end
end

sq2 = sq2 + sq;
%typ = stat(typ,statistics,sq,mit);

%plot_qv_fourier(qv,m,n);
        
%hq = t_hamiltonain_f(sx,sy,sz,jv,qv);        

end

sq2 = sq2/statistics;
[qx,qy] = qxqy(m,n);
k = 1;
figure;
hold on;
for i = 1:m
    t1 = qx(i);
    for j = 1:n
        plot3(t1,qy(j),sq2(k), '*');
        title('Avg_|Sq|2 vs qx & qy');
        xlabel('qx'); 
        ylabel('qy'); 
        zlabel('|Sq2|');
        grid on;
        k = k + 1;
    end
end

figure;
q = 1:1:m*n;
scatter(q,f_sq,150,'.');


toc;
        
               
        