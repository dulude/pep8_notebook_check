from distutils.core import setup
from setuptools import find_packages
setup(
    name='pep8_notebook_check',
    version='1',
    packages=[''],
    package_dir={'src'},
    packages=find_packages('src'),
    url='',
    license='MIT',
    author='dulude',
    author_email='dulude@stsci.edu',
    description='PEP8 style checker for python code embedded in Jupyter notebooks'
)
