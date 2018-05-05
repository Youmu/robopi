# robopi
## BOM
* Raspberry Pi board
* PCA9685 PWM controller
* MPU6500 sensor

## Deploy

### Install the reqired packages
```
sudo apt install apache2
sudo apt-get install libapache2-mod-wsgi-py3
sudo pip3 install django
```

### Get the source code
```
cd /var
sudo git clone https://github.com/Youmu/robopi.git
sudo chown -R pi:pi robopi
```

### Configure the Apache
* /etc/apache2/sites-enabled/000-default.conf
```
DocumentRoot /var/robopi/html
WSGIScriptAlias /api /var/robopi/robopi_api/robopi_api/wsgi.py
<Directory /api>
  Require all granted
</Directory>
```
* /etc/apache2/apache2.conf
```
<Directory /var/robopi/>
    Options Indexes FollowSymLinks
    AllowOverride None
    Require all granted
</Directory>
```
* Restart apache
```
sudo /etc/init.d/apache2 restart
```:q

