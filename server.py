#!/usr/bin/python3

from gpiozero import LED
from flask import Flask

# constanten: de definitie van de Flask applicatie en de definitie van de LED
app = Flask(__name__)   # standaard gebruik van Flask
led = LED(17) # ofwel GPIO 0, zie https://cdn.sparkfun.com/assets/learn_tutorials/4/2/4/header_pinout.jpg (Koppelingen naar een externe site.)Koppelingen naar een externe site.

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
    # voer hier programmacode toe die van belang is
    #     wanneer de client een knopdruk aangeeft
    return "Knop gedrukt!\n"

# de route bepaalt bij welk pad de onderstaande callback hoort
@app.route("/knopuit")
# functie die wanneer de knop is losgelaten de LED uitzet
#     en een bevestiging geeft naar de client
def knopuit():
    # voer hier programmacode toe die van belang is
    #     wanneer de client het loslaten van de knop aangeeft
    return "Knop losgelaten!\n"

# manier om Flask vanuit Python te laten starten
#    host='0.0.0.0' zorgt ervoor dat op alle NICs geluisterd wordt
if __name__ == '__main__':
    app.run(host='0.0.0.0')