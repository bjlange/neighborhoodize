#!/usr/bin/env python

from distutils.core import setup

setup(name="Neighborhoodize",
      version='0.9.3',
      description='Utility for translating lat, long coordinates into '
                  'neighborhoods in various cities',
      author='Brian Lange',
      author_email='brian.lange@datascopeanalytics.com',
      url='https://github.com/bjlange/neighborhoodize',
      packages=['neighborhoodize', ],
      install_requires=[
          "Shapely >= 1.5.7",
          "beautifulsoup4 >= 4.3.2",
          "fastkml >= 0.9",
          "fiona >= 1.6.2"
      ],
      keywords=['neighborhood','gis','boundaries'],
      classifiers = [],
      zip_safe=False,
      include_package_data=True)
