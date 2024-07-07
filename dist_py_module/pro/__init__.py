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
    Defines class GenSetup with attribute(s) and method(s).
    Generates module file setup.py by template and parameters.
'''

import sys
from typing import Any, List, Dict, Optional
from os.path import dirname, realpath

try:
    from ats_utilities.config_io.file_check import FileCheck
    from ats_utilities.console_io.error import error_message
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.config_io.yaml.yaml2object import Yaml2Object
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.exceptions.ats_value_error import ATSValueError
    from dist_py_module.pro.read_template import ReadTemplate
    from dist_py_module.pro.write_template import WriteTemplate
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


class GenSetup(FileCheck):
    '''
        Defines class GenSetup with attribute(s) and method(s).
        Generates module file setup.py by template and parameters.

        It defines:

            :attributes:
                | _GEN_VERBOSE - Console text indicator for process-phase.
                | _PRO_STRUCTURE - Project setup (template, module).
                | _reader - Reader API.
                | _writer - Writer API.
            :methods:
                | __init__ - Initials GenSetup constructor.
                | get_reader - Gets template reader.
                | get_writer - Gets template writer.
                | gen_setup - Generates module file setup.py.
                | select_pro - Selects project structure.
    '''

    _GEN_VERBOSE: str = 'DIST_PY_MODULE::PRO::GEN_SETUP'
    _PRO_STRUCTURE: str = '/../conf/project.yaml'

    def __init__(self, verbose: bool = False) -> None:
        '''
            Initials GenSetup constructor.

            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :exceptions: None
        '''
        super().__init__(verbose)
        verbose_message(verbose, [f'{self._GEN_VERBOSE.lower()} init setup'])
        self._reader: Optional[ReadTemplate] = ReadTemplate(verbose)
        self._writer: Optional[WriteTemplate] = WriteTemplate(verbose)
        current_dir: str = dirname(realpath(__file__))
        project: str = f'{current_dir}{self._PRO_STRUCTURE}'
        self.check_path(project, verbose)
        self.check_mode('r', verbose)
        self.check_format(project, 'yaml', verbose)
        if self.is_file_ok():
            yml2obj: Yaml2Object | None = Yaml2Object(project)
            self.config: Dict[Any, Any] = yml2obj.read_configuration()

    def get_reader(self) -> Optional[ReadTemplate]:
        '''
            Gets template reader.

            :return: Template reader object | None
            :rtype: <Optional[ReadTemplate]>
            :exceptions: None
        '''
        return self._reader

    def get_writer(self) -> Optional[WriteTemplate]:
        '''
            Gets template writer.

            :return: Template writer object | none
            :rtype: <Optional[WriteTemplate]>
            :exceptions: None
        '''
        return self._writer

    def gen_setup(
        self, pack_name: Optional[str], verbose: bool = False
    ) -> bool:
        '''
            Generates setup.py for python package.

            :param pack_name: Package name | None
            :type pack_name: <Optional[str]>
            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :return: True (success operation) | False
            :rtype: <bool>
            :exceptions: ATSTypeError | ATSValueError
        '''
        error_msg: Optional[str] = None
        error_id: Optional[int] = None
        error_msg, error_id = self.check_params([
            ('str:pack_name', pack_name)
        ])
        if error_id == self.TYPE_ERROR:
            raise ATSTypeError(error_msg)
        if not bool(pack_name):
            raise ATSValueError('missing package name')
        status: bool = False
        verbose_message(
            verbose, [
                f'{self._GEN_VERBOSE.lower()} generating package', pack_name
            ]
        )
        template_files: Optional[List[str]] = self.select_pro(verbose)
        if bool(template_files) and self._reader and self._writer:
            if 'cancel' in template_files:
                status = True
            else:
                setup_content: Dict[Any, Any] = self._reader.read(
                    template_files, verbose
                )
                if bool(setup_content):
                    status: bool = self._writer.write(
                        setup_content, pack_name,
                        self.config['modules'], verbose
                    )
        return status

    def select_pro(self, verbose: bool = False) -> Optional[List[str]]:
        '''
            Select project structure.

            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :return: Templates | None
            :rtype: <Optional[List[str]]>
            :exceptions: None
        '''
        template_selected: Optional[List[str]] = None
        if bool(self.config):
            types: Dict[Any, Any] = self.config['templates']
            pro_types_len: int = len(types)
            for index, pro_type in enumerate(types):
                for project_type, template_files in pro_type.items():
                    print(
                        f'{index + 1} {project_type.capitalize()}'
                    )
                    verbose_message(
                        verbose, [
                            f'{self._GEN_VERBOSE.lower()} processed template',
                            template_files
                        ]
                    )
            while True:
                input_type: str = input(' select project type: ')
                options = range(1, pro_types_len + 1, 1)
                if int(input_type) in list(options):
                    for target in types[int(input_type) - 1].values():
                        if target is None:
                            template_selected = ['cancel']
                        else:
                            template_selected = target
                    break
                else:
                    error_message([
                        f'{self._GEN_VERBOSE.lower()} not suitable'
                    ])
            verbose_message(
                verbose, [
                    f'{self._GEN_VERBOSE.lower()} selected', template_selected
                ]
            )
        return template_selected
