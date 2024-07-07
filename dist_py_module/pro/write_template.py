# -*- coding: UTF-8 -*-

'''
modules
    write_template.py
Copyright
    Copyright (C) 2017 - 2024 Vladimir Roncevic <elektron.ronca@gmail.com>
    dist_py_modules is free software: you can redistribute it and/or modify it
    under the terms of the GNU General Public License as published by the
    Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    dist_py_modules is distributed in the hope that it will be useful, but
    WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
    See the GNU General Public License for more details.
    You should have received a copy of the GNU General Public License along
    with this program. If not, see <http://www.gnu.org/licenses/>.
Info
    Defines class WriteTemplate with attribute(s) and method(s).
    Creates an API for writing  setup template with parameters.
'''

import sys
from typing import Any, List, Dict, Optional
from os import getcwd, chmod
from datetime import datetime
from string import Template

try:
    from ats_utilities.config_io.file_check import FileCheck
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.exceptions.ats_value_error import ATSValueError
except ImportError as ats_error_message:
    # Force close python ATS ##################################################
    sys.exit(f'\n{__file__}\n{ats_error_message}\n')

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2024, https://vroncevic.github.io/dist_py_modules'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/dist_py_modules/blob/dev/LICENSE'
__version__ = '3.0.7'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class WriteTemplate(FileCheck):
    '''
        Defines class WriteTemplate with attribute(s) and method(s).
        Creates an API for writing  setup template with parameters.

        It defines:

            :attributes:
                | _GEN_VERBOSE - Console text indicator for process-phase.
            :methods:
                | __init__ - Initials WriteTemplate constructor.
                | write - Writes setup content to file.
    '''

    _GEN_VERBOSE: str = 'DIST_PY_MODULES::PRO::WRITE_TEMPLATE'

    def __init__(self, verbose: bool = False) -> None:
        '''
            Initial constructor.

            :param verbose: Enable/Disable verbose option.
            :type verbose: <bool>
            :exceptions: None
        '''
        super().__init__(verbose)
        verbose_message(verbose, [f'{self._GEN_VERBOSE.lower()} init writer'])

    def write(
        self,
        setup_content: Dict[Any, Any],
        package_name: str,
        modules: List[str],
        verbose: bool = False
    ) -> bool:
        '''
            Writes setup content to file.

            :param setup_content: Content for module setup.py
            :type setup_content: <Dict[Any, Any]>
            :param package_name: Package name
            :type package_name: <str>
            :param modules: List of modules
            :type modules: <List[str]>
            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :return: True (success operation) | False
            :rtype: <bool>
            :exception: ATSTypeError | ATSValueError
        '''
        error_msg: Optional[str] = None
        error_id: Optional[int] = None
        error_msg, error_id = self.check_params([
            ('dict:setup_content', setup_content),
            ('str:package_name', package_name),
            ('list:modules', modules)
        ])
        if error_id == self.TYPE_ERROR:
            raise ATSTypeError(error_msg)
        if not bool(setup_content):
            raise ATSValueError('missing setup content')
        if not bool(package_name):
            raise ATSValueError('missing package name')
        if not bool(modules):
            raise ATSValueError('missing setup modules')
        all_stat: List[bool] = []
        setup = list(f'{getcwd()}/{module}' for module in modules)
        verbose_message(
            verbose, [f'{self._GEN_VERBOSE.lower()} write modules']
        )
        for index, content in enumerate(setup_content.values()):
            template: Template = Template(content)
            if bool(template):
                with open(
                    setup[index], 'w', encoding='utf-8'
                ) as setup_file:
                    setup_file.write(template.substitute({
                        'PKG': f'{package_name}',
                        'YEAR': f'{datetime.now().year}'
                    }))
                    chmod(setup[index], 0o666)
                    self.check_path(setup[index], verbose)
                    self.check_mode('w', verbose)
                    self.check_format(
                        setup[index],
                        setup[index].split('.')[1],
                        verbose
                    )
                    if self.is_file_ok():
                        all_stat.append(True)
                    else:
                        all_stat.append(False)
            else:
                all_stat.append(False)
        return all([all(all_stat), bool(all_stat)])
