# -*- coding: UTF-8 -*-
# write_template.py
# Copyright (C) 2018 Vladimir Roncevic <elektron.ronca@gmail.com>
#
# dist_py_module is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# dist_py_module is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program. If not, see <http://www.gnu.org/licenses/>.
#

import sys
from inspect import stack
from os import getcwd, chmod
from string import Template

try:
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.config.config_context_manager import ConfigFile
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.exceptions.ats_bad_call_error import ATSBadCallError
except ImportError as e:
    msg = "\n{0}\n{1}\n".format(__file__, e)
    sys.exit(msg)  # Force close python ATS ###################################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2018, Free software to use and distributed it.'
__credits__ = ['Vladimir Roncevic']
__license__ = 'GNU General Public License (GPL)'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class WriteTemplate(object):
    """
        Define class WriteTemplate with attribute(s) and method(s).
        Write template content with parameters to a file setup.py.
        It defines:
            attribute:
                __SETUP_FILE - File name for setup file
                __FORMAT - File format (file extension)
                VERBOSE - Console text indicator for current process-phase
            method:
                __init__ - Initial constructor
                write - Write a template content to a file setup.py
    """

    __SETUP_FILE = 'setup.py'
    __FORMAT = 'py'
    VERBOSE = 'SETUP::WRITE_TEMPLATE'

    def __init__(self, verbose=False):
        """
            Initial constructor
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
        """
        cls = WriteTemplate
        verbose_message(cls.VERBOSE, verbose, 'Initial writer')
        pass

    def write(self, setup_content, package_name, verbose=False):
        """
            Write setup content to file.
            :param setup_content: Template content
            :type setup_content: <str>
            :param package_name: Parameter package name
            :type package_name: <str>
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
            :return: True (success) | False
            :rtype: <bool>
            :exception: ATSBadCallError | ATSTypeError
        """
        cls, status = WriteTemplate, False
        func, current_dir = stack()[0][3], getcwd()
        setup_txt = 'First argument: expected setup_content <str> object'
        setup_msg = "{0} {1} {2}".format('def', func, setup_txt)
        package_txt = 'First argument: expected package_name <str> object'
        package_msg = "{0} {1} {2}".format('def', func, package_txt)
        if setup_content is None or not setup_content:
            raise ATSBadCallError(setup_msg)
        if not isinstance(setup_content, str):
            raise ATSTypeError(setup_msg)
        if package_name is None or not package_name:
            raise ATSBadCallError(package_msg)
        if not isinstance(package_name, str):
            raise ATSTypeError(package_msg)
        setup = "{0}/{1}".format(current_dir, cls.__SETUP_FILE)
        verbose_message(cls.VERBOSE, verbose, 'Write setup file')
        package = {'pkg': "{0}".format(package_name)}
        template = Template(setup_content)
        try:
            with open(setup, 'w') as setup_file:
                setup_file.write(template.substitute(package))
                chmod(setup, 0o666)
                status = True
        except AttributeError:
            pass
        return True if status else False
