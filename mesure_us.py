#!/usr/bin/python3
# -*-coding:Utf-8 -*
""" Programme de mesure en continue par capteur utrason
Version n° 1.0.1
Date de version : 15/03/2016
Auteur : Christophe MAGINOT """

import RPi.GPIO as GPIO
import time
from datetime import date

# paramétrage des ports GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(16, GPIO.IN)

print("Mesure en cours...")

# On contrôle que la broche Trig est à un potantiel bas et on lui laisse le temps de s'initialiser

GPIO.output(20, False)
print("Attente de l'initialisation du capteur")
time.sleep(2)

# déclecnhement de la mesure par envoi d'une impulsion de 10µs sur la broche TRIG
GPIO.output(20, True)
time.sleep(0.00001)
GPIO.output(TRIG, False)

# Horodatage du début du signal haut
while GPIO.input(16) == 0:
    pulse_start = time.time()

# Horodatage de la fin du signal Haut
while GPIO.input(16) == 1:
    pulse_end = time.time()
    
# Calculs
pulse_duration = pulse_end - pulse_start
distance = pulse_duration * 17150
distance = round(distance, 2)

#Affichage du résultat
print("Distance: ", distance, " cm")

# réinitialisation des broches
GPIO.cleanup()
