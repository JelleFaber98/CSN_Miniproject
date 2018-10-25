from flask import Flask
import RPi.GPIO as GPIO
import time

app = Flask(__name__)   # standaard gebruik van Flask
@app.route("/")
def ready():
    return "Server beschikbaar\n"

@app.route("/alarmAaan")

def alarmAan():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(18, GPIO.OUT)
    GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # Set pin 10 to be an input pin and set initial value to be pulled low (off)
    GPIO.setup(17, GPIO.OUT)
    while True:
        if GPIO.input(24) == 0:
            GPIO.output(18, GPIO.HIGH)
            GPIO.output(17, GPIO.HIGH)
            time.sleep(1)
            GPIO.output(18, GPIO.LOW)
            GPIO.output(17, GPIO.LOW)
            time.sleep(1)
        else:
            GPIO.cleanup()
            break
    return "het alarm is uitgeschakeld\n"

if __name__ == '__main__':
    app.run(host='0.0.0.0')
