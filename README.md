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
* Raspberry Pi GPIO Pin map
```
 +-----+-----+---------+------+---+---Pi 3---+---+------+---------+-----+-----+
 | BCM | wPi |   Name  | Mode | V | Physical | V | Mode | Name    | wPi | BCM |
 +-----+-----+---------+------+---+----++----+---+------+---------+-----+-----+
 |     |     |    3.3v |      |   |  1 || 2  |   |      | 5v      |     |     |
 |   2 |   8 |   SDA.1 |   IN | 1 |  3 || 4  |   |      | 5v      |     |     |
 |   3 |   9 |   SCL.1 |   IN | 1 |  5 || 6  |   |      | 0v      |     |     |
 |   4 |   7 | GPIO. 7 |   IN | 1 |  7 || 8  | 1 | ALT5 | TxD     | 15  | 14  |
 |     |     |      0v |      |   |  9 || 10 | 1 | ALT5 | RxD     | 16  | 15  |
 |  17 |   0 | GPIO. 0 |   IN | 0 | 11 || 12 | 0 | IN   | GPIO. 1 | 1   | 18  |
 |  27 |   2 | GPIO. 2 |   IN | 0 | 13 || 14 |   |      | 0v      |     |     |
 |  22 |   3 | GPIO. 3 |   IN | 0 | 15 || 16 | 0 | IN   | GPIO. 4 | 4   | 23  |
 |     |     |    3.3v |      |   | 17 || 18 | 0 | IN   | GPIO. 5 | 5   | 24  |
 |  10 |  12 |    MOSI | ALT0 | 0 | 19 || 20 |   |      | 0v      |     |     |
 |   9 |  13 |    MISO | ALT0 | 0 | 21 || 22 | 0 | IN   | GPIO. 6 | 6   | 25  |
 |  11 |  14 |    SCLK | ALT0 | 0 | 23 || 24 | 1 | OUT  | CE0     | 10  | 8   |
 |     |     |      0v |      |   | 25 || 26 | 1 | OUT  | CE1     | 11  | 7   |
 |   0 |  30 |   SDA.0 |   IN | 1 | 27 || 28 | 1 | IN   | SCL.0   | 31  | 1   |
 |   5 |  21 | GPIO.21 |   IN | 1 | 29 || 30 |   |      | 0v      |     |     |
 |   6 |  22 | GPIO.22 |   IN | 1 | 31 || 32 | 0 | IN   | GPIO.26 | 26  | 12  |
 |  13 |  23 | GPIO.23 |   IN | 0 | 33 || 34 |   |      | 0v      |     |     |
 |  19 |  24 | GPIO.24 |  OUT | 1 | 35 || 36 | 1 | OUT  | GPIO.27 | 27  | 16  |
 |  26 |  25 | GPIO.25 |   IN | 0 | 37 || 38 | 0 | IN   | GPIO.28 | 28  | 20  |
 |     |     |      0v |      |   | 39 || 40 | 0 | IN   | GPIO.29 | 29  | 21  |
 +-----+-----+---------+------+---+----++----+---+------+---------+-----+-----+
 | BCM | wPi |   Name  | Mode | V | Physical | V | Mode | Name    | wPi | BCM |
 +-----+-----+---------+------+---+---Pi 3---+---+------+---------+-----+-----+
```
* Hardware connection 
```
    OLED   =>    Raspberry Pi
   VCC    ->    3.3
   GND    ->    GND
   DIN    ->    MOSI
   CLK    ->    SCLK
   CS     ->    24 (Physical, BCM: CE0, 8)
   D/C    ->    36 (Physical, BCM: 16)
   RES    ->    35 (Physical, BCM: 19)
```
