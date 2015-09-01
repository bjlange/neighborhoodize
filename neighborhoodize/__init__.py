"""A module for taking latitude, longitude pairs and returning which
neighborhood they're located in. Currently Chicago only."""

# imports
import os
import sys
import pygeoif
import shapely
from bs4 import BeautifulSoup
from fastkml import kml
import fiona

# constants

PATH_TO_THIS_FILE = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(PATH_TO_THIS_FILE, 'data')

# relevant meta_key: PRI_NEIGH
CHICAGO_NEIGHBORHOODS = os.path.join(DATA_DIR,
                                     "Boundaries - Neighborhoods.kml")
# relevant meta_key: NTAName
NYC_NEIGHBORHOODS = os.path.join(DATA_DIR,
                                 "NYC - Neighborhood Tabulation Areas.kml")

NEW_YORK_ZILLOW = os.path.join(DATA_DIR, "ZillowNeighborhoods-NY")


# exception classes

# interface functions
def read_neighborhood_kml(filename, map_name, meta_key="PRI_NEIGH"):
    """Takes a path to a KML file. Returns a dictionary of Shapely
    polygons keyed by specified metadata field (default: primary
    neighborhood).
    TODO: improve docstring
    """
    with open(filename) as kml_file:
        kml_obj = kml.KML()
        kml_obj.from_string(kml_file.read())

    document = list(kml_obj.features())[0]

    hood_map = NeighborhoodMap(map_name)

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

        hood = Neighborhood(meta_dict[meta_key], shape_poly, meta_dict=meta_dict)
        hood_map.neighborhoods.append(hood)

    return hood_map


def read_zillow_shapefile(filename, map_name):
    hood_map = NeighborhoodMap(map_name)
    with fiona.open(filename) as data:
        for hood_data in data:
            metadata = dict(hood_data['properties'])
            geometry = shapely.geometry.shape(hood_data['geometry'])
            hood = Neighborhood(metadata['NAME'], geometry, meta_dict=metadata)
            hood_map.neighborhoods.append(hood)
    return hood_map


# classes
class Neighborhoodizer(object):
    def __init__(self):
        # self.hood_map = read_neighborhood_kml(NYC_NEIGHBORHOODS, "NYC", meta_key="NTAName")
        self.hood_map = read_zillow_shapefile(NEW_YORK_ZILLOW, "NY-Zillow")

    def get_neighborhoods(self, lat, lng):
        """Takes a latitude and a longitude and returns a list of matching
        neighborhood names."""
        point = shapely.geometry.Point(lng, lat)
        hoods = [hood.name for hood in self.hood_map.neighborhoods
                 if hood.polygon.contains(point)]
        return hoods


class NeighborhoodMap(object):
    """A NeighborhoodMap is a series of polygons representing
    neighborhoods, constructed from a file (KML only for the time
    being)"""
    neighborhoods = []

    def __init__(self, map_name):
        self.name = map_name


class Neighborhood(object):
    """A Neighborhood is a polygon defining geographic borders, with accompanying metadata.
    """

    def __init__(self, neighborhood_name, polygon, meta_dict=None):
        self.name = neighborhood_name
        self.polygon = polygon
        self.meta_dict = meta_dict


# internal functions & classes


def main():
    izer = Neighborhoodizer()
    # lat, lng = 41.925495, -87.705847
    # print "Should be Logan Square:"
    # print izer.get_neighborhoods(lat, lng)
    #
    # lat, lng = 41.927299, -87.646270
    # print "should be Lincoln Park:"
    # print izer.get_neighborhoods(lat, lng)

    lat, lng = 40.709467, -73.962600
    print "should be Williamsburg:"
    print izer.get_neighborhoods(lat, lng)

    return 0


if __name__ == "__main__":
    STATUS_CODE = main()
    sys.exit(STATUS_CODE)
