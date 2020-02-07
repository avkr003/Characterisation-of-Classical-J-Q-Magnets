function plot_qv_fourier(qv,m,n)

figure;
hold;

for i = 1:m*n
    for j = 1:m*n
        plot3(i,j,qv_fourier(i,j,qv,m,n), '*');
        title('Qq vs i & j');
        xlabel('i'); 
        ylabel('j'); 
        zlabel('Qq');
    end
end
end