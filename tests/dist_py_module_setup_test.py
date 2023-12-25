# -*- coding: UTF-8 -*-

'''
Module
    dist_py_module_setup_test.py
Copyright
    Copyright (C) 2017 - 2024 Vladimir Roncevic <elektron.ronca@gmail.com>
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
    Defines class GenSetupTestCase with attribute(s) and method(s).
    Creates test cases for checking functionalities of GenSetup.
Execute
    python3 -m unittest -v dist_py_module_setup_test
'''

import sys
from typing import Any, List
from os.path import exists
from os import remove
from unittest import TestCase, main
from unittest.mock import patch

try:
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.exceptions.ats_value_error import ATSValueError
    from dist_py_module.pro import GenSetup
except ImportError as test_error_message:
    # Force close python test #################################################
    sys.exit(f'\n{__file__}\n{test_error_message}\n')

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2024, https://vroncevic.github.io/dist_py_module'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/dist_py_module/blob/dev/LICENSE'
__version__ = '3.0.3'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class GenSetupTestCase(TestCase):
    '''
        Defines class GenSetupTestCase with attribute(s) and method(s).
        Creates test cases for checking functionalities of GenSetup.
        GenSetup unit tests.

        It defines:

            :attributes:
                | None
            :methods:
                | setUp - Call before test case.
                | tearDown - Call after test case.
                | test_default_create - Default on create is not None.
                | test_get_reader - Is reader ok.
                | test_get_writer - Is writer ok.
                | test_gen_project_empty - Create project with missing name.
                | test_gen_project_none - Create project with None name.
                | test_gen_project - Create project.
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

    def test_default_create(self) -> None:
        '''Default on create is not None'''
        generator: GenSetup = GenSetup()
        self.assertIsNotNone(generator)

    def test_get_reader(self) -> None:
        '''Is reader ok'''
        generator: GenSetup = GenSetup()
        self.assertIsNotNone(generator.get_reader())

    def test_get_writer(self) -> None:
        '''Is writer ok'''
        generator: GenSetup = GenSetup()
        self.assertIsNotNone(generator.get_writer())

    def test_gen_project_empty(self) -> None:
        '''Create project with missing name'''
        generator: GenSetup = GenSetup()
        with self.assertRaises(ATSValueError):
            generator.gen_setup("")

    def test_gen_project_none(self) -> None:
        '''Create project with None name'''
        generator: GenSetup = GenSetup()
        with self.assertRaises(ATSTypeError):
            generator.gen_setup(None)

    @patch('builtins.input', return_value='1')
    def test_gen_project(self, mock_input: Any) -> None:
        '''Create project'''
        generator: GenSetup = GenSetup()
        self.assertTrue(generator.gen_setup('simple_project'))
        mock_input.assert_called_once_with(' select project type: ')


if __name__ == '__main__':
    main()
