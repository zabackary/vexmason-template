from vex import *

from constants import WHEEL_TRACK_WIDTH_MM, WHEEL_TRAVEL_MM


class Peripherals:
    brain: Brain
    controller: Controller
    inertial: Inertial
    drivetrain: SmartDrive
    left_motors: MotorGroup
    right_motors: MotorGroup

    def __init__(self) -> None:
        self.brain = Brain()
        self.controller = Controller()

        motor_left_front = Motor(Ports.PORT1)
        motor_left_back = Motor(Ports.PORT2)
        motor_right_front = Motor(Ports.PORT3, True)
        motor_right_back = Motor(Ports.PORT4, True)
        self.inertial = Inertial(Ports.PORT5)

        self.left_motors = MotorGroup(motor_left_front, motor_left_back)
        self.right_motors = MotorGroup(motor_right_front, motor_right_back)
        self.drivetrain = SmartDrive(
            self.left_motors,
            self.right_motors,
            self.inertial,
            WHEEL_TRAVEL_MM,
            WHEEL_TRACK_WIDTH_MM
        )
