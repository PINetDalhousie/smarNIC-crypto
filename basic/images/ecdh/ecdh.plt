# This plot a round trip latency

set terminal pdf enhanced font "SourceCodePro,18"
set output "ecdh.pdf"

color1 = "#0D47A1"; color2 = "#1976D2"; color3 = "#42A5F5";
set style data histogram
set style histogram cluster gap 1
set style fill solid
set boxwidth 0.9
set xtics format ""
set xlabel "ECDH curve type"
set grid ytics
set format y "10^{{%L}}"
set logscale y 10
set yrange [1:100000]
set ylabel "Throughput (op/s)"
set ytics (0, 10, 100, 1000, 10000, 100000)
set key top right

plot "ecdh.dat" using 2:xtic(1) title "SmartNIC" linecolor rgb color1,   \
     "ecdh.dat" using 3 title "SmartNIC (PKA)" linecolor rgb color2,    \
     "ecdh.dat" using 4 title "Server" linecolor rgb color3
