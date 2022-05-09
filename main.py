from time import sleep
import requests
import RPi.GPIO as GPIO
from datetime import datetime
#instalar no sistema: nodejs e npm
#instalar o json-server com root
#criar um db.json
def main():
        i=0
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(8, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setwarnings(False)
        while True:
                sleep(.2)
                print("Estado do GPIO 14:",GPIO.input(8))
                if (GPIO.input(8) == GPIO.HIGH):
                        dados = {"hora":datetime.now(), "Distância":323}
                        r = requests.post(url="http://localhost:3000/alarmes", data=dados)
                        print("Alarme enviado!")
                        print(r)

if __name__ == "__main__":
        main()
