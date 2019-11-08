from . import common
import pygeoif
import shapely
from bs4 import BeautifulSoup
from fastkml import kml


def parser_generator(name_meta_key):
    """
    Closure that returns a parser function for KMLs such as the ones from the
    City of Chicago and New York City.
    Takes the key for the metadata dictionary that corresponds
    to neighborhood name.
    """

    def read_neighborhood_kml(filename):
        """ General purpose parser function for KMLs such as ones from the City of
        Chicago and New York City.
        Takes a filepath, returns a list of Neighborhoods.
        """
        with open(filename) as kml_file:
            kml_obj = kml.KML()
            kml_obj.from_string(kml_file.read())

        document = list(kml_obj.features())[0]

        hoods = []

        for placemark in document.features():
            # print "EXTENDED"
            # print placemark.extended_data
            # print "DESC"
            metadata = BeautifulSoup(placemark.description)
            attr_names = [el.text for el in
                          metadata.find_all('span', 'atr-name')]
            attr_vals = [el.text for el in
                         metadata.find_all('span', 'atr-value')]

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

            hood = common.Neighborhood(meta_dict[name_meta_key],
                                shape_poly,
                                meta_dict=meta_dict)
            hoods.append(hood)

        return hoods

    return read_neighborhood_kml
