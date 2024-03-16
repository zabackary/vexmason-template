# from peripherals import Peripherals
# from pid_drivetrain import PIDDrivetrain


class Route():
    @staticmethod
    def name() -> str:
        ...

    @staticmethod
    def category_name() -> str:
        ...

    @staticmethod
    # TODO: type these as Peripherals and Drivetrain
    def run(p, d) -> None:
        ...


class OffenseRoute(Route):
    @staticmethod
    def category_name() -> str:
        return "Offense"


class DefenseRoute(Route):
    @staticmethod
    def category_name() -> str:
        return "Defense"


class TestRoute(Route):
    @staticmethod
    def category_name() -> str:
        return "Test"


class EmptyRoute(Route):
    @staticmethod
    def name() -> str:
        return "No route"

    @staticmethod
    def category_name() -> str:
        return "No route!"

    is_empty_route = True
