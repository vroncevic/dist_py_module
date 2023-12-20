# -*- coding: UTF-8 -*-

'''
Module
    write_template_test.py
Copyright
    Copyright (C) 2022-2024 Vladimir Roncevic <elektron.ronca@gmail.com>
    gen_stm8 is free software: you can redistribute it and/or modify it
    under the terms of the GNU General Public License as published by the
    Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    gen_stm8 is distributed in the hope that it will be useful, but
    WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
    See the GNU General Public License for more details.
    You should have received a copy of the GNU General Public License along
    with this program. If not, see <http://www.gnu.org/licenses/>.
Info
    Defines class WriteTemplateTestCase with attribute(s) and method(s).
    Creates test cases for checking functionalities of WriteTemplate.
Execute
    python3 -m unittest -v write_template_test
'''

import sys
from os.path import exists
from os import remove
from typing import Any, List, Dict
from unittest import TestCase, main

try:
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.exceptions.ats_value_error import ATSValueError
    from dist_py_module.pro.read_template import ReadTemplate
    from dist_py_module.pro.write_template import WriteTemplate
except ImportError as test_error_message:
    # Force close python test #################################################
    sys.exit(f'\n{__file__}\n{test_error_message}\n')

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2024, https://vroncevic.github.io/gen_stm8'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_stm8/blob/dev/LICENSE'
__version__ = '3.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class WriteTemplateTestCase(TestCase):
    '''
        Defines class WriteTemplateTestCase with attribute(s) and method(s).
        Creates test cases for checking functionalities of WriteTemplate.
        WriteTemplate unit tests.

        It defines:

            :attributes:
                | None
            :methods:
                | setUp - call before test case.
                | tearDown - call after test case.
                | test_write_template_create - Test write templates create.
                | test_write_template_empty - Test write templates empty.
                | test_write_template_none - Test write templates None.
                | test_write_template - Test write templates.
                | test_write_missing_modules - Test missing modules.
                | test_write_empty_pkg_name - Test empty pkg name.
    '''

    def setUp(self) -> None:
        '''Call before test case.'''

    def tearDown(self) -> None:
        '''Call after test case.'''
        if exists('MANIFEST.in'):
            remove('MANIFEST.in')
        if exists('pyproject.toml'):
            remove('pyproject.toml')
        if exists('setup.cfg'):
            remove('setup.cfg')
        if exists('setup.py'):
            remove('setup.py')

    def test_write_template_create(self) -> None:
        '''Test write templates create'''
        template = WriteTemplate()
        self.assertIsNotNone(template)

    def test_write_template_empty(self) -> None:
        '''Test write templates empty'''
        template = WriteTemplate()
        content: Dict[Any, Any] = {}
        templates: List[str] = []
        with self.assertRaises(ATSValueError):
            self.assertFalse(
                template.write(content, 'simple_project', templates)
            )

    def test_write_template_none(self) -> None:
        '''Test write templates None'''
        template = WriteTemplate()
        templates: List[str] = []
        with self.assertRaises(ATSTypeError):
            self.assertFalse(
                template.write(
                    None, 'simple_project', templates  # type: ignore
                )
            )

    def test_write_template(self) -> None:
        '''Test write templates'''
        template_read = ReadTemplate()
        template_write = WriteTemplate()
        templates: List[str] | None = [
            'setup_package.template',
            'MANIFEST.template',
            'pyproject.template',
            'setup.template'
        ]
        modules: List[str] | None = [
            'setup.py',
            'MANIFEST.in',
            'pyproject.toml',
            'setup.cfg'
        ]
        content: Dict[Any, Any] = template_read.read(templates)
        self.assertTrue(
            template_write.write(content, 'simple_project', modules)
        )

    def test_write_missing_modules(self) -> None:
        '''Test missing templates'''
        template_read = ReadTemplate()
        template_write = WriteTemplate()
        templates: List[str] | None = [
            'setup_package.template',
            'MANIFEST.template',
            'pyproject.template',
            'setup.template'
        ]
        modules: List[str] = []
        content: Dict[Any, Any] = template_read.read(templates)
        with self.assertRaises(ATSValueError):
            self.assertTrue(
                template_write.write(content, 'simple_project', modules)
            )

    def test_write_empty_pkg_name(self) -> None:
        '''Test empty pkg name'''
        template_read = ReadTemplate()
        template_write = WriteTemplate()
        templates: List[str] | None = [
            'setup_package.template',
            'MANIFEST.template',
            'pyproject.template',
            'setup.template'
        ]
        modules: List[str] | None = [
            'setup.py',
            'MANIFEST.in',
            'pyproject.toml',
            'setup.cfg'
        ]
        content: Dict[Any, Any] = template_read.read(templates)
        with self.assertRaises(ATSValueError):
            self.assertTrue(
                template_write.write(content, '', modules)
            )


if __name__ == '__main__':
    main()
