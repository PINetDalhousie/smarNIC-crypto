#!/usr/bin/env python3
import datalib
import pandas as pd
import matplotlib.pyplot as plt
from pygnuplot import gnuplot

symmetric_hash_df = datalib.get_data_list_from()
asymmetric_df = datalib.get_asymmetric_data_list_from()

def get_results(df, hardware_list=["mellanox", "server"], process="encryption", metric="throughput (GB/s)", algorithm="aes-256-gcm", filename="data"):
    size_list = [16, 64, 256, 1024, 8192, 16384]
    f_dat = open(f"results/dat/{filename}.dat", "w")
    f_dat.write("#")
    for hardware in hardware_list:
        f_dat.write("\t" + hardware)
    f_dat.write("\n")
    for size in size_list:
        f_dat.write(str(size))
        for hardware in hardware_list:
            avg = datalib.get_average(df, hardware=hardware, algorithm=algorithm, size=size, process=process, metric=metric)
            f_dat.write("\t" + str(avg))
        for hardware in hardware_list:
            sem = datalib.get_sem(df, hardware=hardware, algorithm=algorithm, size=size, process=process, metric=metric)
            f_dat.write("\t" + str(sem))
        f_dat.write("\n")
    f_dat.close()

def get_colorset(colorset=["#FF0000", "#00FF00", "#0000FF"]):
    colorstr = ""
    index = 1
    for color in colorset:
        colorstr += f"color{index} = \"{color}\"; "
        index += 1
    return colorstr

def draw_symmetric_graph(algorithm="aes-256-gcm", title="title", process="encryption", filename="filename", yrange="[:]", colorset=["#FF0000", "#00FF00", "#0000FF"]):
    df = symmetric_hash_df
    hardware_list = ["mellanox", "server"]
    get_results(df, algorithm=algorithm, process=process, hardware_list=hardware_list, filename=filename)

    g = gnuplot.Gnuplot()

    colorstr = get_colorset(colorset=colorset)

    plot_cmd = f'''
    set terminal pdf enhanced font "SourceCodePro,18"
    set output 'images/{filename}.pdf'

    {colorstr}
    set style data histogram
    set style histogram cluster gap 1
    set style fill solid
    set boxwidth 0.9
    set xtics format ""
    set xlabel "Message size (bytes)"
    set grid ytics
    set yrange {yrange}
    set ylabel "Throughput (GB/s)"
    set key top left

    plot "results/dat/{filename}.dat" using 2:xtic(1) title "SmartNIC" linecolor rgb color1,   \
         "results/dat/{filename}.dat" using 3 title "Server" linecolor rgb color2
    '''
    g.cmd(plot_cmd)
    g.close()

def draw_hash_graph(algorithm="sha256", title="SHA256 Hash Function Throughput Comparison", filename="sha256_hash", yrange="[:]", colorset=["#FF0000", "#00FF00"]):
    df = symmetric_hash_df
    hardware_list = ["mellanox", "server"]
    get_results(df, algorithm=algorithm, hardware_list=hardware_list, filename=filename)

    g = gnuplot.Gnuplot()

    colorstr = get_colorset(colorset=colorset)

    plot_cmd = f'''
    set terminal pdf enhanced font "SourceCodePro,18"
    set output 'images/{filename}.pdf'

    {colorstr}
    set style data histogram
    set style histogram cluster gap 1
    set style fill solid
    set boxwidth 0.9
    set xtics format ""
    set xlabel "Message size (bytes)"
    set grid ytics
    set yrange {yrange}
    set ylabel "Throughput (GB/s)"
    set key top left

    plot "results/dat/{filename}.dat" using 2:xtic(1) title "SmartNIC" linecolor rgb color1,   \
         "results/dat/{filename}.dat" using 3 title "Server" linecolor rgb color2
    '''
    g.cmd(plot_cmd)
    g.close()

#def get_asymmetric_results(df, hardware_list=["mellanox", "server"], algorithm_list=["rsa2048", "rsa4096", "dsa2048", "ecdsap256", "ecdhp256", "ecdsap384", "ecdhp384", "ecdsap521", "ecdhp521"], use_engine=False, process="sign", filename="data"):
def get_asymmetric_results(df, hardware_list=["mellanox", "server"], algorithm_list=["dsa2048", "rsa2048", "rsa4096", "ecdsap256"], use_engine=False, process="sign", filename="data"):
    metric = "sign speed (sign/s)" if process == "sign" else "verify speed (verify/s)"
    f_dat = open(f"results/dat/{filename}.dat", "w")
    f_dat.write("#")
    for hardware in hardware_list:
        f_dat.write("\t" + hardware)
        if hardware == "mellanox":
            f_dat.write("\t" + hardware + "(pka)")
    for hardware in hardware_list:
        f_dat.write("\t" + hardware + " (error)")
        if hardware == "mellanox":
            f_dat.write("\t" + hardware + "(pka)" + " (error)")
    f_dat.write("\n")

    for algorithm in algorithm_list:
        f_dat.write(algorithm)
        for hardware in hardware_list:
            avg = datalib.get_asymmetric_average(df, hardware=hardware, algorithm=algorithm, metric=metric)
            f_dat.write("\t" + str(avg))
            if hardware == "mellanox":
                avg = datalib.get_asymmetric_average(df, hardware=hardware, algorithm=algorithm, engine="pka", metric=metric)
                f_dat.write("\t" + str(avg))
        for hardware in hardware_list:
            sem = datalib.get_asymmetric_sem(df, hardware=hardware, algorithm=algorithm, metric=metric)
            f_dat.write("\t" + str(sem))
            if hardware == "mellanox":
                sem = datalib.get_asymmetric_sem(df, hardware=hardware, algorithm=algorithm, engine="pka", metric=metric)
                f_dat.write("\t" + str(sem))
        f_dat.write("\n")

    #for algorithm in algorithm_list:
    #    if (use_engine):
    #        #f_dat.write(algorithm + "(pka)")
    #        f_dat.write(algorithm)
    #        for metric in metric_list:
    #            avg = datalib.get_asymmetric_average(df, hardware=hardware, algorithm=algorithm, engine="pka", metric=metric)
    #            f_dat.write("\t" + str(avg))
    #        f_dat.write("\n")
    #    else:
    #        f_dat.write(algorithm)
    #        for metric in metric_list:
    #            avg = datalib.get_asymmetric_average(df, hardware=hardware, algorithm=algorithm, metric=metric)
    #            f_dat.write("\t" + str(avg))
    #        f_dat.write("\n")

    f_dat.close()

