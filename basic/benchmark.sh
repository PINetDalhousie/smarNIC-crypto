#!/usr/bin/env bash

# custom variable
output_file=$([ -z "$1" ] && echo "test" || echo "$1")

# version info
openssl version >> "${output_file}_version"
echo "" >> "${output_file}_version"
lsb_release -a >> "${output_file}_version"
echo "" >> "${output_file}_version"
uname -a >> "${output_file}_version"

# benchmark function
benchmark() {
    options=$1
    algorithm=$2
    output_f=$3
    cmd="$options $algorithm"
    echo "command: $cmd"
    echo "output file: $output_f"

    last_option=$(echo $options | awk '{print $(NF-1)}')
    process="encryption"
    if [ $last_option == "-decrypt" ]; then
        process="decryption"
    fi

    declare -a bytesArray=("16" "64" "256" "1024" "8192" "16384")
    echo "size: ${bytesArray[*]} (bytes)"
    echo "time: 3 (s)"
     
    for bytes in ${bytesArray[@]}; do
        for seconds in 3; do
            echo "$bytes bytes $seconds seconds $algorithm $process" >> $output_file
            sleep 3
            $cmd -seconds $seconds -bytes $bytes | tail -n1 | awk '{print $NF"B/s"}' >> $output_f
            #sleep 3
            #{ /usr/bin/time -v $cmd -seconds $seconds -bytes $bytes ; } |& grep "Maximum resident set size" | awk '{print $NF"kB"}' >> $output_f
            sleep 3
        done
    done
}

# asymmetric benchmark function
benchmark_asymmetric() {
    options=$1
    algorithm=$2
    output_f=$3
    cmd="$options $algorithm"
    echo "command: $cmd"
    echo "output file: $output_f"

    last_option=$(echo $options | awk '{print $NF}')
    engine="null"
    if [ $last_option == "pka" ]; then
        engine="pka"
    fi

    echo "$engine $($cmd | tail -n1)" >> $output_f
    sleep 3
}

##
## symmetric
##

# aes-256-gcm
for i in {1..20}; do
    echo ""
    echo "round: $i"
    benchmark "openssl speed -elapsed -evp" "aes-256-gcm" $output_file
    benchmark "openssl speed -elapsed -decrypt -evp" "aes-256-gcm" $output_file
    echo ""
done

# aes-256-cbc
for i in {1..20}; do
    echo ""
    echo "round: $i"
    benchmark "openssl speed -elapsed -evp" "aes-256-cbc" $output_file
    benchmark "openssl speed -elapsed -decrypt -evp" "aes-256-cbc" $output_file
    echo ""
done

# chacha20-poly1305
for i in {1..20}; do
    echo ""
    echo "round: $i"
    benchmark "openssl speed -elapsed -evp" "chacha20-poly1305" $output_file
    benchmark "openssl speed -elapsed -decrypt -evp" "chacha20-poly1305" $output_file
    echo ""
done

#
# hash
#

# sha256
for i in {1..20}; do
    echo ""
    echo "round: $i"
    benchmark "openssl speed -elapsed -evp" "sha256" $output_file
    echo ""
done

# sha512
for i in {1..20}; do
    echo ""
    echo "round: $i"
    benchmark "openssl speed -elapsed -evp" "sha512" $output_file
    echo ""
done

#
# asymmetric
#

output_file_asymmetric="${output_file}_asymmetric"

# rsa2048
for i in {1..20}; do
    echo ""
    echo "round: $i"
    benchmark_asymmetric "openssl speed -elapsed" "rsa2048" $output_file_asymmetric
    #benchmark_asymmetric "sudo openssl speed -elapsed -engine pka" "rsa2048" $output_file_asymmetric
    echo ""
done

# rsa4096
for i in {1..20}; do
    echo ""
    echo "round: $i"
    benchmark_asymmetric "openssl speed -elapsed" "rsa4096" $output_file_asymmetric
    #benchmark_asymmetric "sudo openssl speed -elapsed -engine pka" "rsa4096" $output_file_asymmetric
    echo ""
done

# dsa2048
for i in {1..20}; do
    echo ""
    echo "round: $i"
    benchmark_asymmetric "openssl speed -elapsed" "dsa2048" $output_file_asymmetric
    #benchmark_asymmetric "sudo openssl speed -elapsed -engine pka" "dsa2048" $output_file_asymmetric
    echo ""
done

# ecdsap256
for i in {1..20}; do
    echo ""
    echo "round: $i"
    benchmark_asymmetric "openssl speed -elapsed" "ecdsap256" $output_file_asymmetric
    #benchmark_asymmetric "sudo openssl speed -elapsed -engine pka" "ecdsap256" $output_file_asymmetric
    echo ""
done

# ecdsap384
for i in {1..20}; do
    echo ""
    echo "round: $i"
    benchmark_asymmetric "openssl speed -elapsed" "ecdsap384" $output_file_asymmetric
    #benchmark_asymmetric "sudo openssl speed -elapsed -engine pka" "ecdsap384" $output_file_asymmetric
    echo ""
done

# ecdsap521
for i in {1..20}; do
    echo ""
    echo "round: $i"
    benchmark_asymmetric "openssl speed -elapsed" "ecdsap521" $output_file_asymmetric
    #benchmark_asymmetric "sudo openssl speed -elapsed -engine pka" "ecdsap521" $output_file_asymmetric
    echo ""
done

# ecdhp256
for i in {1..20}; do
    echo ""
    echo "round: $i"
    benchmark_asymmetric "openssl speed -elapsed" "ecdhp256" $output_file_asymmetric
    #benchmark_asymmetric "sudo openssl speed -elapsed -engine pka" "ecdhp256" $output_file_asymmetric
    echo ""
done

# ecdhp384
for i in {1..20}; do
    echo ""
    echo "round: $i"
    benchmark_asymmetric "openssl speed -elapsed" "ecdhp384" $output_file_asymmetric
    #benchmark_asymmetric "sudo openssl speed -elapsed -engine pka" "ecdhp384" $output_file_asymmetric
    echo ""
done

# ecdhp521
for i in {1..20}; do
    echo ""
    echo "round: $i"
    benchmark_asymmetric "openssl speed -elapsed" "ecdhp521" $output_file_asymmetric
    #benchmark_asymmetric "sudo openssl speed -elapsed -engine pka" "ecdhp521" $output_file_asymmetric
    echo ""
done

echo ""; echo "Benchmark Complete!"; echo ""
