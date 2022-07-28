# This plot a round trip latency

set terminal pdf enhanced font ",18"
set output "auth_time.pdf"

color1 = "#29B6F6"; color2 = "#0288D1";

set style data histogram
set style histogram cluster gap 1
set style fill solid
set boxwidth 0.9
set xtics format "" nomirror
set xtics rotate by 45 right

set grid ytics
set style histogram errorbars linewidth 1 
set errorbars linecolor black
set bars front
set yrange [0:14.5]
set ylabel "Latency (ms)"
plot "time.dat" using 3:2:4:xtic(1) title "Server" linecolor rgb color1, \
     "time.dat" using 6:5:7 title "SmartNIC" linecolor rgb color2
