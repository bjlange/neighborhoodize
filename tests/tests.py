import neighborhoodize

# TODO: read these from a file so more neighborhoods can be tested
known_chicago_pairs = {
    (41.925495, -87.705847): ['Logan Square'],
    (41.927299, -87.646270): ['Lincoln Park']
}

known_nyc_pairs = {
    (40.709467, -73.962600): ['Williamsburg'] # only on Zillow
}

def test_chicago_city():
    params = neighborhoodize.city_of_chicago.NEIGHBORHOODS
    chicago_map = neighborhoodize.NeighborhoodMap(params)

    for (lat, lng), answer in known_chicago_pairs.iteritems():
        assert chicago_map.get_neighborhoods(lat, lng) == answer


def test_chicago_zillow():
    params = neighborhoodize.zillow.ILLINOIS
    chicago_map = neighborhoodize.NeighborhoodMap(params)

    for (lat, lng), answer in known_chicago_pairs.iteritems():
        assert chicago_map.get_neighborhoods(lat, lng) == answer

def test_nyc_zillow():
    params = neighborhoodize.zillow.NEW_YORK
    nyc_map = neighborhoodize.NeighborhoodMap(params)

    for (lat, lng), answer in known_nyc_pairs.iteritems():
        assert nyc_map.get_neighborhoods(lat, lng) == answer