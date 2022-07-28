# This plot a round trip latency

set terminal pdf enhanced font "SourceCodePro,18"
set output "ipsec_tcp.pdf"

color1 = "#0288D1"; color2 = "#29B6F6";

set style data histogram
set style histogram cluster gap 1
set style fill solid
set boxwidth 0.9
set xtics format "" nomirror
set xtics rotate by 45 right

set grid ytics
set style histogram
set errorbars linecolor black
set bars front
set yrange [0:4500]
set ytics (0, 1500, 3000, 4500)
set ylabel "Throughput (Mbits/sec)"

set key top right

plot "tcp.dat" using 3:xtic(1) title "SmartNIC" linecolor rgb color1, \
     "tcp.dat" using 6 title "Server" linecolor rgb color2
