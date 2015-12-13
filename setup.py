#!/usr/bin/env python
from setuptools import setup
import re
import ciur


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

setup(
    name=ciur.__title__,
    version=ciur.__version__,
    url=ciur.__git__,
    dependency_links=[
       "git+%s.git#egg=ciur" % ciur.__git__
    ],
    author_email=ciur.__email__,
    author=ciur.__author__,
    description=ciur.__doc__,
    license="MIT",
    long_description=open("README.rst").read(),
    packages=[
        ciur.__title__
    ],
    install_requires=parse_requirements("requirements-pip.txt"),
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    classifiers=[
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        # "Programming Language :: Python :: 3",
    ],
    entry_points={
        "console_scripts": [
            "ciur = ciur.cli:main",            
        ]
    }
)
