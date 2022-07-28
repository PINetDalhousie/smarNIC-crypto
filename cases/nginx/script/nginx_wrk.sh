#!/bin/bash

wrk=./wrk/wrk
ip_address=10.50.1.5
declare -a PageNameList=("1k" "10k" "100k" "1m" "10m")

for thread in {1,2,4,8,16,32}
do
    for page_name in ${PageNameList[@]}; do
        echo $wrk -t $thread -c 1000 -d 180s -H \'Connection: close\' https://$ip_address/$page_name.html
        echo ""
        $wrk -t $thread -c 1000 -d 180s -H 'Connection: close' https://$ip_address/$page_name.html
        echo ""
        sleep 3
    done
done
