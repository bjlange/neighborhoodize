"""A module for taking latitude, longitude pairs and returning which
neighborhood they're located in. Currently Chicago only."""

# imports
import sys

from . import city_of_chicago
from . import nyc
from . import zillow

from .common import NeighborhoodMap, Neighborhood


def main():
    return 0


if __name__ == "__main__":
    STATUS_CODE = main()
    sys.exit(STATUS_CODE)
