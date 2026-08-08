# -*- coding: UTF-8 -*-

'''
Module
    dependencies.py
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
    DistPyModule bundle dependencies for the dist_py_module bundle.
'''

from __future__ import annotations

from typing import TypedDict

from ats_utilities.base.setup.bundle import BaseBundle

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


class DistPyModuleBundleDependencies(TypedDict):
    '''
        DistPyModule bundle dependencies for the dist_py_module bundle.

        It defines:

            :attributes:
                | base - The base bundle with the base components for the dist_py_module bundle.
                | service - The service orchestrating the dist_py_module's execution for the dist_py_module bundle.
                | subprocessor - The adapter executing the dist_py_module's sub-processes for the dist_py_module bundle.
                | cli - The command-line interface adapter for the dist_py_module bundle.
    '''

    base: BaseBundle
    service: IService
    subprocessor: ISubProcessor
    cli: ICLI
