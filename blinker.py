import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
i = 1
import time
try:
 while i == 1:
  GPIO.output(18, GPIO.HIGH)
  time.sleep(0.25)
  i = 2
except KeyboardInterrupt:
 GPIO.cleanup()

GPIO.output(18, GPIO.LOW)
