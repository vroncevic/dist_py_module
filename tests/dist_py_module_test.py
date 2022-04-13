# -*- coding: UTF-8 -*-

'''
 Module
     dist_py_module_test.py
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
     Defined class DistPyModuleTestCase with attribute(s) and method(s).
     Created test cases for checking functionalities of DistPyModule.
 Execute
     python3 -m unittest -v dist_py_module_test
'''

import sys
import unittest

try:
    from dist_py_module.pro import GenSetup
except ImportError as test_error_message:
    MESSAGE = '\n{0}\n{1}\n'.format(__file__, test_error_message)
    sys.exit(MESSAGE)  # Force close python test ############################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2021, https://vroncevic.github.io/dist_py_module'
__credits__ = ['Vladimir Roncevic']
__license__ = 'https://github.com/vroncevic/dist_py_module/blob/dev/LICENSE'
__version__ = '2.5.8'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class DistPyModuleTestCase(unittest.TestCase):
    '''
        Defined class DistPyModuleTestCase with attribute(s) and method(s).
        Created test cases for checking functionalities of DistPyModule.
        It defines:

            :attributes:
                | tool_generator - tool generator object.
            :methods:
                | setUp - call before test cases.
                | tearDown - call after test cases.
                | test_reader_not_none - test for check reader.
                | test_writer_not_none - test for check writer.
                | test_process - test for base process.
    '''

    def setUp(self):
        '''Call before test cases.'''
        self.verbose = False
        self.tool_generator = GenSetup(self.verbose)

    def tearDown(self):
        '''Call after test cases.'''
        self.tool_generator = None

    def test_reader_not_none(self):
        '''Test is reader setup done.'''
        self.assertIsNot(self.tool_generator.get_reader(), None)

    def test_writer_not_none(self):
        '''Test is writer setup done.'''
        self.assertIsNot(self.tool_generator.get_writer(), None)

    def test_process(self):
        '''Test base process.'''
        status = self.tool_generator.gen_setup(
            '{0}'.format('simple_test'), self.verbose
        )
        self.assertEqual(status, True)


if __name__ == '__main__':
    unittest.main()
