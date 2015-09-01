# Neighborhoodize

Neighborhoodize uses `fastkml`, `fiona`, and `shapely` to determine what 
neighborhood a latitude, longitude pair resides in.

## Usage example
```
import neighborhoodize

hood_map = neighborhoodize.NeighborhoodMap(neighborhoodize.zillow.ILLINOIS)

hood_map.get_neighborhoods(41.879617, -87.633463)
# [u'Loop']
```

## NeighborhoodMaps available for use
### Zillow 
Zillow provides their neighborhood boundaries free under Creative Commons. 
These are good boundaries to use for colloquial/property-value related use cases.

- zillow.ILLINOIS
- zillow.NEW_YORK
- more coming soon...

### City of New York
- nyc.NEIGHBORHOOD_TABULATION_AREAS (these are [defined](http://www.nyc.gov/html/dcp/html/bytes/applbyte.shtml) 
by the Department of City Planning)

### City of Chicago
- city_of_chicago.NEIGHBORHOODS (these are 
[defined](https://data.cityofchicago.org/Facilities-Geographic-Boundaries/Boundaries-Neighborhoods/9wp7-iasj) 
by the Department of Tourism)

*Have other boundaries you want to see in the package? Open an issue, or, 
better yet, make a pull request!*

## Other implementations

jkgiesler's [`chicago_neighborhoods`](https://github.com/jkgiesler/chicago_neighborhoods) 
provides similar functionality for Chicago without dependencies.

coddingtonbear's [`django-neighborhoods`](https://github.com/coddingtonbear/django-neighborhoods)
provides similar functionality as a Django app.

## Future of this project
(see Issues for details/to make suggestions)

 - ability to use Chicago community areas or wards instead of 2012 neighborhoods
 - ability to use subarb boundaries for Chicagoland areas not inside the city limits
 - additional cities
