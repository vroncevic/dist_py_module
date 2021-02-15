# -*- coding: UTF-8 -*-

"""
 Module
     read_template.py
 Copyright
     Copyright (C) 2018 Vladimir Roncevic <elektron.ronca@gmail.com>
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
     Define class ReadTemplate with attribute(s) and method(s).
     Read a template file (setup.template) and return a content.
"""

import sys
from os.path import isdir

try:
    from pathlib import Path
    from ats_utilities.config_io.base_check import FileChecking
    from ats_utilities.console_io.verbose import verbose_message
except ImportError as error_message:
    MESSAGE = "\n{0}\n{1}\n".format(__file__, error_message)
    sys.exit(MESSAGE)  # Force close python ATS ##############################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2018, Free software to use and distributed it.'
__credits__ = ['Vladimir Roncevic']
__license__ = 'GNU General Public License (GPL)'
__version__ = '1.2.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class ReadTemplate(FileChecking):
    """
        Define class ReadTemplate with attribute(s) and method(s).
        Read a template file (setup.template) and return a content.
        It defines:

            :attributes:
                | __slots__ - Setting class slots.
                | VERBOSE - Console text indicator for current process-phase.
                | __TEMPLATE_DIR - Template dir path.
                | __TEMPLATES - Types of templates.
                | __FORMAT - File format for template.
                | __template_dir - Absolute file path of template dir.
            :methods:
                | __init__ - Initial constructor.
                | get_tempalte_dir - Getter for template directory object.
                | read - Read a template and return a string representation.
    """

    __slots__ = (
        'VERBOSE', '__TEMPLATE_DIR', '__TEMPLATES',
        '__FORMAT', '__template_dir'
    )
    VERBOSE = 'DIST_PY_MODULE::SETUP::READ_TEMPLATE'
    __TEMPLATE_DIR = '/../conf/template/'
    __TEMPLATES = {1:'setup.template'}
    __FORMAT = 'template'

    def __init__(self, verbose=False):
        """
            Initial constructor.

            :param verbose: Enable/disable verbose option.
            :type verbose: <bool>
            :exceptions: None
        """
        verbose_message(
            ReadTemplate.VERBOSE, verbose, 'Initial reader'
        )
        FileChecking.__init__(self, verbose=verbose)
        current_dir = Path(__file__).parent
        template_dir = "{0}{1}".format(
            current_dir, ReadTemplate.__TEMPLATE_DIR
        )
        check_template_dir = isdir(template_dir)
        if check_template_dir:
            self.__template_dir = template_dir
        else:
            self.__template_dir = None

    def get_tempalte_dir(self):
        """
            Getter for template directory.

            :return: Template directory object.
            :rtype: <str>
        """
        return self.__template_dir

    def read(self, verbose=False):
        """
            Read template structure.

            :param verbose: Enable/disable verbose option.
            :type verbose: <bool>
            :return: Template content for setup module | None.
            :rtype: <str> | <NoneType>
            :exceptions: None
        """
        setup_content, template_file = None, None
        verbose_message(ReadTemplate.VERBOSE, verbose, 'Loading template')
        template_file = "{0}{1}".format(
            self.__template_dir, ReadTemplate.__TEMPLATES[1]
        )
        self.check_path(file_path=template_file, verbose=verbose)
        if self.file_path_ok:
            with open(template_file, 'r') as tmpl:
                setup_content = tmpl.read()
        return setup_content
