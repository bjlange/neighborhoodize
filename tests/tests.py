import neighborhoodize

# TODO: read these from a file so more neighborhoods can be tested
known_chicago_pairs = {
    (41.925495, -87.705847): ['Logan Square'],
    (41.927299, -87.646270): ['Lincoln Park']
}

known_zillow_nyc_pairs = {
    (40.709467, -73.962600): ['Williamsburg'],
    (40.786330, -73.975881): ['Upper West Side'],
    (40.668329, -73.977553): ['Park Slope']
}

known_city_nyc_pairs = {
    (40.709467, -73.962600): ['North Side-South Side'],
    (40.786330, -73.975881): ['Upper West Side'],
    (40.668329, -73.977553): ['Park Slope-Gowanus']
}

def test_chicago_city():
    params = neighborhoodize.city_of_chicago.NEIGHBORHOODS
    chicago_map = neighborhoodize.NeighborhoodMap(params)

    for (lat, lng), answer in known_chicago_pairs.iteritems():
        assert chicago_map.get_neighborhoods(lat, lng) == answer

def test_nyc_city():
    params = neighborhoodize.nyc.NEIGHBORHOOD_TABULATION_AREAS
    nyc_map = neighborhoodize.NeighborhoodMap(params)

    for (lat, lng), answer in known_city_nyc_pairs.iteritems():
        assert nyc_map.get_neighborhoods(lat, lng) == answer

def test_chicago_zillow():
    params = neighborhoodize.zillow.ILLINOIS
    chicago_map = neighborhoodize.NeighborhoodMap(params)

    for (lat, lng), answer in known_chicago_pairs.iteritems():
        assert chicago_map.get_neighborhoods(lat, lng) == answer


def test_nyc_zillow():
    params = neighborhoodize.zillow.NEW_YORK
    nyc_map = neighborhoodize.NeighborhoodMap(params)

    for (lat, lng), answer in known_zillow_nyc_pairs.iteritems():
        assert nyc_map.get_neighborhoods(lat, lng) == answer
