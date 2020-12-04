import os
from setuptools import setup, find_packages

version = '0.1'
description = "Obtener cambios de repositorios contenidos en una carpeta"

with open("README.md", "r") as fh:
  long_description = fh.read()

setup(
	name = "puller-cli",
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
    'console_scripts': ['puller=puller.puller:main'],
  }
)