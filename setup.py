#!/usr/bin/env python
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

from RealEstateAnalysis import __version__ as version

def requireModules(moduleNames=None):
    import re
    if moduleNames is None:
        moduleNames = []
    else:
        moduleNames = moduleNames

    commentPattern = re.compile(r'^\w*?#')
    moduleNames.extend(
        filter(lambda line: not commentPattern.match(line), 
            open('requirements.txt').readlines()))

    return moduleNames

setup(
    name='RealEstateAnalysis',
    version=version,

    author='Chris Bremer',
    author_email='cbremer4@gmail.com',

    description='RealEstateAnalysis',
    long_description=open('README.txt').read(),
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers'
    ],

    install_requires=requireModules([

    ]),

    test_suite='RealEstateAnalysis.test'
)
