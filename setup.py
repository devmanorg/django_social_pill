import os
from os.path import join, dirname
from setuptools import find_packages, setup


# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))


def load_readme():
    with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
        return readme.read()


def load_requirements():
    return open(join(dirname(__file__), 'requirements.txt')).readlines()


setup(
    name='django-social-pill',
    version='0.0.2',
    packages=find_packages(),
    include_package_data=True,
    license='MIT License',
    description='A Django app to speed up social auth adoption.',
    long_description=load_readme(),
    install_requires=load_requirements()
)
