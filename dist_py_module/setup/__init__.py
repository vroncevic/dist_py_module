# -*- coding: UTF-8 -*-

"""
 Module
     __init__.py
 Copyright
     Copyright (C) 2021 Vladimir Roncevic <elektron.ronca@gmail.com>
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
     Define class GenSetup with attribute(s) and method(s).
     Generate module file setup.py by template and parameters.
"""

import sys

try:
    from pathlib import Path
    from ats_utilities.checker import ATSChecker
    from ats_utilities.config_io.base_check import FileChecking
    from dist_py_module.setup.read_template import ReadTemplate
    from ats_utilities.console_io.verbose import verbose_message
    from dist_py_module.setup.write_template import WriteTemplate
    from ats_utilities.config_io.yaml.yaml2object import Yaml2Object
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.exceptions.ats_bad_call_error import ATSBadCallError
except ImportError as error_message:
    MESSAGE = "\n{0}\n{1}\n".format(__file__, error_message)
    sys.exit(MESSAGE)  # Force close python ATS ##############################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2021, Free software to use and distributed it.'
__credits__ = ['Vladimir Roncevic']
__license__ = 'GNU General Public License (GPL)'
__version__ = '1.5.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class GenSetup(FileChecking):
    """
        Define class GenSetup with attribute(s) and method(s).
        Generate module file setup.py by template and parameters.
        It defines:

            :attributes:
                | __slots__ - Setting class slots.
                | VERBOSE - Console text indicator for current process-phase.
                | __PRO_STRUCTURE - Project setup (template, module).
                | __reader - Reader API.
                | __writer - Writer API.
                | __config - Project setup in dict format.
            :methods:
                | __init__ - Initial constructor.
                | get_reader - Getter for template reader.
                | get_writer - Getter for template writer.
                | gen_setup - Generate module file setup.py.
    """

    __slots__ = (
        'VERBOSE', '__PRO_STRUCTURE', '__reader', '__writer', '__config'
    )
    VERBOSE = 'DIST_PY_MODULE::SETUP::GEN_SETUP'
    __PRO_STRUCTURE = '/../conf/project.yaml'

    def __init__(self, verbose=False):
        """
            Initial constructor.

            :param verbose: Enable/disable verbose option.
            :type verbose: <bool>
            :exceptions: None
        """
        FileChecking.__init__(self, verbose=verbose)
        verbose_message(GenSetup.VERBOSE, verbose, 'init setup')
        self.__reader = ReadTemplate(verbose=verbose)
        self.__writer = WriteTemplate(verbose=verbose)
        project = "{0}/{1}".format(
            Path(__file__).parent, GenSetup.__PRO_STRUCTURE
        )
        self.check_path(file_path=project, verbose=verbose)
        self.check_mode(file_mode='r', verbose=verbose)
        self.check_format(
            file_path=project, file_format='yaml', verbose=verbose
        )
        if self.is_file_ok():
            yml2obj = Yaml2Object(project)
            self.__config = yml2obj.read_configuration()
        else:
            self.__config = None

    def get_reader(self):
        """
            Getter for template reader.

            :return: Template reader object.
            :rtype: <ReadTemplate>
            :exceptions: None
        """
        return self.__reader

    def get_writer(self):
        """
            Getter for template writer.

            :return: Template writer object.
            :rtype: <WriteTemplate>
            :exceptions: None
        """
        return self.__writer

    def gen_setup(self, package_name, verbose=False):
        """
            Generate setup.py for python package.

            :param package_name: Parameter package name.
            :type package_name: <str>
            :param verbose: Enable/disable verbose option.
            :type verbose: <bool>
            :return: True (success) | False.
            :rtype: <bool>
            :exceptions: ATSTypeError | ATSBadCallError
        """
        checker, error, status = ATSChecker(), None, False
        error, status = checker.check_params(
            [('str:package_name', package_name)]
        )
        if status == ATSChecker.TYPE_ERROR: raise ATSTypeError(error)
        if status == ATSChecker.VALUE_ERROR: raise ATSBadCallError(error)
        status, setup_content = False, None
        verbose_message(
            GenSetup.VERBOSE, verbose, 'generating package', package_name
        )
        setup_content = self.__reader.read(
            self.__config['template'], verbose=verbose
        )
        if setup_content:
            status = self.__writer.write(
                setup_content, package_name, verbose=verbose
            )
        return True if status else False
