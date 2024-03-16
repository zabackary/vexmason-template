from _route import TestRoute as TestRouteCategory


class TestRoute(TestRouteCategory):
    @staticmethod
    def name():
        return "Test route"

    @staticmethod
    def run(p, d):
        while True:
            d.drive(1000)
            d.turn(180)
