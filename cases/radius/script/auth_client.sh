#!/bin/bash
# ./auth.sh &> auth_result.txt

ip_address=10.50.1.5

count=10000

for requests in {1..32}

do

    echo "requests: $requests count: $count"

    for round in {1..20}
    do
        time echo "User-Name=testing,User-Password=password,NAS-IP-Address=127.0.1.1,NAS-Port=0,Message-Authenticator=0x00,Cleartext-Password=\"password\"" | radclient $ip_address:1812 -q -p $requests -c $count auth testing123
        sleep 5
    done

    echo ""

done


count=100000

for requests in {1..32}

do

    echo "requests: $requests count: $count"

    for round in {1..20}
    do
        time echo "User-Name=testing,User-Password=password,NAS-IP-Address=127.0.1.1,NAS-Port=0,Message-Authenticator=0x00,Cleartext-Password=\"password\"" | radclient $ip_address:1812 -q -p $requests -c $count auth testing123
        sleep 5
    done

    echo ""

done


##!/bin/bash
## ./auth.sh &> auth_result.txt
#
#ip_address=10.50.1.5
#
#count=1000000
#
#for requests in 1 1000 10000 100000
#
#do
#
#    echo "requests: $requests count: $count"
#
#    for round in {1..20}
#    do
#        time echo "User-Name=testing,User-Password=password,NAS-IP-Address=127.0.1.1,NAS-Port=0,Message-Authenticator=0x00,Cleartext-Password=\"password\"" | radclient $ip_address:1812 -q -p $requests -c $count auth testing123
#        sleep 5
#    done
#
#    echo ""
#
#done



#!/bin/bash
# ./auth.sh &> auth_result.txt

ip_address=10.50.1.5

count=10000

for requests in {1..32}

do

    echo "requests: $requests count: $count"

    for round in {1..20}
    do
        time echo "User-Name=testing,User-Password=password,NAS-IP-Address=127.0.1.1,NAS-Port=0,Message-Authenticator=0x00,SHA2-Password=\"5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8\"" | radclient $ip_address:1812 -q -p $requests -c $count auth testing123
        sleep 5
    done

    echo ""

done


count=100000

for requests in {1..32}

do

    echo "requests: $requests count: $count"

    for round in {1..20}
    do
        time echo "User-Name=testing,User-Password=password,NAS-IP-Address=127.0.1.1,NAS-Port=0,Message-Authenticator=0x00,SHA2-Password=\"5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8\"" | radclient $ip_address:1812 -q -p $requests -c $count auth testing123
        sleep 5
    done

    echo ""

done
