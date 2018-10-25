from flask import Flask
import RPi.GPIO as GPIO
import time


# constanten: de definitie van de Flask applicatie en de definitie van de LED
app = Flask(__name__)   # standaard gebruik van Flask
# de route bepaalt bij welk pad de onderstaande callback hoort
@app.route("/")
# functie die wanneer de knop is ingedrukt de LED aanzet
#     en een bevestiging geeft naar de client
def ready():
    # voer hier programmacode toe die van belang is
    #     wanneer de client zich voor het eerst meldt
    return "Server beschikbaar\n"

# de route bepaalt bij welk pad de onderstaande callback hoort
@app.route("/knopin")
# functie die wanneer de knop is ingedrukt de LED aanzet
#     en een bevestiging geeft naar de client
def knopin():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(18, GPIO.OUT)
    GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # Set pin 10 to be an input pin and set initial value to be pulled low (off)
    alarm = True
    while True:
        if GPIO.input(24) == 0:
            GPIO.output(18, GPIO.HIGH)
            time.sleep(1)
            GPIO.output(18, GPIO.LOW)
            time.sleep(1)
        else:
            GPIO.cleanup()
            break
    return "het alarm is uitgeschakeld\n"
    # voer hier programmacode toe die van belang is
    #     wanneer de client een knopdruk aangeeft

# manier om Flask vanuit Python te laten starten
#    host='0.0.0.0' zorgt ervoor dat op alle NICs geluisterd wordt
if __name__ == '__main__':
    app.run(host='0.0.0.0')