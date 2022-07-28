#!/usr/bin/env python3
import pandas as pd
import matplotlib.pyplot as plt
from pygnuplot import gnuplot

def get_data_list_from(filename_list=["results/mellanox", "results/vps", "results/server"], list_name="results/symmetric_hash"):

    data_list_result = list_name + "_result.csv"
    result_file = open(data_list_result, "w")
    result_file.write("\"hardware\",\"algorithm\",\"process\",\"size (bytes)\",\"time (s)\",\"throughput (kB/s)\",\"throughput (GB/s)\"\n")

    for filename in filename_list:
        print(filename)
        get_data_from(filename, filename.split("/")[-1], result_file)

    result_file.close()

    df = pd.read_csv(data_list_result)
    return df

def get_data_from(filename, hardware, result_file):

    f = open(filename, "r")

    for line in f:
        info = line
        performance = f.readline()

        size = int(info.split()[0])
        time = int(info.split()[2])
        algorithm = str(info.split()[4])
        process = str(info.split()[5])

        throughput = float(performance[:-5])
        throughput_GB = float(performance[:-5]) / 1000000

        result_file.write(hardware + "," + algorithm + "," + process + "," + str(size) + "," + str(time) + "," + str(throughput) + "," + str(throughput_GB) + "\n")

    f.close()

def get_average(df, hardware="mellanox", algorithm="aes-256-gcm", size=16, time=3, process="encryption", metric="throughput (kB/s)"):
    mean = df.loc[(df["hardware"] == hardware) & (df["algorithm"] == algorithm) & (df["size (bytes)"] == size) & (df["time (s)"] == time) & (df["process"] == process), metric].mean()
    return mean

def get_sem(df, hardware="mellanox", algorithm="aes-256-gcm", size=16, time=3, process="encryption", metric="throughput (kB/s)"):
    sem = df.loc[(df["hardware"] == hardware) & (df["algorithm"] == algorithm) & (df["size (bytes)"] == size) & (df["time (s)"] == time) & (df["process"] == process), metric].sem()
    return sem




def get_asymmetric_data_list_from(filename_list=["results/mellanox_asymmetric", "results/vps_asymmetric", "results/server_asymmetric"], list_name="results/asymmetric"):

    data_list_result = list_name + "_result.csv"
    result_file = open(data_list_result, "w")
    result_file.write("\"hardware\",\"algorithm\",\"engine\",\"sign time (s)\",\"verify time (s)\",\"sign speed (sign/s)\",\"verify speed (verify/s)\"\n")

    for filename in filename_list:
        print(filename)
        get_asymmetric_data_from(filename, filename.split("/")[-1].split("_")[0], result_file)

    result_file.close()

    df = pd.read_csv(data_list_result)
    return df

def get_asymmetric_data_from(filename, hardware, result_file):

    f = open(filename, "r")

    for line in f:
        #print(line.split())
        info = line.split()
        engine = str(info[0])
        algorithm = str(info[1])
        size = int(info[2])
        sign_time = float(info[4][:-1])
        verify_time = float(info[5][:-1])
        sign_speed = float(info[6])
        verify_speed = float(info[7])

        result_file.write(hardware + "," + algorithm + str(size) + "," + engine + "," + str(sign_time) + "," + str(verify_time) + "," + str(sign_speed) + "," + str(verify_speed) + "\n")

    f.close()

def get_asymmetric_average(df, hardware="mellanox", algorithm="rsa2048", engine="null", metric="sign speed (sign/s)"):
    if (engine == "null"):
        mean = df.loc[(df["hardware"] == hardware) & (df["algorithm"] == algorithm) & (df["engine"].isnull()), metric].mean()
    else:
        mean = df.loc[(df["hardware"] == hardware) & (df["algorithm"] == algorithm) & (df["engine"] == engine), metric].mean()
    return mean

def get_asymmetric_sem(df, hardware="mellanox", algorithm="rsa2048", engine="null", metric="sign speed (sign/s)"):
    if (engine == "null"):
        sem = df.loc[(df["hardware"] == hardware) & (df["algorithm"] == algorithm) & (df["engine"].isnull()), metric].sem()
    else:
        sem = df.loc[(df["hardware"] == hardware) & (df["algorithm"] == algorithm) & (df["engine"] == engine), metric].sem()
    return sem
