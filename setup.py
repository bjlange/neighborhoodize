#!/usr/bin/env python

from distutils.core import setup

setup(name="Neighborhoodize",
      version='0.9.2',
      description='Utility for translating lat, long coordinates into '
                  'neighborhoods in various cities',
      author='Brian Lange',
      author_email='brian.lange@datascopeanalytics.com',
      url='https://github.com/bjlange/neighborhoodize',
      packages=['neighborhoodize', ],
      package_data={'neighborhoodize': ['data/*']},
      download_url = 'https://github.com/bjlange/neighborhoodize/tarball/0.9.2',
      install_requires=[
          "Shapely >= 1.5.7",
          "beautifulsoup4 >= 4.3.2",
          "fastkml >= 0.9",
          "fiona >= 1.6.2"
      ],
      keywords=['neighborhood','gis','boundaries'],
      classifiers = [],
      )
