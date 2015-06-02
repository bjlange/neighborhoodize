"""A module for taking latitude, longitude pairs and returning which
neighborhood they're located in. Currently Chicago only."""

# imports
import os
import sys
import pygeoif
import shapely
from bs4 import BeautifulSoup
from fastkml import kml

# constants

PATH_TO_THIS_FILE = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(PATH_TO_THIS_FILE, 'data')

CHICAGO_NEIGHBORHOODS = os.path.join(DATA_DIR,
                                     "Boundaries - Neighborhoods.kml")
NYC_NEIGHBORHOODS = os.path.join(DATA_DIR,
                                 "NYC - Neighborhood Tabulation Areas.kml")



# exception classes

# interface functions
def read_neighborhood_kml(filename, meta_key="PRI_NEIGH"):
    """Takes a path to a KML file. Returns a dictionary of Shapely
    polygons keyed by specified metadata field (default: primary
    neighborhood).
    TODO: improve docstring
    """
    with open(filename) as kml_file:
        kml_obj = kml.KML()
        kml_obj.from_string(kml_file.read())

    document = list(kml_obj.features())[0]
    hood_polys = {}

    for placemark in document.features():
        # print "EXTENDED"
        # print placemark.extended_data
        # print "DESC"
        metadata = BeautifulSoup(placemark.description)
        attr_names = [el.text for el in metadata.find_all('span', 'atr-name')]
        attr_vals = [el.text for el in metadata.find_all('span', 'atr-value')]

        meta_dict = dict(zip(attr_names, attr_vals))
        # example:
        # {u'PRI_NEIGH': u'Austin',
        #  u'SEC_NEIGH': u'AUSTIN',
        #  u'SHAPE_AREA': u'1.70037750826E8',
        #  u'SHAPE_LEN': u'55473.345911',
        #  u'_SocrataID': u'2avh-wj5s'}

        poly = [g for g in placemark.geometry.geoms
                if isinstance(g, pygeoif.geometry.Polygon)][0]
        shape_reader = shapely.geos.WKTReader(shapely.geos.lgeos)
        shape_poly = shape_reader.read(poly.wkt)

        hood_polys[meta_dict[meta_key]] = shape_poly
    return hood_polys

# classes
class Neighborhoodizer(object):

    def __init__(self):
        self.hood_polys = read_neighborhood_kml(CHICAGO_NEIGHBORHOODS)

    def get_neighborhoods(self, lat, lng):
        """Takes a latitude and a longitude and returns a list of matching
        neighborhood names."""
        point = shapely.geometry.Point(lng, lat)
        hoods = [name for name, poly in self.hood_polys.iteritems()
                 if poly.contains(point)]
        return hoods

class NeighborhoodMap(object):
    """A NeighborhoodMap is a series of polygons representing
    neighborhoods, constructed from a file (KML only for the time
    being)"""


    pass

# internal functions & classes


def main():
    izer = Neighborhoodizer()
    lat, lng = 41.925495, -87.705847
    print "Should be Logan Square:"
    print izer.get_neighborhoods(lat, lng)

    lat, lng = 41.927299, -87.646270
    print "should be Lincoln Park:"
    print izer.get_neighborhoods(lat, lng)

    return 0

if __name__ == "__main__":
    STATUS_CODE = main()
    sys.exit(STATUS_CODE)
