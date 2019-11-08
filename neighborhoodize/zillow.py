import os
import fiona
import shapely

from . import common
from . import constants


def read_zillow_shapefile(filename):
    hoods = []
    with fiona.open(filename) as data:
        for hood_data in data:
            metadata = dict(hood_data['properties'])
            geometry = shapely.geometry.shape(hood_data['geometry'])
            hood = common.Neighborhood(metadata['NAME'], geometry,
                                       meta_dict=metadata)
            hoods.append(hood)
    return hoods


NEW_YORK = ("New York State - Zillow",
            os.path.join(constants.DATA_DIR, "zillow", "ZillowNeighborhoods-NY"),
            read_zillow_shapefile)

ILLINOIS = ("Illinois State - Zillow",
            os.path.join(constants.DATA_DIR, "zillow", "ZillowNeighborhoods-IL"),
            read_zillow_shapefile)

