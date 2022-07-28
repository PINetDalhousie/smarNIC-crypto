# IPsec 

![VPN tunneling setup](vpn-setup.pdf)

## Install StrongSwan

```
sudo apt install strongswan
```

```
sudo systemctl status strongswan.service
```

You might also need this:

```
sudo apt install strongswan strongswan-pki libcharon-extra-plugins libcharon-extauth-plugins libstrongswan-extra-plugins
```

## Configuration

Suppose the server address is 192.168.100.1 and the client address is 192.168.100.2

### Server Configuration

```
sudo vim /etc/ipsec.conf
```

```
config setup
        charondebug="all"
        uniqueids=yes
conn devgateway-to-prodgateway
        type=tunnel
        auto=start
        keyexchange=ikev2
        authby=secret
        left=192.168.100.1
        right=192.168.100.2
        ike=aes256-sha1-modp1024!
        esp=aes256-sha1!
        aggressive=no
        keyingtries=%forever
        ikelifetime=28800s
        lifetime=3600s
        dpddelay=30s
        dpdtimeout=120s
        dpdaction=restart
```

```
sudo vim /etc/ipsec.secrets
```

```
192.168.100.1 192.168.100.2 : PSK "qLGLTVQOfqvGLsWP75FEtLGtwN3Hu0ku6C5HItKo6ac="
192.168.100.2 192.168.100.1 : PSK "qLGLTVQOfqvGLsWP75FEtLGtwN3Hu0ku6C5HItKo6ac="
```

### Client Configuration

```
sudo vim /etc/ipsec.conf
```

```
config setup
        charondebug="all"
        uniqueids=yes
conn devgateway-to-prodgateway
        type=tunnel
        auto=start
        keyexchange=ikev2
        authby=secret
        left=192.168.100.2
        right=192.168.100.1
        ike=aes256-sha1-modp1024!
        esp=aes256-sha1!
        aggressive=no
        keyingtries=%forever
        ikelifetime=28800s
        lifetime=3600s
        dpddelay=30s
        dpdtimeout=120s
        dpdaction=restart
```

```
sudo vim /etc/ipsec.secrets
```

```
192.168.100.2 192.168.100.1 : PSK "qLGLTVQOfqvGLsWP75FEtLGtwN3Hu0ku6C5HItKo6ac="
192.168.100.1 192.168.100.2 : PSK "qLGLTVQOfqvGLsWP75FEtLGtwN3Hu0ku6C5HItKo6ac="
```

## Tests

1) Client (encryption point) ---> Client smartNIC ---> Server smartNIC (decryption point) ---> Server
2) Client (encryption point) ---> Client smartNIC ---> Server smartNIC ---> Server (decryption point)
3) Client ---> Client smartNIC (encryption point) ---> Server smartNIC ---> Server (decryption point)
4) Client ---> Client smartNIC (encryption point) ---> Server smartNIC (decryption point) ---> Server

### Ping

```
ping -c 100 <server_ip>
```

### iPerf

On the server side:

```
iperf3 -s
```

On the client side (TCP test):

```
iperf3 -c <server_ip>
```

On the client side (UDP test):

```
iperf3 -c <server_ip> -u
```

On the client with time:

```
iperf3 -c <server_ip> -u -t 600
```
