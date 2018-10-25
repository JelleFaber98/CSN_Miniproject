from urllib.request import urlopen
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # Set pin 10 to be an input pin and set initial value to be pulled low (off)

# constanten: hostname van de server en definitie van de knop
hostname='192.168.42.5:5000' # vul hier de juiste hostname en poort in

# hulpfunctie voor sturen van een bericht naar de server
#    het antwoord wordt simpelweg geprint
def httpconnect(action):
    url='http://{}/{}'.format(hostname,action)
    try:
        print(urlopen(url).read().decode())
    except:
        print("Verbinding naar {} kon niet gemaakt worden".format(url))
        exit()

# actie voor ingedrukte knop (voor gebruik met gpiozero geen argument)
def knopin():
    httpconnect('knopin')

# klaar voor gebruik, open de basis URL
httpconnect('')

# blijf oneindig deze lus maken, waarbij input gelezen wordt
#     en de functie knopin() aangeroepen bij invoer van '+' (gevolgd door enter)
#     en de functie knopuit() bij invoer van '-' (gevolgd door enter)
while True:
    invoer=input()
    if invoer == '+' or GPIO.input(24) == 0:
        knopin()
GPIO.cleanup()