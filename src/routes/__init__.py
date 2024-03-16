from _route import EmptyRoute, Route
from route_o1 import O1Route
from route_test import TestRoute

routes: list[type[Route]] = [O1Route, TestRoute, EmptyRoute]

__all__ = ["Route", "routes"]
