from urllib.request import urlopen
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # Hier word de knop geconfigureerd
hostname='192.168.42.5:5000'  # Dit is het IP adres van de server

def httpconnect(action):
    url='http://{}/{}'.format(hostname, action)
    try:
        print(urlopen(url).read().decode())
    except:
        print("Verbinding naar {} kon niet gemaakt worden".format(url))  # Als je niet kan verbinden met de server word deze melding gegeven
        exit()

def alarmAan():
    httpconnect('alarmAan')  # Hiermee word er verbinding gemaakt met de server en word de alarmAan functie aangeroepen op de server

httpconnect('')

while True:
    if GPIO.input(21) == 1:  # Hier word gekeken of de knop is ingedrukt
        alarmAan()
GPIO.cleanup()