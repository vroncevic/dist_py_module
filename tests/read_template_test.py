# -*- coding: UTF-8 -*-

'''
Module
    read_template_test.py
Copyright
    Copyright (C) 2017 - 2026 Vladimir Roncevic <elektron.ronca@gmail.com>
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
    Defines class ReadTemplateTestCase with attribute(s) and method(s).
    Creates test cases for checking functionalities of ReadTemplate.
Execute
    python3 -m unittest -v read_template_test
'''

import sys
from typing import List
from unittest import TestCase, main

try:
    from ats_utilities.exceptions.ats_value_error import ATSValueError
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from dist_py_module.pro.read_template import ReadTemplate
except ImportError as test_error_message:
    # Force close python test #################################################
    sys.exit(f'\n{__file__}\n{test_error_message}\n')

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/dist_py_module'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/dist_py_module/blob/dev/LICENSE'
__version__: str = '3.0.9'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'


class ReadTemplateTestCase(TestCase):
    '''
        Defines class ReadTemplateTestCase with attribute(s) and method(s).
        Creates test cases for checking functionalities of ReadTemplate.
        ReadTemplate unit tests.

        It defines:

            :attributes:
                | None
            :methods:
                | setUp - Call before test case.
                | tearDown - Call after test case.
                | test_read_template_create - Test read templates create.
                | test_read_template_empty - Test read templates empty.
                | test_read_template_none - Test read templates None.
                | test_read_template - Test read templates.
    '''

    def setUp(self) -> None:
        '''Call before test case.'''

    def tearDown(self) -> None:
        '''Call after test case.'''

    def test_read_template_create(self) -> None:
        '''Test read templates create'''
        template = ReadTemplate()
        self.assertIsNotNone(template)

    def test_read_template_empty(self) -> None:
        '''Test read templates empty'''
        template = ReadTemplate()
        template_file: List[str] | None = []
        with self.assertRaises(ATSValueError):
            self.assertFalse(
                template.read(template_file)
            )

    def test_read_template_none(self) -> None:
        '''Test read templates None'''
        template = ReadTemplate()
        with self.assertRaises(ATSTypeError):
            self.assertFalse(
                template.read(None)  # type: ignore
            )

    def test_read_template(self) -> None:
        '''Test read templates'''
        template = ReadTemplate()
        template_files: List[str] | None = [
            'setup_package.template',
            'MANIFEST.template',
            'pyproject.template',
            'setup.template'
        ]
        self.assertTrue(bool(template.read(template_files)))


if __name__ == '__main__':
    main()
