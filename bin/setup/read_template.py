# -*- coding: UTF-8 -*-
# read_template.py
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

try:
    from pathlib import Path

    from ats_utilities.config.file_checking import FileChecking
    from ats_utilities.exceptions.ats_file_error import ATSFileError
    from ats_utilities.config.config_context_manager import ConfigFile
    from ats_utilities.console_io.verbose import verbose_message
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


class ReadTemplate(FileChecking):
    """
        Define class ReadTemplate with attribute(s) and method(s).
        Read a template file (setup.template) and return a content.
        It defines:
            attribute:
                __TEMPLATE - Template file path
                __FORMAT - File format for template
                VERBOSE - Console text indicator for current process-phase
                __template - Absolute template file path
            method:
                __init__ - Initial constructor
                read - Read a template and return a string representation
    """

    __TEMPLATE = '/../../conf/template/setup.template'
    __FORMAT = 'template'
    VERBOSE = 'SETUP::READ_TEMPLATE'

    def __init__(self, verbose=False):
        """
            Setting template file from configuration directory.
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
        """
        cls = self.__class__
        super(ReadTemplate, self).__init__(verbose=verbose)
        verbose_message(cls.VERBOSE, verbose, 'Initial template')
        module_dir = Path(__file__).resolve().parent
        template_file = "{0}{1}".format(module_dir, cls.__TEMPLATE)
        template_file_exists = self.check_file(
            file_path=template_file, verbose=verbose
        )
        if template_file_exists:
            self.__template = template_file
        else:
            self.__template = None

    def read(self, verbose=False):
        """
            Read template structure.
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
            :return: Template content for setup module | None
            :rtype: <str> or <NoneType>
        """
        cls, setup_content = self.__class__, None
        verbose_message(cls.VERBOSE, verbose, 'Loading template')
        try:
            with ConfigFile(self.__template, 'r', cls.__FORMAT) as template:
                setup_content = template.read()
        except AttributeError:
            pass
        return setup_content
