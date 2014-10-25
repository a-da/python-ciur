#!/usr/bin/env python
from setuptools import setup
from pip.req import parse_requirements
from __init__ import VERSION

setup(
    name="ciur",
    version=VERSION,
    url='http://asta-s.eu',
    dependency_links=[
       "git+https://bitbucket.org/ada/ciur.git#egg=ciur"
    ],
    author_email="ada@asta-s.eu",
    author="Andrei Danciuc",
    description="Advanced python dict",
    license="TODO",
    long_description=open("README.rst").read(),
    packages=[],
    package_data={
        "": ["*.py", "requirements.txt"]
    },
    include_package_data=True,
    install_requires=[str(ir.req) for ir in parse_requirements("requirements.txt")]
)
