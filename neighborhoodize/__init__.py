"""A module for taking latitude, longitude pairs and returning which
neighborhood they're located in. Currently Chicago only."""

# imports
import sys

import city_of_chicago
import nyc
import zillow

from common import NeighborhoodMap, Neighborhood


def main():
    chicago_map = city_of_chicago.NEIGHBORHOODS
    lat, lng = 41.925495, -87.705847
    print "Should be Logan Square:"
    print chicago_map.get_neighborhoods(lat, lng)

    lat, lng = 41.927299, -87.646270
    print "should be Lincoln Park:"
    print chicago_map.get_neighborhoods(lat, lng)

    # lat, lng = 40.709467, -73.962600
    # print "should be Williamsburg:"
    # print izer.get_neighborhoods(lat, lng)

    return 0


if __name__ == "__main__":
    STATUS_CODE = main()
    sys.exit(STATUS_CODE)
