import shapely


class NeighborhoodMap(object):
    """A NeighborhoodMap is a series of polygons representing
    neighborhoods, constructed from a file.
    Constructor takes a tuple with three things:
    - name for the map
    - a filepath
    - a parser function for that file.
    Parser functions take the filepath and return a list of Neighborhoods.
    """
    neighborhoods = []

    def get_neighborhoods(self, lat, lng):
        """Takes a latitude and a longitude and returns a list of matching
        neighborhood names."""
        point = shapely.geometry.Point(lng, lat)
        hoods = [hood.name for hood in self.neighborhoods
                 if hood.polygon.contains(point)]
        return hoods

    def __init__(self, arg_tuple):
        map_name, filepath, parser_fn = arg_tuple
        self.name = map_name
        self.neighborhoods = parser_fn(filepath)


class Neighborhood(object):
    """A Neighborhood is a (Shapely) polygon defining geographic borders,
    with accompanying metadata.
    """

    def __init__(self, neighborhood_name, polygon, meta_dict=None):
        self.name = neighborhood_name
        self.polygon = polygon
        self.meta_dict = meta_dict
