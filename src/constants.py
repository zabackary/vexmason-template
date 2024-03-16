""" Constants which will be replaced dynamically at build time. """

# remove the underscores to keep it tidy, and python-compiler
# doesn't export symbols starting with underscores anyway.
__COMPETITION_MODE__ = True
COMPETITION_MODE = __COMPETITION_MODE__

__USE_REAL_BOT__ = True
USE_REAL_BOT = __USE_REAL_BOT__

__AUTONOMOUS_ROUTE__ = "No route"
AUTONOMOUS_ROUTE = __AUTONOMOUS_ROUTE__

__TURNING_SPEED_FACTOR__ = 0.5
TURNING_SPEED_FACTOR = __TURNING_SPEED_FACTOR__
