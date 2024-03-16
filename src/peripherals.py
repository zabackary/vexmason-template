from vex import *


class Peripherals:
    brain: Brain
    inertial: Inertial
    left_motors_list: list[Motor]
    left_motors: MotorGroup
    right_motors_list: list[Motor]
    right_motors: MotorGroup
    controller: Controller
    claw_piston: Pneumatics
    wing_piston: Pneumatics
    front_sonar: Sonar

    WHEEL_TRAVEL_MM: int
    WHEEL_TRACK_WIDTH_MM: int


class RealBotPeripherals(Peripherals):
    WHEEL_TRAVEL_MM = 460
    WHEEL_TRACK_WIDTH_MM = 305

    def __init__(self) -> None:
        self.brain = Brain()
        self.controller = Controller()

        self.wing_piston = Pneumatics(self.brain.three_wire_port.h)
        self.claw_piston = Pneumatics(self.brain.three_wire_port.g)

        self.front_sonar = Sonar(self.brain.three_wire_port.c)

        self.inertial = Inertial(Ports.PORT6)

        self.left_motors_list = [
            Motor(Ports.PORT20, False),
            Motor(Ports.PORT19, True),
            Motor(Ports.PORT9, False),
            Motor(Ports.PORT8, True),
        ]
        self.left_motors = MotorGroup(*self.left_motors_list)
        self.right_motors_list = [
            Motor(Ports.PORT12, True),
            Motor(Ports.PORT13, False),
            Motor(Ports.PORT1, True),
            Motor(Ports.PORT2, False),
        ]
        self.right_motors = MotorGroup(*self.right_motors_list)


class TestBotPeripherals(Peripherals):
    WHEEL_TRAVEL_MM = 320
    WHEEL_TRACK_WIDTH_MM = 265

    def __init__(self) -> None:
        self.brain = Brain()
        self.controller = Controller()

        self.wing_piston = Pneumatics(self.brain.three_wire_port.f)
        self.claw_piston = Pneumatics(self.brain.three_wire_port.a)

        self.front_sonar = Sonar(self.brain.three_wire_port.c)

        self.inertial = Inertial(Ports.PORT5)

        self.left_motors_list = [
            Motor(Ports.PORT20),
            Motor(Ports.PORT19)
        ]
        self.left_motors = MotorGroup(*self.left_motors_list)
        self.right_motors_list = [
            Motor(Ports.PORT11, True),
            Motor(Ports.PORT1, True)
        ]
        self.right_motors = MotorGroup(*self.right_motors_list)
