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
```

### Config Permission
* /etc/udev/rules.d/99-com.rules
```
SUBSYSTEM=="input", GROUP="input", MODE="0666"
SUBSYSTEM=="i2c-dev", GROUP="i2c", MODE="0666"
SUBSYSTEM=="spidev", GROUP="spi", MODE="0666"
SUBSYSTEM=="bcm2835-gpiomem", GROUP="gpio", MODE="0666"

SUBSYSTEM=="gpio", GROUP="gpio", MODE="0666"
```

## Install OLED service
* Install BCM2835 libs
http://www.airspayce.com/mikem/bcm2835/
* Make in /var/robopi/oledsrv/
```
cd /var/robopi/oledsrv/
make
```
* Install service
```
sudo ln -s /var/robopi/oledsrv/oledsrv.service /etc/systemd/system/multi-user.target.wants/oledsrv.service
```

