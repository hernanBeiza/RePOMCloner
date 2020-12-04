import os
from setuptools import setup, find_packages

version = '0.1'
description = "Clonar todos los repositorios ingresados en un pom.xml"

with open("README.md", "r") as fh:
  long_description = fh.read()

setup(
	name = "repomcloner-cli",
	version = version,
	url = 'http://hiperactivo.cl',
	license = 'BSD',
	description = description,
	long_description = long_description,
	author = 'Hernán Beiza',
	author_email = 'hernan@hiperactivo.cl',
	packages = find_packages('src'),
	package_dir = {'': 'src'},
	install_requires = ['setuptools'],
  entry_points = {
    'console_scripts': ['repomcloner=repomcloner.repomcloner:main'],
  }
)