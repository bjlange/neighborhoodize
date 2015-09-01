import os

import kml_parsers
import constants

NEIGHBORHOOD_TABULATION_AREAS = ("NYC Neighborhood Tabulation Areas",
                                 os.path.join(constants.DATA_DIR, "nyc",
                                 "NYC - Neighborhood Tabulation Areas.kml"),
                                 kml_parsers.parser_generator("NTAName"))
