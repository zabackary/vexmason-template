from vex import *

from autonomous_route1 import autonomous_route1
from constants import AUTONOMOUS_ROUTE, COMPETITION_MODE
from opcontrol import opcontrol
from peripherals import Peripherals

peripherals = Peripherals()


def autonomous():
    match AUTONOMOUS_ROUTE:
        case "route1":
            autonomous_route1(peripherals)


def driver():
    # restart the opcontrol routine on errors so if it crashes we don't
    # automatically lose the match
    while True:
        try:
            opcontrol(peripherals)
        except:
            pass


if COMPETITION_MODE:
    Competition(driver, autonomous)
else:
    autonomous()
