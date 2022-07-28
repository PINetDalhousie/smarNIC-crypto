# This plot a round trip latency

set terminal pdf enhanced font "SourceCodePro,18"
set output "single_core_throughput.pdf"

color1 = "#0288D1"; color2 = "#29B6F6"; color3 = "#80D4F8"
set style data histogram
set style histogram cluster gap 1
set style fill solid
set boxwidth 0.9
set xtics format ""
set xlabel "Web Page Size"
set grid ytics
set ylabel "Throughput (requests/sec)"
set format y "10^{{%L}}"
set logscale y 10
set yrange [1:10000]
set ytics (0, 10, 100, 1000, 10000, 100000)
set key top right

plot "single_core_throughput.dat" using 2:xtic(1) title "SmartNIC (TLS1.2)" linecolor rgb color1,   \
     "single_core_throughput.dat" using 3 title "SmartNIC" linecolor rgb color2,   \
     "single_core_throughput.dat" using 4 title "Server" linecolor rgb color3
