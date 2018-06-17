from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from device.mpu6050 import mpu6050
from device.bmp180 import BMP180
from device.pca9685 import pca9685

servo = None

def index(request):
    return HttpResponse("Hello World! It is working")

@csrf_exempt
def drive(request, channel_id, pulse_width):
    global servo
    response = "You're driving the robot %s."
    if(servo is None):
        servo = pca9685(0x40)
    servo.OutPut(int(channel_id), int(pulse_width));
    return HttpResponse(response % channel_id)