def draw_asymmetric_graph(algorithm="rsa2048", title="title", process="sign", filename="filename", yrange="[:50000]", colorset=["#FF0000", "#00FF00", "#0000FF"]):
    df = asymmetric_df
    hardware_list = ["mellanox", "server"]
    get_asymmetric_results(df, hardware_list=hardware_list, process=process, filename=filename)

    g = gnuplot.Gnuplot()

    colorstr = get_colorset(colorset=colorset)

    ylabel = "Sign speed (sign/s)" if process == "sign" else "Verify speed (verify/s)"

    plot_cmd = f'''
    set terminal pdf size 5,5 enhanced font "SourceCodePro,18"
    set output 'images/{filename}.pdf'

    {colorstr}
    set style data histogram
    set style histogram cluster gap 1
    set style fill solid
    set boxwidth 0.9
    set xtics format ""
    set xtics rotate by 45 right
    set xlabel "Cryptographic algorithm"
    set grid ytics
    set format y "10^{{%L}}"
    set logscale y 10
    set yrange {yrange}
    set ylabel "{ylabel}"
    set ytics (0, 10, 100, 1000, 10000, 100000, 1000000)
    set key top left

    plot "results/dat/{filename}.dat" using 2:xtic(1) title "SmartNIC" linecolor rgb color1,   \
         "results/dat/{filename}.dat" using 3 title "SmartNIC(PKA)" linecolor rgb color2,  \
         "results/dat/{filename}.dat" using 4 title "Server" linecolor rgb color3
    '''
    g.cmd(plot_cmd)
    g.close()

# Symmetric

# aes-256-gcm
draw_symmetric_graph(title="AES-256-GCM Symmetric Algorithm Throughput Comparison (Encryption)", filename="aes-256-gcm_symmetric_encrypt", yrange="[:3]", colorset=["#0D47A1","#1976D2","#42A5F5"])
draw_symmetric_graph(title="AES-256-GCM Symmetric Algorithm Throughput Comparison (Decryption)", process="decryption", filename="aes-256-gcm_symmetric_decrypt", yrange="[:3]", colorset=["#0D47A1","#1976D2","#42A5F5"])
# aes-256-cbc
draw_symmetric_graph(algorithm="aes-256-cbc", title="AES-256-CBC Symmetric Algorithm Throughput Comparison (Encryption)", filename="aes-256-cbc_symmetric_encrypt", yrange="[:3]", colorset=["#1B5E20","#388E3C","#66BB6A"])
draw_symmetric_graph(algorithm="aes-256-cbc", title="AES-256-CBC Server Symmetric Algorithm Throughput Comparison (Decryption)", process="decryption", filename="aes-256-cbc_symmetric_decrypt", yrange="[:3]", colorset=["#1B5E20","#388E3C","#66BB6A"])
# chacha20-poly1305
draw_symmetric_graph(algorithm="chacha20-poly1305", title="ChaCha20-Poly1305 Symmetric Algorithm Throughput Comparison (Encryption)", filename="chacha20-poly1305_symmetric_encrypt", yrange="[:3]", colorset=["#B71C1C","#EF9A9A"])
draw_symmetric_graph(algorithm="chacha20-poly1305", title="ChaCha20-Poly1305 Symmetric Algorithm Throughput Comparison (Decryption)", process="decryption", filename="chacha20-poly1305_symmetric_decrypt", yrange="[:3]", colorset=["#B71C1C","#EF9A9A"])

# Hash

# sha256
draw_hash_graph(algorithm="sha256", yrange="[:0.5]", colorset=["#0D47A1","#1976D2","#42A5F5"])
# sha512
draw_hash_graph(algorithm="sha512", title="SHA512 Hash Function Throughput Comparison", filename="sha512_hash", yrange="[:0.5]", colorset=["#1B5E20","#388E3C","#66BB6A"])

# Asymmetric

# sign
draw_asymmetric_graph(process="sign", filename="asymmetric_sign_short", yrange="[1:1000000]", colorset=["#0D47A1","#1976D2","#42A5F5"])
# verify
draw_asymmetric_graph(process="verify", filename="asymmetric_verify_short", yrange="[1:1000000]", colorset=["#1B5E20","#388E3C","#66BB6A"])
