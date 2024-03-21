import RPi.GPIO as GPIO
#BOARD didn't work so I used BCM instead and I setwarnings to false
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
#Since while 1 didn't work, I set i to 1 and when it's done, I broke the tey and while loop statements
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
