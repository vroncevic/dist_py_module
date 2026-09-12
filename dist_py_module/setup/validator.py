# -*- coding: UTF-8 -*-

'''
Module
    validator.py
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
    A validator for the dist_py_module bundle.
'''

from __future__ import annotations

from ats_utilities.base.setup.bundle import BaseBundle
from ats_utilities.exceptions import ATSValueError, ATSTypeError
from ats_utilities.validation.check_value import not_none
from ats_utilities.validation.check_type import istype

from dist_py_module.setup.bundle import DistPyModuleBundle
from dist_py_module.core.service.iservice import IService
from dist_py_module.core.service.isubprocessor import ISubProcessor
from dist_py_module.infrastructure.cli.icli import ICLI

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2026, https://vroncevic.github.io/dist_py_module'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/dist_py_module/blob/dev/LICENSE'
__version__ = '3.1.4'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class DistPyModuleBundleValidator:
    '''
        A validator for the dist_py_module bundle.

        It defines:

            :methods:
                | validate - Validates the dist_py_module bundle.
                | is_valid - Checks if the dist_py_module bundle is valid.
    '''

    @classmethod
    def validate(cls, bundle: DistPyModuleBundle) -> None:
        '''
            Validates the dist_py_module bundle.

            :param bundle: The dist_py_module bundle to be validated.
            :exceptions:
                | ATSValueError: The dist_py_module bundle must be provided and have proper values.
                | ATSTypeError:  The dist_py_module bundle must be an instance of DistPyModuleBundle and
                |                its attributes must be instances of their respective types.
        '''
        ctx: str = 'dist_py_module_bundle_validator::validate(...)'
        msg_bundle_none: str = 'the dist_py_module bundle must be provided'
        msg_bundle_istype: str = 'the dist_py_module bundle must be an instance of DistPyModuleBundle'
        msg_base_none: str = 'the base bundle must be provided'
        msg_service_none: str = 'the service must be provided'
        msg_subprocessor_none: str = 'the subprocessor must be provided'
        msg_cli_none: str = 'the cli must be provided'
        msg_base_istype: str = 'the base bundle must be an instance of BaseBundle'
        msg_service_istype: str = 'the service must be an instance of IService'
        msg_subprocessor_istype: str = 'the subprocessor must be an instance of ISubProcessor'
        msg_cli_istype: str = 'the cli must be an instance of ICLI'

        not_none(bundle, ctx, msg_bundle_none)
        istype(bundle, DistPyModuleBundle, ctx, msg_bundle_istype)

        not_none(bundle.base, ctx, msg_base_none)
        not_none(bundle.service, ctx, msg_service_none)
        not_none(bundle.subprocessor, ctx, msg_subprocessor_none)
        not_none(bundle.cli, ctx, msg_cli_none)

        istype(bundle.base, BaseBundle, ctx, msg_base_istype)
        istype(bundle.service, IService, ctx, msg_service_istype)
        istype(bundle.subprocessor, ISubProcessor, ctx, msg_subprocessor_istype)
        istype(bundle.cli, ICLI, ctx, msg_cli_istype)

    @classmethod
    def is_valid(cls, bundle: DistPyModuleBundle) -> bool:
        '''
            Checks if the dist_py_module bundle is valid.

            :param bundle: The dist_py_module bundle to be checked.
            :return: True if valid, False otherwise.
        '''
        try:
            cls.validate(bundle)
            return True

        except (ATSValueError, ATSTypeError):
            return False
