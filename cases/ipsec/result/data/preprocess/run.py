#!/usr/bin/env python3

def get_all(filename):
    file = open(filename, "r")
    number = file.read()
    #print(number)
    
    number_list = number.split()

    file.close()
    #print(number_list)

    float_map = map(float, number_list)
    num_list = list(float_map)

    avg = sum(num_list)/len(num_list)
    min_var = min(num_list)
    max_var = max(num_list)
    print(str(min_var) + " " + str(avg) + " " + str(max_var))

get_all("long_server_ipsec_tcp.txt")
get_all("long_server_normal_tcp.txt")
get_all("long_smartnic_ipsec_tcp.txt")
get_all("long_smartnic_normal_tcp.txt")

get_all("server_aes256gcm.txt")
get_all("smartnic_aes256gcm.txt")
