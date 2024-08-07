# -*- coding: UTF-8 -*-

'''
Module
    dist_py_module_test.py
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
    Defines class DistPyModuleTestCase with attribute(s) and method(s).
    Creates test cases for checking functionalities of DistPyModule.
Execute
    python3 -m unittest -v dist_py_module_test
'''

import sys
from typing import Any, List
from os.path import exists
from os import remove
from unittest import TestCase, main
from unittest.mock import patch

try:
    from dist_py_module import DistPyModule
except ImportError as test_error_message:
    # Force close python test #################################################
    sys.exit(f'\n{__file__}\n{test_error_message}\n')

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2024, https://vroncevic.github.io/dist_py_module'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/dist_py_module/blob/dev/LICENSE'
__version__ = '3.0.7'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class DistPyModuleTestCase(TestCase):
    '''
        Defines class DistPyModuleTestCase with attribute(s) and method(s).
        Creates test cases for checking functionalities of DistPyModule.
        DistPyModule unit tests.

        It defines:

            :attributes:
                | None
            :methods:
                | setUp - Call before test case.
                | tearDown - Call after test case.
                | test_default_create - Default on create (not None).
                | test_missing_args - Test missing args.
                | test_wrong_arg - Test wrong arg.
                | test_process - Generate project structure.
                | test_cancel_process - Test cancel process.
                | test_package_process - Test package process.
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
        '''Default on create (not None)'''
        generator: DistPyModule = DistPyModule()
        self.assertIsNotNone(generator)

    def test_missing_args(self) -> None:
        '''Test missing args'''
        sys.argv.clear()
        generator: DistPyModule = DistPyModule()
        self.assertFalse(generator.process())

    def test_wrong_arg(self) -> None:
        '''Test wrong arg'''
        sys.argv.clear()
        sys.argv.insert(2, '-d')
        sys.argv.insert(3, 'simple_project')
        generator: DistPyModule = DistPyModule()
        self.assertFalse(generator.process())

    @patch('builtins.input', return_value='1')
    def test_process(self, mock_input: Any) -> None:
        '''Generate project structure'''
        sys.argv.clear()
        sys.argv.insert(0, '-n')
        sys.argv.insert(1, 'simple_project')
        generator: DistPyModule = DistPyModule()
        self.assertTrue(generator.process())
        mock_input.assert_called_once_with(' select project type: ')

    @patch('builtins.input', return_value='3')
    def test_cancel_process(self, mock_input: Any) -> None:
        '''Test cancel process'''
        sys.argv.clear()
        sys.argv.insert(0, '-n')
        sys.argv.insert(1, 'simple_project')
        generator: DistPyModule = DistPyModule()
        self.assertTrue(generator.process())
        mock_input.assert_called_once_with(' select project type: ')

    @patch('builtins.input', return_value='2')
    def test_package_process(self, mock_input: Any) -> None:
        '''Test package process'''
        sys.argv.clear()
        sys.argv.insert(0, '-n')
        sys.argv.insert(1, 'simple_project')
        generator: DistPyModule = DistPyModule()
        self.assertTrue(generator.process())
        mock_input.assert_called_once_with(' select project type: ')


if __name__ == '__main__':
    main()
