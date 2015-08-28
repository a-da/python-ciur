#!/usr/bin/env python
from setuptools import setup
import re

def parse_requirements(filename, editable=False):
    _ = []
    for line in open(filename, "r"):
        if re.search("^\s*(#|-)", line):
            continue
        line = re.search("^\s*(.*)\s*", line).group(1)

        if not line:
            continue

        if not editable:
            m = re.search("#egg=(...*)", line)
            if m:
                line = m.group(1)

        m = re.search("(.+) #.*", line)
        if m:
            line = m.group(1)

        _.append(line)

    return _

name = "ciur"
version = __import__(name).VERSION

setup(
    name=name,
    version=version,
    url='http://asta-s.eu',
    dependency_links=[
       "git+https://bitbucket.org/ada/ciur.git#egg=ciur"
    ],
    author_email="ada@asta-s.eu",
    author="Andrei Danciuc",
    description="Advanced python dict",
    license="TODO",
    long_description=open("README.rst").read(),
    packages=[
        "ciur",
        "ciur.common",
        "ciur.util"
    ],
    package_data={
        "": ["*.py", "requirements.txt"]
    },
    include_package_data=True,
    install_requires=parse_requirements("requirements.txt"),
    classifiers=[
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
    ],
)
