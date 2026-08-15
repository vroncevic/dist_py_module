# -*- coding: UTF-8 -*-

'''
Module
    registry.py
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
    Encapsulates core dist_py_module components for simplification of dist_py_module bundle.
'''

from __future__ import annotations

from ats_utilities.base.setup.bundle import BaseBundle

from dist_py_module.core.service.iservice import IService
from dist_py_module.core.service.isubprocessor import ISubProcessor
from dist_py_module.infrastructure.cli.icli import ICLI
from dist_py_module.setup.bundle import DistPyModuleBundle
from dist_py_module.setup.validator import DistPyModuleBundleValidator
from dist_py_module.setup.keys import DistPyModuleBundleKeys
from dist_py_module.setup.dependencies import DistPyModuleBundleDependencies
from dist_py_module.setup.dep_validator import DistPyModuleBundleDependenciesValidator

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2026, https://vroncevic.github.io/dist_py_module'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/dist_py_module/blob/dev/LICENSE'
__version__ = '3.1.3'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class DistPyModuleBundleRegistry:
    '''
        Encapsulates core dist_py_module components for simplification of dist_py_module bundle.

        It defines:

            :methods:
                | create_bundle - Creates the dist_py_module bundle.
                | get_version - Returns the registry version.
    '''

    @classmethod
    def create_bundle(cls, dependencies: DistPyModuleBundleDependencies) -> DistPyModuleBundle:
        '''
            Creates the dist_py_module bundle.

            :param dependencies: The dist_py_module bundle dependencies.
            :return: The dist_py_module bundle.
            :exceptions:
                | ATSValueError: The dist_py_module bundle dependencies must be provided and have proper values.
                | ATSTypeError:  The dist_py_module bundle dependencies must be an instance of Mapping and its
                |                attributes must be instances of their respective types.
                | ATSValueError: The dist_py_module bundle must be provided and have proper values.
                | ATSTypeError:  The dist_py_module bundle must be an instance of DistPyModuleBundle and
                |                its attributes must be instances of their respective types.
        '''
        DistPyModuleBundleDependenciesValidator.validate(dependencies)

        base: BaseBundle | None = dependencies.get(DistPyModuleBundleKeys.DEPENDENCY_BASE) if dependencies else None
        service: IService | None = dependencies.get(DistPyModuleBundleKeys.DEPENDENCY_SERVICE) if dependencies else None
        subprocessor: ISubProcessor | None = dependencies.get(DistPyModuleBundleKeys.DEPENDENCY_SUBPROCESSOR) if dependencies else None
        cli: ICLI | None = dependencies.get(DistPyModuleBundleKeys.DEPENDENCY_CLI) if dependencies else None

        bundle: DistPyModuleBundle = DistPyModuleBundle(base=base, service=service, subprocessor=subprocessor, cli=cli)

        DistPyModuleBundleValidator.validate(bundle)

        return bundle

    @classmethod
    def get_version(cls) -> str:
        '''
            Returns the registry version.

            :return: The registry version.
            :exceptions: None.
        '''
        return __version__
