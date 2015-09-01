#!/usr/bin/env python

from distutils.core import setup

setup(name="Neighborhoodize",
      version='0.9',
      description='Utility for translating lat, long coordinates into Chicago '
                  'neighborhoods',
      author='Brian Lange',
      author_email='brian.lange@datascopeanalytics.com',
      url='https://github.com/bjlange/neighborhoodize',
      packages=['neighborhoodize', ],
      package_data={'neighborhoodize': ['data/*']},
      install_requires=[
          "Shapely >= 1.5.7",
          "beautifulsoup4 >= 4.3.2",
          "fastkml >= 0.9"],
      )
