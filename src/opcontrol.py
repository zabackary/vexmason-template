from vex import *

from peripherals import Peripherals


def opcontrol(p: Peripherals):
    while True:
        # Spin the left and right groups based on the controller
        axis3 = p.controller.axis3.position()
        if axis3 < 3 and axis3 > -3:  # dead zone
            axis3 = 0

        axis1 = p.controller.axis1.position()
        if axis1 < 3 and axis1 > -3:  # dead zone
            axis1 = 0

        p.left_motors.spin(
            DirectionType.FORWARD,
            axis3 + axis1,
            VelocityUnits.PERCENT)
        p.right_motors.spin(
            DirectionType.FORWARD,
            axis3 - axis1,
            VelocityUnits.PERCENT)

        wait(20)
