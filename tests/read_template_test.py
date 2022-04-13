# -*- coding: UTF-8 -*-

'''
 Module
     read_template_test.py
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
     Defined class ReadTemplateTestCase with attribute(s) and method(s).
     Created test cases for checking functionalities of ReadTemplate.
 Execute
     python3 -m unittest -v read_template_test
'''

import sys
import unittest

try:
    from dist_py_module.pro.read_template import ReadTemplate
except ImportError as test_error_message:
    MESSAGE = '\n{0}\n{1}\n'.format(__file__, test_error_message)
    sys.exit(MESSAGE)  # Force close python test ############################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2022, https://vroncevic.github.io/dist_py_module'
__credits__ = ['Vladimir Roncevic']
__license__ = 'https://github.com/vroncevic/dist_py_module/blob/dev/LICENSE'
__version__ = '2.5.8'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class ReadTemplateTestCase(unittest.TestCase):
    '''
        Defined class ReadTemplateTestCase with attribute(s) and method(s).
        Created test cases for checking functionalities of ReadTemplate.
        It defines:

            :attributes:
                | template_reader - Template read object.
            :methods:
                | setUp - call before test cases.
                | tearDown - call after test cases.
                | test_template_dir - test template dir check.
                | test_setup_package - test setup package check.
                | test_setup_tool - test setup tool check.
    '''

    def setUp(self):
        '''Call before test cases.'''
        self.template_reader = ReadTemplate()

    def tearDown(self):
        '''Call after test cases.'''
        self.template_reader = None

    def test_template_dir(self):
        '''Test template dir check.'''
        self.assertIsNot(self.template_reader.get_template_dir(), None)

    def test_setup_package(self):
        '''Test setup package check.'''
        self.assertIsNot(
            self.template_reader.read('setup_package.template'), None
        )

    def test_setup_tool(self):
        '''Test setup tool check.'''
        self.assertIsNot(
            self.template_reader.read('setup_tool.template'), None
        )


if __name__ == '__main__':
    unittest.main()
