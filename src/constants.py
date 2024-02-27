""" Constants which will be replaced dynamically at build time. """

# IMPORTANT NOTE:
# Make sure this file is kept up-to-date with .vscode/vexmason-config.json

# remove the underscores to keep it tidy, and python-compiler
# doesn't export symbols starting with underscores anyway.
__AUTONOMOUS_ROUTE__: str | None = None
AUTONOMOUS_ROUTE = __AUTONOMOUS_ROUTE__

__COMPETITION_MODE__ = True
COMPETITION_MODE = __COMPETITION_MODE__

__WHEEL_TRAVEL_MM__ = 320
WHEEL_TRAVEL_MM = __WHEEL_TRAVEL_MM__

__WHEEL_TRACK_WIDTH_MM__ = 265
WHEEL_TRACK_WIDTH_MM = __WHEEL_TRACK_WIDTH_MM__
