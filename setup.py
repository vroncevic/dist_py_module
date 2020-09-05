#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
 Module
     setup.py
 Copyright
     Copyright (C) 2018 Vladimir Roncevic <elektron.ronca@gmail.com>
     dist_py_module is free software: you can redistribute it and/or modify it
     under the terms of the GNU General Public License as published by the
     Free Software Foundation, either version 3 of the License, or
     (at your option) any later version.
     dist_py_module is distributed in the hope that it will be useful, but
     WITHOUT ANY WARRANTY; without even the implied warranty of
     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
     See the GNU General Public License for more details.
     You should have received a copy of the GNU General Public License along
     with this program. If not, see <http://www.gnu.org/licenses/>.
 Info
     Define setup for dist_py_module package.
"""

from setuptools import setup

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2018, Free software to use and distributed it.'
__credits__ = ['Vladimir Roncevic']
__license__ = 'GNU General Public License (GPL)'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'

setup(
    name='dist_py_module',
    version='1.1.0',
    description='Python package for generation of setup file',
    author='Vladimir Roncevic',
    author_email='elektron.ronca@gmail.com',
    url='https://vroncevic.github.io/dist_py_module/',
    license='GPL 2018 Free software to use and distributed it.',
    long_description='Package dist_py_module for python App/Tool/Script.',
    keywords='setup, python, install',
    platforms='POSIX',
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: GPL',
        'Operating System :: OS Independent',
    ],
    packages=[
        'dist_py_module',
        'dist_py_module.setup',
    ],
    install_requires=['wheel', 'colorama', 'bs4', 'yaml', 'configparser', 'pathlib'],
    data_files=[
        ('/usr/bin/', ['dist_py_module/run/dist_py_module_run.py']),
        (
             '/usr/local/lib/python2.7/dist-packages/dist_py_module/conf/',
             ['dist_py_module/conf/dist_py_module.cfg']
        ),
        (
            '/usr/local/lib/python2.7/dist-packages/dist_py_module/conf/',
            ['dist_py_module/conf/dist_py_module_util.cfg']
        ),
        (
            '/usr/local/lib/python2.7/dist-packages/dist_py_module/conf/template/',
            ['dist_py_module/conf/template/setup.template']
        ),
        (
            '/usr/local/lib/python2.7/dist-packages/dist_py_module/log/',
            ['dist_py_module/log/dist_py_module.log']
        )
    ]
)