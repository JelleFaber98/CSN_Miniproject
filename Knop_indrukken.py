import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM) # Use physical pin numbering
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)

while True: # Run forever
    if GPIO.input(24) == 1:
        print("Button was pushed!")
GPIO.cleanup()