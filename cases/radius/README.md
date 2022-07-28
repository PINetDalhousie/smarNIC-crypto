# Authentication Server

![User authentication setup](radius-setup.pdf)

## Install FreeRADIUS

```
sudo apt install freeradius
```

## Configuration

In `/etc/freeradius/3.0/clients.conf` add:

```
client new {
        ipaddr = 10.50.1.6
        secret = testing123
}
```

In `/etc/freeradius/3.0/users` add 

```
testing Cleartext-Password := "password"
```

## Tests

First, start the server in background:

```
freeradius
```

Or in single thread mode:

```
freeradius -s -t
```

Or in debug mode:

```
freeradius -X
```

Then, send package:

```
echo "User-Name=testing,User-Password=password,NAS-IP-Address=127.0.1.1,NAS-Port=0,Message-Authenticator=0x00,Cleartext-Password=\"password\"" | radclient localhost:1812 -p 10 -n 10 -c 100000 auth testing123
```

Count the time: 

```
time echo "User-Name=testing,User-Password=password,NAS-IP-Address=127.0.1.1,NAS-Port=0,Message-Authenticator=0x00,Cleartext-Password=\"password\"" | radclient localhost:1812 -q -p 10 -c 100000 auth testing123
```

Count the time: 

```
time echo "User-Name=testing,User-Password=password,NAS-IP-Address=127.0.1.1,NAS-Port=0,Message-Authenticator=0x00,SHA2-Password=\"5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8\"" | radclient 10.50.1.5 -p 100 -c 10000 auth testing123
```
