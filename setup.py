"""This setup.py is added for compatibility with Apache Beam dataflow pipelines."""
from setuptools import setup, find_packages


setup(
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
)
