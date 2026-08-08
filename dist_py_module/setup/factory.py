# -*- coding: UTF-8 -*-

'''
Module
    factory.py
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
    Factory for creating the dist_py_module bundle.
'''

from __future__ import annotations

from ats_utilities.base.setup.factory import BaseBundleFactory
from ats_utilities.base.setup.bundle import BaseBundle
from ats_utilities.base.setup.options import BaseBundleOptions
from ats_utilities.context.bundle import ContextBundle
from ats_utilities.context.factory import ContextBundleFactory

from dist_py_module.setup.bundle import DistPyModuleBundle
from dist_py_module.setup.options import DistPyModuleBundleOptions
from dist_py_module.setup.registry import DistPyModuleBundleRegistry
from dist_py_module.setup.dependencies import DistPyModuleBundleDependencies
from dist_py_module.setup.opt_validator import DistPyModuleBundleOptionsValidator
from dist_py_module.setup.keys import DistPyModuleBundleKeys
from dist_py_module.core.service.engine import Service
from dist_py_module.infrastructure.subprocessor import SubProcessor
from dist_py_module.infrastructure.cli.engine import CLI
from dist_py_module.infrastructure.cli.setup.bundle import CLIBundle
from dist_py_module.infrastructure.cli.setup.dependencies import CLIBundleDependencies
from dist_py_module.infrastructure.cli.setup.registry import CLIBundleRegistry
from dist_py_module.infrastructure.command.command import CommandBundle
from dist_py_module.infrastructure.command.dist_py_module_command_definition import DistPyModuleCommandDefinition
from dist_py_module.infrastructure.command.dist_py_module_command_executor import DistPyModuleCommandExecutor

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2026, https://vroncevic.github.io/dist_py_module'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/dist_py_module/blob/dev/LICENSE'
__version__ = '3.1.1'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class DistPyModuleBundleFactory:
    '''
        Factory for creating the dist_py_module bundle.

        It defines:

            :attributes:
                | _info_file - Path to the dist_py_module info file.
            :methods:
                | create_bundle - Creates the dist_py_module bundle with optional pre-configured options.
    '''

    _info_file: str = 'dist_py_module/infrastructure/config/dist_py_module.cfg'

    @classmethod
    def create_bundle(cls, options: DistPyModuleBundleOptions | None = None) -> DistPyModuleBundle:
        '''
            Creates the dist_py_module bundle with optional pre-configured options.

            :param options: The pre-configured options for the dist_py_module bundle.
            :return: The dist_py_module bundle.
            :exceptions:
                | ATSValueError: The dist_py_module bundle options must be provided and have proper values.
                | ATSTypeError:  The dist_py_module bundle options must be an instance of Mapping and its
                |                attributes must be instances of their respective types.
                | ATSValueError: The dist_py_module bundle dependencies must be provided and have proper values.
                | ATSTypeError:  The dist_py_module bundle dependencies must be an instance of Mapping and its
                |                attributes must be instances of their respective types.
                | ATSValueError: The dist_py_module bundle must be provided and have proper values.
                | ATSTypeError:  The dist_py_module bundle must be an instance of DistPyModuleBundle and
                |                its attributes must be instances of their respective types.
        '''
        if options is not None:
            DistPyModuleBundleOptionsValidator.validate(options)

        info_file = options.get(DistPyModuleBundleKeys.OPTION_INFO_FILE) if options else cls._info_file

        context_bundle: ContextBundle = ContextBundleFactory.create_bundle()

        base_bundle: BaseBundle = BaseBundleFactory.create_bundle(
            options=BaseBundleOptions(
                info_file=info_file,
                use_generator=True,
                context_bundle=context_bundle
            )
        )

        subprocessor: SubProcessor = SubProcessor(generator=base_bundle.generation_manager)

        service: Service = Service(subprocessor=subprocessor)

        dist_py_module_definition: DistPyModuleCommandDefinition = DistPyModuleCommandDefinition()

        dist_py_module_bundle: CommandBundle = CommandBundle(
            definition=dist_py_module_definition,
            executor=DistPyModuleCommandExecutor(dist_py_module_definition)
        )

        cli_bundle: CLIBundle = CLIBundleRegistry.create_bundle(
            dependencies=CLIBundleDependencies(
                service=service,
                parser=base_bundle.option_manager,
                commands=[dist_py_module_bundle]
            )
        )

        cli: CLI = CLI(cli_bundle)

        return DistPyModuleBundleRegistry.create_bundle(
            dependencies=DistPyModuleBundleDependencies(
                base=base_bundle,
                service=service,
                subprocessor=subprocessor,
                cli=cli
            )
        )
