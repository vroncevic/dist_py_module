# -*- coding: UTF-8 -*-
# dist_py_module.py
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
from os import getcwd

try:
    from pathlib import Path

    from setup.gen_setup import GenSetup
    from ats_utilities.cfg_base import CfgBase
    from ats_utilities.console_io.error import error_message
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.console_io.success import success_message
except ImportError as e:
    msg = "\n{0}\n{1}\n".format(__file__, e)
    sys.exit(msg)  # Force close python ATS ##################################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2018, Free software to use and distributed it.'
__credits__ = ['Vladimir Roncevic']
__license__ = 'GNU General Public License (GPL)'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class DistPyModule(CfgBase):
    """
        Define class DistPyModule with attribute(s) and method(s).
        Load a settings, create an interface and run operation(s).
        It defines:
            attribute:
                __slots__ - Setting class slots
                VERBOSE - Console text indicator for current process-phase
                __CONFIG - Configuration file path
                __OPS -  Tool options (list)
            method:
                __init__ - Initial constructor
                process - Process and generate module setup.py
    """

    __slots__ = ('VERBOSE', '__CONFIG', '__OPS')
    VERBOSE = 'DISTRIBUTE_PY_MODULE'
    __CONFIG = '/../conf/dist_py_module.cfg'
    __OPS = ['-g', '--gen', '-h', '--version', '--verbose']

    def __init__(self, verbose=False):
        """
            Loading configuration and setting argument options.
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
            :exceptions: None
        """
        verbose_message(DistPyModule.VERBOSE, verbose, 'Initial configuration')
        module_dir = Path(__file__).resolve().parent
        base_config_file = "{0}{1}".format(module_dir, DistPyModule.__CONFIG)
        CfgBase.__init__(self, base_config_file, verbose=verbose)
        if self.tool_status:
            self.add_new_option(
                DistPyModule.__OPS[0], DistPyModule.__OPS[1], dest='pkg',
                help='generate module setup.py'
            )

    def process(self, verbose=False):
        """
            Process and run operation.
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
            :return: True (success) | False
            :rtype: <bool>
            :exceptions: None
        """
        status = False
        if self.tool_status:
            num_of_args_sys = len(sys.argv)
            if num_of_args_sys > 1:
                option = sys.argv[1]
                if option not in DistPyModule.__OPS:
                    sys.argv = []
                    sys.argv.append('-h')
            else:
                sys.argv.append('-h')
            opts, args = self.parse_args(sys.argv)
            num_of_args, current_dir = len(args), getcwd()
            setup_path = "{0}/{1}".format(current_dir, 'setup.py')
            setup_exists = Path(setup_path).exists()
            if num_of_args == 1 and opts.pkg and not setup_exists:
                generator, gen_status = GenSetup(verbose=verbose), False
                message = "{0} {1} [{2}]".format(
                    "[{0}]".format(self.name),
                    'Generating setup.py for package', opts.pkg
                )
                print(message)
                gen_status = generator.gen_setup("{0}".format(opts.pkg))
                if gen_status:
                    success_message(self.name, 'Done\n')
                    status = True
                else:
                    error_message(self.name, 'Failed to generate setup.py')
            else:
                error_message(self.name, 'setup.py already exist !')
        else:
            error_message('dist_py_module', 'Tool is not operational')
        return True if status else False

