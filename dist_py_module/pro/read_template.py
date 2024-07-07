# -*- coding: UTF-8 -*-

'''
Module
    read_template.py
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
    Defines class ReadTemplate with attribute(s) and method(s).
    Creates an API for reading a template file.
'''

import sys
from typing import Any, List, Dict, Optional
from os.path import dirname, realpath

try:
    from ats_utilities.config_io.file_check import FileCheck
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.exceptions.ats_value_error import ATSValueError
except ImportError as ats_error_message:
    # Force close python ATS ##################################################
    sys.exit(f'\n{__file__}\n{ats_error_message}\n')

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2024, https://vroncevic.github.io/dist_py_module'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/dist_py_module/blob/dev/LICENSE'
__version__ = '3.0.7'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class ReadTemplate(FileCheck):
    '''
        Defines class ReadTemplate with attribute(s) and method(s).
        Creates an API for reading a template file.

        It defines:

            :attributes:
                | _GEN_VERBOSE - Console text indicator for process-phase.
                | _TEMPLATE_DIR - Template dir path.
            :methods:
                | __init__ - Initials ReadTemplate constructor.
                | read - Reads a template file.
    '''

    _GEN_VERBOSE: str = 'DIST_PY_MODULE::PRO::READ_TEMPLATE'
    _TEMPLATE_DIR: str = '/../conf/template/'

    def __init__(self, verbose: bool = False) -> None:
        '''
            Initials ReadTemplate constructor.

            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :exceptions: None
        '''
        super().__init__(verbose)
        verbose_message(verbose, [f'{self._GEN_VERBOSE.lower()} init reader'])

    def read(
        self,
        template_files: Optional[List[str]],
        verbose: bool = False
    ) -> Dict[Any, Any]:
        '''
            Reads a template file.

            :param template_files: Template file | None
            :type template_files: <Optional[List[str]]>
            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :return: Template content for setup module
            :rtype: <Dict[Any, Any]>
            :exceptions: ATSTypeError | ATSValueError
        '''
        error_msg: Optional[str] = None
        error_id: Optional[int] = None
        error_msg, error_id = self.check_params([
            ('list:template_files', template_files)
        ])
        if error_id == self.TYPE_ERROR:
            raise ATSTypeError(error_msg)
        if not bool(template_files):
            raise ATSValueError('missing template name')
        config: Dict[Any, Any] = {}
        verbose_message(
            verbose, [f'{self._GEN_VERBOSE.lower()} load templates']
        )
        current_dir: str = dirname(realpath(__file__))
        template_dir: str = f'{current_dir}{self._TEMPLATE_DIR}'
        for template_file in template_files:
            template_module: str = f'{template_dir}{template_file}'
            self.check_path(template_module, verbose)
            self.check_mode('r', verbose)
            self.check_format(template_module, 'template', verbose)
            if self.is_file_ok():
                with open(
                    template_module, 'r', encoding='utf-8'
                ) as setup_template:
                    config[template_file] = setup_template.read()
        return config
