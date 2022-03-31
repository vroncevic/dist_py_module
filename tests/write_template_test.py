# -*- coding: UTF-8 -*-

'''
 Module
     write_template_test.py
 Copyright
     Copyright (C) 2022 Vladimir Roncevic <elektron.ronca@gmail.com>
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
     Defined class WriteTemplateTestCase with attribute(s) and method(s).
     Created test cases for checking functionalities of WriteTemplate.
 Execute
     python3 -m unittest -v write_template_test
'''

import sys
import unittest

try:
    from dist_py_module.pro.write_template import WriteTemplate
except ImportError as test_error_message:
    MESSAGE = '\n{0}\n{1}\n'.format(__file__, test_error_message)
    sys.exit(MESSAGE)  # Force close python test ############################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2022, https://vroncevic.github.io/dist_py_module'
__credits__ = ['Vladimir Roncevic']
__license__ = 'https://github.com/vroncevic/dist_py_module/blob/dev/LICENSE'
__version__ = '2.4.8'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class WriteTemplateTestCase(unittest.TestCase):
    '''
        Defined class WriteTemplateTestCase with attribute(s) and method(s).
        Created test cases for checking functionalities of WriteTemplate.
        It defines:

            :attributes:
                | SETUP_CONTENT_PACKAGE - Package template.
                | SETUP_CONTENT_TOOL - Tool template.
                | template_writer - Template write object.
            :methods:
                | setUp - call before test cases.
                | tearDown - call after test cases.
                | test_write_template_package - test for check writer.
                | test_write_template_tool - test for base process.
    '''

    SETUP_CONTENT_PACKAGE = '''#!/usr/bin/env python
# -*- coding: UTF-8 -*-

\'\'\'
 Module
     setup.py
 Copyright
     Copyright (C) 2022 Vladimir Roncevic <elektron.ronca@gmail.com>
     $pkg is free software: you can redistribute it and/or modify it
     under the terms of the GNU General Public License as published by the
     Free Software Foundation, either version 3 of the License, or
     (at your option) any later version.
     $pkg is distributed in the hope that it will be useful, but
     WITHOUT ANY WARRANTY; without even the implied warranty of
     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
     See the GNU General Public License for more details.
     You should have received a copy of the GNU General Public License along
     with this program. If not, see <http://www.gnu.org/licenses/>.
 Info
     Define setup for $pkg package.
\'\'\'

from os.path import abspath, dirname, join
from setuptools import setup

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2022, Free software to use and distributed it.'
__credits__ = ['Vladimir Roncevic']
__license__ = 'GNU General Public License (GPL)'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'

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
    name='$pkg',
    version='1.0.0',
    description='Python module $pkg',
    author='Vladimir Roncevic',
    author_email='elektron.ronca@gmail.com',
    url='https://github.com/vroncevic/TODO',
    license='GPL 2022 Free software to use and distributed it.',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    keywords='$pkg, TODO',
    platforms='POSIX',
    classifiers=PYP_CLASSIFIERS,
    packages=['$pkg'],
    install_requires=['ats-utilities']
)
'''

    SETUP_CONTENT_TOOL = '''#!/usr/bin/env python
# -*- coding: UTF-8 -*-

\'\'\'
 Module
     setup.py
 Copyright
     Copyright (C) 2022 Vladimir Roncevic <elektron.ronca@gmail.com>
     $pkg is free software: you can redistribute it and/or modify it
     under the terms of the GNU General Public License as published by the
     Free Software Foundation, either version 3 of the License, or
     (at your option) any later version.
     $pkg is distributed in the hope that it will be useful, but
     WITHOUT ANY WARRANTY; without even the implied warranty of
     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
     See the GNU General Public License for more details.
     You should have received a copy of the GNU General Public License along
     with this program. If not, see <http://www.gnu.org/licenses/>.
 Info
     Defined setup for tool $pkg.
\'\'\'

from __future__ import print_function
import sys
from os.path import abspath, dirname, join, exists
from setuptools import setup

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2022, Free software to use and distributed it.'
__credits__ = ['Vladimir Roncevic']
__license__ = 'GNU General Public License (GPL)'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'

def install_directory():
    \'\'\'
        Return the installation directory, or None.

        :return: Path (success) | None.
        :rtype: <str> | <NoneType>
        :exceptions: None
    \'\'\'
    py_version = '{0}.{1}'.format(sys.version_info[0], sys.version_info[1])
    if '--github' in sys.argv:
        index = sys.argv.index('--github')
        sys.argv.pop(index)
        paths = (
            '{0}/lib/python{1}/dist-packages/'.format(sys.prefix, py_version),
            '{0}/lib/python{1}/site-packages/'.format(sys.prefix, py_version)
        )
    else:
        paths = (s for s in (
            '{0}/local/lib/python{1}/dist-packages/'.format(
                sys.prefix, py_version
            ),
            '{0}/local/lib/python{1}/site-packages/'.format(
                sys.prefix, py_version
            )
        ))
    message = None
    for path in paths:
        message = '[setup] check path {0}'.format(path)
        print(message)
        if exists(path):
            message = '[setup] use path {0}'.format(path)
            print(message)
            return path
    message = '[setup] no installation path found, check {0}\\n'.format(
        sys.prefix
    )
    print(message)
    return None

INSTALL_DIR = install_directory()
TOOL_DIR = '${pkg}/'
if not bool(INSTALL_DIR):
    print('[setup] force exit from install process')
    sys.exit(127)
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
    name='$pkg',
    version='1.0.0',
    description='Python module $pkg',
    author='Vladimir Roncevic',
    author_email='elektron.ronca@gmail.com',
    url='https://github.com/vroncevic/TODO',
    license='GPL 2022 Free software to use and distributed it.',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    keywords='$pkg, TODO',
    platforms='POSIX',
    classifiers=PYP_CLASSIFIERS,
    packages=['$pkg'],
    install_requires=['ats-utilities'],
    data_package = {
        '$pkg': [
            'conf/${pkg}.cfg',
            'conf/${pkg}_util.cfg',
            'conf/project.yaml',
            'conf/template/project.template',
            'log/$pkg.log',
        ]
    },
    data_files=[(
        '/usr/local/bin/', [
            '{0}{1}'.format(TOOL_DIR, 'run/${pkg}_run.py')
        ]
    )]
)
'''

    def setUp(self):
        '''Call before test cases.'''
        self.template_writer = WriteTemplate()

    def tearDown(self):
        '''Call after test cases.'''
        self.template_writer = None

    def test_write_template_package(self):
        '''Test write template package check.'''
        self.assertIsNot(
            self.template_writer.write(
                WriteTemplateTestCase.SETUP_CONTENT_PACKAGE,
                '{0}'.format('simple_test'),
                'setup_package.py'
            ), False
        )

    def test_write_template_tool(self):
        '''Test write template tool check.'''
        self.assertIsNot(
            self.template_writer.write(
                WriteTemplateTestCase.SETUP_CONTENT_TOOL,
                '{0}'.format('simple_test'),
                'setup_tool.py'
            ), False
        )

if __name__ == '__main__':
    unittest.main()
