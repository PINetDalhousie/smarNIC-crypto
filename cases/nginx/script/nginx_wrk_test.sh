#!/bin/bash

wrk=./wrk/wrk
ip_address=10.50.1.5
#ip_address=10.50.1.15
declare -a PageNameList=("1k" "10k" "100k" "1m" "10m")

for page_name in ${PageNameList[@]}; do
    for i in `seq 1`; do
        taskset -c $i $wrk -t 1 -c 50 -d 180s -H 'Connection: close' https://$ip_address/$page_name.html &
    done
    sleep 190 # 10 more seconds than 180s
done
