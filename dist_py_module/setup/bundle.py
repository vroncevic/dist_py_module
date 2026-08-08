# -*- coding: UTF-8 -*-

'''
Module
    bundle.py
Copyright
    Copyright (C) 2026 Vladimir Roncevic <elektron.ronca@gmail.com>
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
    Defines the dist_py_module bundle.
'''

from __future__ import annotations

from dataclasses import dataclass

from ats_utilities.base.setup.bundle import BaseBundle
from ats_utilities.utils.reflection import instance_to_dict

from dist_py_module.core.service.iservice import IService
from dist_py_module.core.service.isubprocessor import ISubProcessor
from dist_py_module.infrastructure.cli.icli import ICLI

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2026, https://vroncevic.github.io/dist_py_module'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/dist_py_module/blob/dev/LICENSE'
__version__ = '3.1.1'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


@dataclass(slots=True, frozen=True, kw_only=True)
class DistPyModuleBundle:
    '''
        DistPyModule bundle holding the components of the dist_py_module.

        It defines:

            :attributes:
                | base - The base bundle with the base components.
                | service - The service orchestrating the dist_py_module's execution.
                | subprocessor - The adapter executing the dist_py_module's sub-processes.
                | cli - The command-line interface adapter.
            :methods:
                | to_dict - Converts the dist_py_module bundle to a dictionary.
    '''

    base: BaseBundle
    service: IService
    subprocessor: ISubProcessor
    cli: ICLI

    def to_dict(self) -> dict[str, object]:
        '''
            Converts the dist_py_module bundle to a dictionary.

            :return: Dictionary representation of the dist_py_module bundle.
            :exceptions: None.
        '''
        return instance_to_dict(self)
