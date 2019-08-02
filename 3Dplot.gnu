# set terminal pngcairo  transparent enhanced font "arial,10" fontscale 1.0 size 600, 400 
# set output 'pm3d.17.png'
set border 4095 front lt black linewidth 1.000 dashtype solid
set style increment default
set view 50, 220, 1, 1
set samples 30, 30
set isosamples 30, 30
set hidden3d back offset 1 trianglepattern 3 undefined 1 altdiagonal bentover
set pm3d implicit at s
set xrange [500000:0]
set ylabel "R [m]"
set xlabel "time [s]"
splot "demo.txt" u 1:3:2
pause -1