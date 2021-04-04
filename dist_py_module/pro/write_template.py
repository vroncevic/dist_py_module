# -*- coding: UTF-8 -*-

'''
 Module
     write_template.py
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
     Defined class WriteTemplate with attribute(s) and method(s).
     Created API for write operation of template content.
'''

import sys
from os import getcwd, chmod
from string import Template

try:
    from ats_utilities.checker import ATSChecker
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


class WriteTemplate(object):
    '''
        Defined class WriteTemplate with attribute(s) and method(s).
        Created API for write operation of template content.
        It defines:

            :attributes:
                | __slots__ - Setting class slots.
                | VERBOSE - Console text indicator for current process-phase.
                | __setup - Setup file path.
            :methods:
                | __init__ - Initial constructor.
                | get_setup - Getter for setup file object.
                | write - Write a template content to a file setup.py.
                | __str__ - Dunder method for WriteTemplate.
    '''

    __slots__ = ('VERBOSE', '__setup')
    VERBOSE = 'DIST_PY_MODULE::PRO::WRITE_TEMPLATE'

    def __init__(self, verbose=False):
        '''
            Initial constructor.

            :param verbose: Enable/disable verbose option.
            :type verbose: <bool>
            :exceptions: None
        '''
        verbose_message(WriteTemplate.VERBOSE, verbose, 'init writer')
        self.__setup = None

    def get_setup(self):
        '''
            Getter for setup file object.

            :return: Setup file path | None.
            :rtype: <str> | <NoneType>
        '''
        return self.__setup

    def write(self, setup_content, package_name, module, verbose=False):
        '''
            Write setup content to file.

            :param setup_content: Template content.
            :type setup_content: <str>
            :param package_name: Parameter package name.
            :type package_name: <str>
            :param module: Module name.
            :type module: <str>
            :param verbose: Enable/disable verbose option.
            :type verbose: <bool>
            :return: True (success) | False.
            :rtype: <bool>
            :exception: ATSTypeError | ATSBadCallError
        '''
        checker, error, status = ATSChecker(), None, False
        error, status = checker.check_params([
            ('str:setup_content', setup_content),
            ('str:package_name', package_name),
            ('str:module', module)
        ])
        if status == ATSChecker.TYPE_ERROR:
            raise ATSTypeError(error)
        if status == ATSChecker.VALUE_ERROR:
            raise ATSBadCallError(error)
        status, template, current_dir = False, None, getcwd()
        self.__setup = '{0}/{1}'.format(current_dir, module)
        verbose_message(WriteTemplate.VERBOSE, verbose, 'write setup.py')
        package = {'pkg': '{0}'.format(package_name)}
        template = Template(setup_content)
        if template:
            with open(self.__setup, 'w') as setup_file:
                setup_file.write(template.substitute(package))
                chmod(self.__setup, 0o666)
                status = True
        return True if status else False

    def __str__(self):
        '''
            Dunder method for WriteTemplate.

            :return: Object in a human-readable format.
            :rtype: <str>
            :exceptions: None
        '''
        return '{0} ({1})'.format(self.__class__.__name__, self.__setup)
