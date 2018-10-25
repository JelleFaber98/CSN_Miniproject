from flask import Flask
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)  # Hier word het lampje geconfigureerd
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)   # Hier word de knop mee geconfigureerd
GPIO.setup(17, GPIO.OUT)  # Hier word de beeper geconfigureerd

app = Flask(__name__)

@app.route("/")

def ready():
    return "Server beschikbaar\n"

@app.route("/alarmAan")

def alarmAan():

    while True:
        if GPIO.input(24) == 0: # Hier word gekeken of de knop niet is ingedrukt
            GPIO.output(18, GPIO.HIGH)  # Hier gaat het lampje branden
            GPIO.output(17, GPIO.HIGH)  # Hier gaat de beeper aan
            time.sleep(1)  # Hier komt een pauze van 1 seconden
            GPIO.output(18, GPIO.LOW)  # Hier gaat het lampje uit
            GPIO.output(17, GPIO.LOW)  # Hier gaat de beeper uit
            time.sleep(1)  # Hier komt een pauze van 1 seconden
        else:
            GPIO.cleanup()  # Hier word de GPIO opgeruimd
            break
    return "het alarm is uitgeschakeld\n"

if __name__ == '__main__':
    app.run(host='0.0.0.0')
