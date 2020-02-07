function r = stat(typ,statistics,sq,mit)

exct(statistics) = 0;
k = 1;

if sq(6) ~= 0 && sq(16) ~= 0 && sq(8) ~= 0 && sq(14) ~= 0 && sq(1) <= 0.01 && sq(10) <= 0.01
    typ(1) = typ(1) + 1;
elseif sq(1) ~= 0 && sq(3) ~= 0 && sq(9) ~= 0 && sq(11) ~= 0 && sq(5) ~= 0 && sq(13) ~= 0 && sq(7) ~= 0 && sq(15) ~= 0 && sq(6) <= 0.01 && sq(12) <= 0.01
    typ(2) = typ(2) + 1;
elseif sq(2) ~= 0 && sq(4) ~= 0 && sq(10) ~= 0 && sq(12) ~= 0 && sq(1) <= 0.01 && sq(6) <= 0.01
    typ(3) = typ(3) + 1;
else
    typ(4) = typ(4) + 1;
    exct(k) = mit;
    k = k + 1;
end

fileID = fopen('exception iterations.txt','w');
fprintf(fileID,'%6s\r\n','exception');
fprintf(fileID,'%6.2f\r\n',exct);
fclose(fileID);
r = typ;
end