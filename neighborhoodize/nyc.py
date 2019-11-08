import os

from . import kml_parsers
from . import constants

NEIGHBORHOOD_TABULATION_AREAS = ("NYC Neighborhood Tabulation Areas",
                                 os.path.join(constants.DATA_DIR, "nyc",
                                 "NYC - Neighborhood Tabulation Areas.kml"),
                                 kml_parsers.parser_generator("NTAName"))
