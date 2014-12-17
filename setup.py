#from __future__ import unicode_literals

import re

from setuptools import find_packages, setup

import sys
sys.path.append('src/')

def get_version(filename):
    content = open(filename).read()
    metadata = dict(re.findall("__([a-z]+)__ = '([^']+)'", content))
    return metadata['version']


setup(
    name='Rotary Encoder',
    version=get_version('src/rotencoder/__init__.py'),
    url='',
    license='Apache License, Version 2.0',
    author='Sven Klomp',
    author_email='mail@klomp.eu',
    description='Rotary Encoder which registers as generic input device',
    long_description=open('README.md').read(),
    packages=['rotencoder'],
    package_dir={'rotencoder': 'src/rotencoder'},
    scripts=['src/bin/rotary-encoder'],
    data_files=[('config', ['config/rotencoder.cfg'])],
    zip_safe=False,
    include_package_data=True,
    #install_requires=[
        #'setuptools',
        #'evdev',
        #'RPi',
    #]
)
