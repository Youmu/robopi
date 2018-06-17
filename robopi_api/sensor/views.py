from django.http import HttpResponse
from device.mpu6050 import mpu6050
from device.bmp180 import BMP180
from device.pca9685 import pca9685
def index(request):
    return HttpResponse("Hello World! It is working")

def accelerator(request):
    sensor = mpu6050(0x69)
    sensor.set_accel_range(mpu6050.ACCEL_RANGE_2G)
    acc_data = sensor.get_accel_data()
    return HttpResponse(acc_data.__str__())

def gyro(request):
    sensor = mpu6050(0x69)
    sensor.set_gyro_range(mpu6050.GYRO_RANGE_250DEG)
    gyro_data = sensor.get_gyro_data()
    return HttpResponse(gyro_data.__str__())

def baro(request):
    sensor = BMP180.BMP180()
    pressure = sensor.read_pressure()
    return HttpResponse('{{"baro":{0}}}'.format(pressure))

def refresh(request, question_id):
    return HttpResponse("You're refreshing the sensor data %s." % question_id)
