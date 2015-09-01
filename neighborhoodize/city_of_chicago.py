import os

import kml_parsers
import constants

NEIGHBORHOODS = ("City of Chicago Neighborhoods",
                 os.path.join(constants.DATA_DIR, "city_of_chicago",
                              "Boundaries - Neighborhoods.kml"),
                 kml_parsers.parser_generator("PRI_NEIGH"))
