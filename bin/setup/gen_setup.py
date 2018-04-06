# -*- coding: UTF-8 -*-
# gen_setup.py
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

try:
    from read_template import ReadTemplate
    from write_template import WriteTemplate

    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.console_io.error import error_message
    from ats_utilities.console_io.success import success_message
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


class GenSetup(ReadTemplate, WriteTemplate):
    """
        Define class GenSetup with attribute(s) and method(s).
        Generate module file setup.py by template and parameters.
        It defines:
            attribute:
                VERBOSE - Verbose prefix text
            method:
                __init__ - Initial constructor
                gen_setup - Generate module file setup.py
    """

    VERBOSE = 'SETUP::GEN_SETUP'

    def __init__(self, verbose=False):
        """
            Initial constructor
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
        """
        cls = self.__class__
        verbose_message(cls.VERBOSE, verbose, 'Initial setup')
        ReadTemplate.__init__(self, verbose=verbose)
        WriteTemplate.__init__(self, verbose=verbose)

    def gen_setup(self, package_name, verbose=False):
        """
            Generate setup.py for python package.
            :param package_name: Parameter package name
            :type package_name: <str>
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
            :return: True (success) | False
            :rtype: <bool>
            :exceptions: ATSBadCallError | ATSTypeError
        """
        cls, func, status = self.__class__, stack()[0][3], False
        package_txt = 'Argument: expected package_name <str> object'
        package_msg = "{0} {1} {2}".format(cls.VERBOSE, func, package_txt)
        if package_name is None or not package_name:
            raise ATSBadCallError(package_msg)
        if not isinstance(package_name, str):
            raise ATSTypeError(package_msg)
        verbose_message(
            cls.VERBOSE, verbose, 'Generating package', package_name
        )
        setup_content = self.read(verbose=verbose)  # Load template
        if setup_content:
            # Generate setup.py
            status = self.write(setup_content, package_name, verbose=verbose)
            if not status:
                error_message(cls.VERBOSE, 'Failed to generate')
        return True if status else False
