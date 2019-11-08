#!/usr/bin/env python
import setuptools
from distutils.core import setup

setup(name="Neighborhoodize",
      version='0.9.6',
      description='Utility for translating lat, long coordinates into '
                  'neighborhoods in various cities',
      author='Brian Lange',
      author_email='thebrianlange@gmail.com',
      url='https://github.com/bjlange/neighborhoodize',
      download_url='https://github.com/bjlange/neighborhoodize/releases/tag/0.9.6',
      packages=['neighborhoodize', ],
      install_requires=[
          "Shapely >= 1.5.7",
          "beautifulsoup4 >= 4.4.0",
          "fastkml >= 0.9",
          "fiona >= 1.6.2"
      ],
      keywords=['neighborhood', 'gis', 'boundaries'],
      classifiers=[],
      include_package_data=True)
