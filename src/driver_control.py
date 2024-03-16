from vex import *

from constants import TURNING_SPEED_FACTOR
from peripherals import Peripherals
from utils import debug


def _damp_controller(val):
    """ Dampens a value on a quadratic curve to match perceived human motor speeds """
    value = math.pow(0.1*val, 2)
    if val < 0:
        return -value
    else:
        return value


def driver_control(p: Peripherals):
    last_wing_pressing = False
    while True:
        # Spin the left and right groups based on the controller
        axis3 = p.controller.axis3.position()
        # ignore low values b/c they're likely controller drift
        if -5 < axis3 < 5:
            axis3 = 0
        axis3 = _damp_controller(axis3)

        # ignore low values b/c they're likely controller drift
        axis1 = p.controller.axis1.position()
        if -5 < axis1 < 5:
            axis1 = 0
        axis1 = _damp_controller(axis1)

        p.left_motors.spin(
            DirectionType.FORWARD,
            axis3 + axis1*TURNING_SPEED_FACTOR,
            VelocityUnits.PERCENT)
        p.right_motors.spin(
            DirectionType.FORWARD,
            axis3 - axis1*TURNING_SPEED_FACTOR,
            VelocityUnits.PERCENT)

        wing_pressing = p.controller.buttonL1.pressing()
        if wing_pressing and not last_wing_pressing:
            if p.wing_piston.value():
                p.wing_piston.close()
            else:
                p.wing_piston.open()
        last_wing_pressing = wing_pressing

        wait(20)
