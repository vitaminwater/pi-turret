#!/bin/env python

import time

from servos import Servos

SERVO_I2C_ADDRESS	= 0x40		# I2C address of the PCA9685-based servo controller
SERVO_XAXIS_CHANNEL = 0			# Channel for the x axis rotation which controls laser up/down
SERVO_YAXIS_CHANNEL = 1			# Channel for the y axis rotation which controls laser left/right
SERVO_PWM_FREQ		= 50		# PWM frequency for the servos in HZ (should be 50)
SERVO_MIN			= 200		# Minimum rotation value for the servo, should be -90 degrees of rotation.
SERVO_MAX			= 600		# Maximum rotation value for the servo, should be 90 degrees of rotation.
SERVO_CENTER		= 330		# Center value for the servo, should be 0 degrees of rotation.

s = Servos(SERVO_I2C_ADDRESS, SERVO_XAXIS_CHANNEL, SERVO_YAXIS_CHANNEL, SERVO_PWM_FREQ)

for i in range(SERVO_MIN, SERVO_MAX):
    s.setXAxis(i)
    s.setYAxis(i)
    print('i: {0}'.format(i))
    time.sleep(0.01)

s.setXAxis(SERVO_CENTER)
s.setYAxis(SERVO_CENTER)