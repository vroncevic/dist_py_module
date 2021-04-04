#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
 Module
     setup.py
 Copyright
     Copyright (C) 2017 Vladimir Roncevic <elektron.ronca@gmail.com>
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
     Defined setup for dist_py_module package.
"""

from sys import argv, version_info, prefix, exit
from os.path import abspath, dirname, join, exists
from site import getusersitepackages
from setuptools import setup

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2017, https://vroncevic.github.io/dist_py_module'
__credits__ = ['Vladimir Roncevic']
__license__ = 'https://github.com/vroncevic/dist_py_module/blob/master/LICENSE'
__version__ = '1.6.2'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'

def install_directory():
    '''
        Return the installation directory, or None.

        :return: Path (success) | None.
        :rtype: <str> | <NoneType>
        :exceptions: None
    '''
    py_version = '{0}.{1}'.format(version_info[0], version_info[1])
    if '--github' in argv:
        index = argv.index('--github')
        argv.pop(index)
        paths = (
            '{0}/lib/python{1}/dist-packages/'.format(prefix, py_version),
            '{0}/lib/python{1}/site-packages/'.format(prefix, py_version)
        )
    else:
        paths = (s for s in (
            '{0}/local/lib/python{1}/dist-packages/'.format(
                prefix, py_version
            ),
            '{0}/local/lib/python{1}/site-packages/'.format(
                prefix, py_version
            )
        ))
    for path in paths:
        print('[setup] check path {0}'.format(path))
        if exists(path):
            print('[setup] using path {0}'.format(path))
            return path
    print('[setup] no installation path found, check {0}\n'.format(prefix))
    return None

INSTALL_DIR = install_directory()

THIS_DIR, LONG_DESCRIPTION = abspath(dirname(__file__)), None
with open(join(THIS_DIR, 'README.md')) as readme:
    LONG_DESCRIPTION = readme.read()

PROGRAMMING_LANG = 'Programming Language :: Python ::'
VERSIONS = ['2.7', '3', '3.2', '3.3', '3.4']
SUPPORTED_PY_VERSIONS = [
    '{0} {1}'.format(PROGRAMMING_LANG, VERSION) for VERSION in VERSIONS
]

LICENSE_PREFIX = 'License :: OSI Approved ::'
LICENSES = [
    'GNU Lesser General Public License v2 (LGPLv2)',
    'GNU Lesser General Public License v2 or later (LGPLv2+)',
    'GNU Lesser General Public License v3 (LGPLv3)',
    'GNU Lesser General Public License v3 or later (LGPLv3+)',
    'GNU Library or Lesser General Public License (LGPL)'
]
APPROVED_LICENSES = [
    '{0} {1}'.format(LICENSE_PREFIX, LICENSE) for LICENSE in LICENSES
]

PYP_CLASSIFIERS = SUPPORTED_PY_VERSIONS + APPROVED_LICENSES

setup(
    name='dist_py_module',
    version='1.6.2',
    description='Python package for generation of setup file',
    author='Vladimir Roncevic',
    author_email='elektron.ronca@gmail.com',
    url='https://vroncevic.github.io/dist_py_module',
    license='https://github.com/vroncevic/dist_py_module/blob/master/LICENSE',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    keywords='setup, python, install',
    platforms='POSIX',
    classifiers=PYP_CLASSIFIERS,
    packages=['dist_py_module', 'dist_py_module.pro'],
    install_requires=['ats-utilities'],
    data_files=[
        ('/usr/local/bin/', ['dist_py_module/run/dist_py_module_run.py']),
        (
            '{0}{1}'.format(INSTALL_DIR, 'dist_py_module/conf/'),
            ['dist_py_module/conf/dist_py_module.cfg']
        ),
        (
            '{0}{1}'.format(INSTALL_DIR, 'dist_py_module/conf/'),
            ['dist_py_module/conf/dist_py_module_util.cfg']
        ),
        (
            '{0}{1}'.format(INSTALL_DIR, 'dist_py_module/conf/'),
            ['dist_py_module/conf/project.yaml']
        ),
        (
            '{0}{1}'.format(INSTALL_DIR, 'dist_py_module/conf/template/'),
            ['dist_py_module/conf/template/setup_package.template']
        ),
        (
            '{0}{1}'.format(INSTALL_DIR, 'dist_py_module/conf/template/'),
            ['dist_py_module/conf/template/setup_tool.template']
        ),
        (
            '{0}{1}'.format(INSTALL_DIR, 'dist_py_module/log/'),
            ['dist_py_module/log/dist_py_module.log']
        )
    ]
)
