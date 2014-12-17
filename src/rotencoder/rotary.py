import logging

logger = logging.getLogger(__name__)

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

LEFT=0
RIGHT=1


# Based on  http://lxr.free-electrons.com/source/drivers/input/misc/rotary_encoder.c
class RotaryEncoder(object):
    def __init__(self, gpio_a, gpio_b, gpio_p):
        self.gpio_a=gpio_a
        self.gpio_b=gpio_b
        self.gpio_p=gpio_p
        self.dir =0
        self.armed=False

        GPIO.setup(gpio_a, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.add_event_detect(gpio_a, GPIO.BOTH)
        GPIO.add_event_callback(gpio_a, self.callback_rotary)

        GPIO.setup(gpio_b, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.add_event_detect(gpio_b, GPIO.BOTH)
        GPIO.add_event_callback(gpio_b, self.callback_rotary)


        GPIO.setup(gpio_p, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.add_event_detect(gpio_p, GPIO.BOTH)
        GPIO.add_event_callback(gpio_p, self.callback_push)




    def callback_rotary(self, channel):
        state = self.get_state()

        if (state==0x0):
            if (self.armed):
                self.report_rotation(self.dir)
                self.armed=False
        elif (state==0x1 or state==0x2):
            if (self.armed):
                self.dir=state-1 
        elif (state==0x3):
            self.armed=True

    def report_rotation(self, direction):
        if (direction==LEFT):
            logger.info("Left")
        else:
            logger.info("Right")


    def get_state(self):
        a=GPIO.input(self.gpio_a)
        b=GPIO.input(self.gpio_b)
        return ((a<<1) | b ) 

    def callback_push(self, channel):
        state = GPIO.input(self.gpio_p)
        if (state):
            self.report_push(True)
        else:
            self.report_push(False)

    def report_push(self, pushed):
        if (pushed):
            logger.info("Pushed")
        else:
            logger.info("Released")

