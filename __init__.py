"""A module for taking latitude, longitude pairs and returning which
neighborhood they're located in. Currently Chicago only."""

# imports
import sys

# constants

# exception classes

# interface functions
def read_kml_to_polygon(filename):
    """Takes a path to a KML file. Returns a (list of?) Shapely polygons
    TODO: improve docstring
    """
    raise NotImplementedError

# classes

# internal functions & classes


def main():
    return 0

if __name__ == "__main__":
    STATUS_CODE = main()
    sys.exit(STATUS_CODE)
