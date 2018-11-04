#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from distutils.core import setup

setup(
    name = 'zebitex',
    version = '0.0.1',
    author = 'Dominique Bleus',
    author_email = 'github@clonix.info',
    maintainer = 'Dominique Bleus',
    maintainer_email = 'github@clonix.info',
    packages = ['zebitex'],
    description = 'Python3 wrapper for zebitex API V1, currently in beta version.',
    long_description = open('README.md','r').read(),    
    keywords = ['zebitex', 'exchange', 'cryptocurrency', 'API', 'wrapper'],
    license = 'BSD 3-Clause License',
    url = 'https://github.com/domble42/zebitex-python3/',
    download_url = 'https://github.com/domble42/zebitex-python3/archive/master.zip'
)
