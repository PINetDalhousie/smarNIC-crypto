# NGINX

![HTTPS server setup](web-setup.pdf)

## Configuration 

### basic setup

our config file is under `config/nginx.conf`, to edit the nginx.conf file:

```
vim /etc/nginx/nginx.conf
```
set up default webpage:

```
cp /var/www/html/index.nginx-debian.html /var/www/html/index.html
```

now you can access it using:

```
wget http://10.50.1.5/index.html
```

### ssl setup

change the `CN` and `IP.1` part inside `ssl.conf`

generate ssl certificate

```
sudo openssl req -new -nodes -x509 -days 365 -keyout /etc/ssl/private/nginx-selfsigned.key -out /etc/ssl/certs/nginx-selfsigned.crt -config ssl.conf
```

verify:

```
openssl x509 -in /etc/ssl/certs/nginx-selfsigned.crt -noout -text
```

### webpage setup

put `1k.html`, `10k.html`, `100k.html`, `1m.html`, and `10m.html` under `/var/www/html/`

## Test

```
git clone https://github.com/wg/wrk.git
cd wrk
make
```

```
./wrk -t12 -c400 -d30s http://10.50.1.5/index.html
```

run our test:
```
./nginx_wrk.sh
```
