config = {
  "name": "continuator",
  "version": "0.0.1",
  "description": "Continuations in Stackless Python",
  "url": "https://github.com/BlackEarth/continuator.git",
  "author": "Sean Harrison",
  "author_email": "sah@blackearth.us",
  "license": "LGPL 3.0",
  "classifiers": [
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: Mozilla Public License Version 2.0",
    "Programming Language :: Python :: 3"
  ],
  "entry_points": {},
  "install_requires": [],
  "extras_require": {
    "dev": [],
    "test": []
  },
  "package_data": {
    "": []
    },
  "data_files": [],
  "scripts": []
}

import os, json
from setuptools import setup, find_packages
from codecs import open

path = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(path, 'README.md'), encoding='utf-8') as f:
    read_me = f.read()

setup(
    long_description=read_me,
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    **config
)
