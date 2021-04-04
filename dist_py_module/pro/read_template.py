# -*- coding: UTF-8 -*-

'''
 Module
     read_template.py
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
     Defined class ReadTemplate with attribute(s) and method(s).
     Created API for read a template file and return a content.
'''

import sys
from os.path import isdir

try:
    from pathlib import Path
    from ats_utilities.checker import ATSChecker
    from ats_utilities.config_io.base_check import FileChecking
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.exceptions.ats_bad_call_error import ATSBadCallError
except ImportError as ats_error_message:
    MESSAGE = '\n{0}\n{1}\n'.format(__file__, ats_error_message)
    sys.exit(MESSAGE)  # Force close python ATS ##############################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2017, https://vroncevic.github.io/dist_py_module'
__credits__ = ['Vladimir Roncevic']
__license__ = 'https://github.com/vroncevic/dist_py_module/blob/master/LICENSE'
__version__ = '1.6.1'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class ReadTemplate(FileChecking):
    '''
        Defined class ReadTemplate with attribute(s) and method(s).
        Created API for read a template file and return a content.
        It defines:

            :attributes:
                | __slots__ - Setting class slots.
                | VERBOSE - Console text indicator for current process-phase.
                | __TEMPLATE_DIR - Template dir path.
                | __template_dir - Absolute file path of template dir.
            :methods:
                | __init__ - Initial constructor.
                | get_template_dir - Getter for template directory object.
                | read - Read a template and return a string representation.
                | __str__ - Dunder method for ReadTemplate.
    '''

    __slots__ = ('VERBOSE', '__TEMPLATE_DIR', '__template_dir')
    VERBOSE = 'DIST_PY_MODULE::PRO::READ_TEMPLATE'
    __TEMPLATE_DIR = '/../conf/template/'

    def __init__(self, verbose=False):
        '''
            Initial constructor.

            :param verbose: Enable/disable verbose option.
            :type verbose: <bool>
            :exceptions: None
        '''
        verbose_message(ReadTemplate.VERBOSE, verbose, 'init reader')
        FileChecking.__init__(self, verbose=verbose)
        current_dir = Path(__file__).parent
        template_dir = '{0}{1}'.format(
            current_dir, ReadTemplate.__TEMPLATE_DIR
        )
        check_template_dir = isdir(template_dir)
        if check_template_dir:
            self.__template_dir = template_dir
        else:
            self.__template_dir = None

    def get_template_dir(self):
        '''
            Getter for template directory.

            :return: Template directory object.
            :rtype: <str>
        '''
        return self.__template_dir

    def read(self, template_module, verbose=False):
        '''
            Read template structure.

            :param template_module: Template module name.
            :type template_module: <str>
            :param verbose: Enable/disable verbose option.
            :type verbose: <bool>
            :return: Template content for setup module | None.
            :rtype: <str> | <NoneType>
            :exceptions: None
        '''
        checker, error, status = ATSChecker(), None, False
        error, status = checker.check_params(
            [('str:template_module', template_module)]
        )
        if status == ATSChecker.TYPE_ERROR:
            raise ATSTypeError(error)
        if status == ATSChecker.VALUE_ERROR:
            raise ATSBadCallError(error)
        setup_content, template_file = None, None
        verbose_message(ReadTemplate.VERBOSE, verbose, 'load template')
        template_file = '{0}{1}'.format(self.__template_dir, template_module)
        self.check_path(file_path=template_file, verbose=verbose)
        if self.file_path_ok:
            with open(template_file, 'r') as tmpl:
                setup_content = tmpl.read()
        return setup_content

    def __str__(self):
        '''
            Dunder method for ReadTemplate.

            :return: Object in a human-readable format.
            :rtype: <str>
            :exceptions: None
        '''
        return '{0} ({1}, {2})'.format(
            self.__class__.__name__, FileChecking.__str__(self),
            self.__template_dir
        )
