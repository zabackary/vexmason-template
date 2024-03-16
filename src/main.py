from vex import *

from constants import AUTONOMOUS_ROUTE, COMPETITION_MODE, USE_REAL_BOT
from driver_control import driver_control
from peripherals import RealBotPeripherals, TestBotPeripherals
from routes import routes
from utils import has_interaction

selected_autonomous: str = AUTONOMOUS_ROUTE

if USE_REAL_BOT:
    peripherals = RealBotPeripherals()
else:
    peripherals = TestBotPeripherals()
drivetrain = SmartDrive(
    lm=peripherals.left_motors,
    rm=peripherals.right_motors,
    wheelTravel=peripherals.WHEEL_TRAVEL_MM,
    trackWidth=peripherals.WHEEL_TRACK_WIDTH_MM,
    g=peripherals.inertial
)


def autonomous():
    route = None
    for possible_route in routes:
        if possible_route.name() == selected_autonomous:
            route = possible_route
    if route is None:
        raise Exception("undefined route! {}".format(route))
    route.run(peripherals, drivetrain)


def driver():
    # don't run driver control if the controller is disabled
    while not has_interaction(peripherals):
        pass
    # keep running the driver control loop if it crashes for redundancy
    while True:
        try:
            driver_control(peripherals)
        except Exception:
            pass


if COMPETITION_MODE:
    Competition(driver, autonomous)
else:
    autonomous()
