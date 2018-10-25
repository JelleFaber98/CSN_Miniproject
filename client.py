from urllib.request import urlopen
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
hostname='192.168.42.5:5000'

def httpconnect(action):
    url='http://{}/{}'.format(hostname, action)
    try:
        print(urlopen(url).read().decode())
    except:
        print("Verbinding naar {} kon niet gemaakt worden".format(url))
        exit()

def alarmAan():
    httpconnect('alarmAan')

httpconnect('')

while True:
    if GPIO.input(21) == 1:
        alarmAan()
GPIO.cleanup()