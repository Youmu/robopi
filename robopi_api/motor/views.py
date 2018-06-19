from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from device.mpu6050 import mpu6050
from device.bmp180 import BMP180
from device.pca9685 import pca9685

servo = None

def index(request):
    return HttpResponse("Hello World! It is working")

@csrf_exempt
def directdrive(request, channel_id, pulse_width):
    global servo
    response = "You're driving the robot %s."
    if(servo is None):
        servo = pca9685(0x40)
    servo.OutPut(int(channel_id), int(pulse_width))
    return HttpResponse(response % channel_id)

@csrf_exempt
def move(request):
    global servo

    if(request.method != 'GET'):
        return HttpResponse("Only GET is supported")

    if(servo is None):
        servo = pca9685(0x40)
    x = float(request.GET.get('x', '0'))
    y = float(request.GET.get('y', '0'))
    r = float(request.GET.get('r', '0'))    
    response = "You're moving the robot: {0},{1},{2}".format(x,y,r)
    v1 = x - r + 1500
    v2 = -0.5 * x - 0.866 * y - r + 1500
    v0 = -0.5 * x + 0.866 * y - r + 1500

    servo.OutPut(0, int(v0))
    servo.OutPut(1, int(v1))
    servo.OutPut(2, int(v2))

    return HttpResponse(response)