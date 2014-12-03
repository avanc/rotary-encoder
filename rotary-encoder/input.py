#! /usr/bin/env python2

from evdev import UInput, ecodes

import rotary

cap = { ecodes.EV_REL : [ecodes.REL_WHEEL],
        ecodes.EV_KEY : [ecodes.BTN_LEFT] }

ui = UInput(cap, name="Rotary", version = 0x1)


class RotaryDevice(rotary.RotaryEncoder):
    def report_rotation(self, direction):
        if (direction==rotary.LEFT):
            ui.write(ecodes.EV_REL, ecodes.REL_WHEEL, -1)
        else:
            ui.write(ecodes.EV_REL, ecodes.REL_WHEEL, 1)
        ui.syn()

    def report_push(self, pushed):
        if (pushed):
            ui.write(ecodes.EV_KEY, ecodes.BTN_LEFT, 1)
        else:
            ui.write(ecodes.EV_KEY, ecodes.BTN_LEFT, 0)


encoder=RotaryDevice(24,25,23)


import time

while True:
    time.sleep(19)

