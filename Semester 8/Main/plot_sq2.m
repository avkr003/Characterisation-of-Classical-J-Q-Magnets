function sq = plot_sq2(sx,sy,sz,mit)

[m,n] = size(sx);

sum_sq2 = 0;

[qx,qy] = qxqy(m,n);

sq(m*n) = 0;
k = 1;

fsq = figure('Visible', 'on');
hold;

for i = 1:m
    t1 = qx(i);
    for j = 1:n
        sq(k) = msq2(sx,sy,sz, t1,qy(j));
        sum_sq2 = sum_sq2 + sq;
        plot3(t1,qy(j),sq(k), '*');
        title('|Sq|2 vs qx & qy');
        xlabel('qx'); 
        ylabel('qy'); 
        zlabel('|Sq2|');
        grid on;
        k = k + 1;
    end
end
%disp(sum_sq2);

folder = '/home/abhinav/Desktop/Week 10/Results/many_runs/Sq_square';
pngFileName = sprintf('Sq_%d.fig', mit);
fullFileName = fullfile(folder, pngFileName);
saveas(fsq,fullFileName);
close(fsq);

end
