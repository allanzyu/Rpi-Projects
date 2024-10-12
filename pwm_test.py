import RPi.GPIO as GPIO
from time import sleep

LED = 12
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED, GPIO.OUT)
pi_pwm = GPIO.PWM(LED, 1000)
pi_pwm.start(0)

while True:
    print("start of low")
    for duty in range(0,101,1):
        print(duty)
        pi_pwm.ChangeDutyCycle(duty)
        sleep(0.01)
    sleep(0.5)
    print("start of high")
    for duty in range(100,-1,-1):
        print(duty)
        pi_pwm.ChangeDutyCycle(duty)
        sleep(0.01)
    sleep(0.5)