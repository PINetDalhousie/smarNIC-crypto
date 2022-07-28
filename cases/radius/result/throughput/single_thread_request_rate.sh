#!/bin/bash
# ./auth.sh &> auth_result.txt

ip_address=10.50.1.5

count=10000

for requests in 500 1000 1500 2000 2500 3000 3500 4000 4500 5000 5500 6000 6500 7000 7500 8000 8500 9000 9500

do

    echo "requests: $requests count: $count"

    for round in {1..20}
    do
        time echo "User-Name=testing,User-Password=password,NAS-IP-Address=127.0.1.1,NAS-Port=0,Message-Authenticator=0x00,Cleartext-Password=\"password\"" | radperf $ip_address:1812 -q -n $requests -c $count auth testing123
        sleep 5
    done

    echo ""

done
