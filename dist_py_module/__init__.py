# -*- coding: UTF-8 -*-

'''
Module
    __init__.py
Copyright
    Copyright (C) 2017 - 2024 Vladimir Roncevic <elektron.ronca@gmail.com>
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
    Defines class DistPyModule with attribute(s) and method(s).
    Loads a base info, creates an CLI interface and runs operations.
'''

import sys
from typing import Any, List, Dict
from os.path import dirname, realpath
from argparse import Namespace

try:
    from ats_utilities.splash import Splash
    from ats_utilities.logging import ATSLogger
    from ats_utilities.cli.cfg_cli import CfgCLI
    from ats_utilities.console_io.error import error_message
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.console_io.success import success_message
    from dist_py_module.pro import GenSetup
except ImportError as ats_error_message:
    # Force close python ATS ##################################################
    sys.exit(f'\n{__file__}\n{ats_error_message}\n')

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2024, https://vroncevic.github.io/dist_py_module'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/dist_py_module/blob/dev/LICENSE'
__version__ = '3.0.1'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class DistPyModule(CfgCLI):
    '''
        Defines class DistPyModule with attribute(s) and method(s).
        Loads a base info, creates an CLI interface and runs operations.

        It defines:

            :attributes:
                | _GEN_VERBOSE - Console text indicator for process-phase.
                | _CONFIG - Tool info file path.
                | _LOG - Tool log file path.
                | _LOGO - Logo for splash screen.
                | _OPS - List of tool options.
                | _logger - Logger object API.
            :methods:
                | __init__ - Initials DistPyModule constructor.
                | process - Processes and generates module setup.py.
    '''

    _GEN_VERBOSE: str = 'DIST_PY_MODULE'
    _CONFIG: str = '/conf/dist_py_module.cfg'
    _LOG: str = '/log/dist_py_module.log'
    _LOGO: str = '/conf/dist_py_module.logo'
    _OPS: List[str] = ['-g', '--gen', '-v', '--verbose', '--version']

    def __init__(self, verbose: bool = False) -> None:
        '''
            Initial constructor.

            :param verbose: Enable/Disable verbose option.
            :type verbose: <bool>
            :exceptions: None
        '''
        current_dir: str = dirname(realpath(__file__))
        dist_py_module_property: Dict[str, str | bool] = {
            'ats_organization': 'vroncevic',
            'ats_repository': 'dist_py_module',
            'ats_name': 'dist_py_module',
            'ats_logo_path': f'{current_dir}{self._LOGO}',
            'ats_use_github_infrastructure': True
        }
        Splash(dist_py_module_property, verbose)
        base_info: str = f'{current_dir}{self._CONFIG}'
        super().__init__(base_info, verbose)
        verbose_message(verbose, [f'{self._GEN_VERBOSE} init tool info'])
        self._logger = ATSLogger(
            self._GEN_VERBOSE.lower(), f'{current_dir}{self._LOG}', verbose
        )
        if self.tool_operational:
            self.add_new_option(
                self._OPS[0], self._OPS[1], dest='gen',
                help='generate module setup.py'
            )
            self.add_new_option(
                self._OPS[2], self._OPS[3],
                action='store_true', default=False,
                help='activate verbose mode'
            )
            self.add_new_option(
                self._OPS[4], action='version', version=__version__
            )

    def process(self, verbose: bool = False) -> bool:
        '''
            Process and run operation.

            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :return: True (success operation) | False
            :rtype: <bool>
            :exceptions: None
        '''
        status: bool = False
        if self.tool_operational:
            if len(sys.argv) >= 4:
                if sys.argv[2] not in self._OPS:
                    error_message(
                        [f'{self._GEN_VERBOSE.lower()} provide project name']
                    )
                    self._logger.write_log(
                        'provide project name', self._logger.ATS_ERROR
                    )
                    return status
            else:
                error_message(
                    [f'{self._GEN_VERBOSE.lower()} provide project name']
                )
                self._logger.write_log(
                    'provide project name', self._logger.ATS_ERROR
                )
                return status
            args: Any | Namespace = self.parse_args(sys.argv[2:])
            if bool(getattr(args, 'gen')):
                print(
                    " ".join([
                        f'[{self._GEN_VERBOSE.lower()}]',
                        'gen setup.py ',
                        str(getattr(args, 'gen'))
                    ])
                )
                generator = GenSetup(getattr(args, 'verbose') or verbose)
                status: bool = generator.gen_setup(
                    f'{getattr(args, "gen")}',
                    getattr(args, 'verbose') or verbose
                )
                if status:
                    success_message([f'{self._GEN_VERBOSE.lower()} done\n'])
                    self._logger.write_log(
                        f'gen setup.py {getattr(args, "gen")} done',
                        self._logger.ATS_INFO
                    )
                else:
                    error_message(
                        [f'{self._GEN_VERBOSE.lower()} generation failed']
                    )
                    self._logger.write_log(
                        'generation failed', self._logger.ATS_ERROR
                    )
            else:
                error_message(
                    [f'{self._GEN_VERBOSE.lower()} provide package name']
                )
                self._logger.write_log(
                    'provide package name', self._logger.ATS_ERROR
                )
        else:
            error_message(
                [f'{self._GEN_VERBOSE.lower()} tool is not operational']
            )
            self._logger.write_log(
                'tool is not operational', self._logger.ATS_ERROR
            )
        return status
