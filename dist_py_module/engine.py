# -*- coding: UTF-8 -*-

'''
Module
    engine.py
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
    Main engine orchestrator class for Task Code Generator CLI.
'''

from typing import Any, override
from os.path import dirname, realpath
from ats_utilities.base.engine import Base
from ats_utilities.base.component_bundle import BaseComponentBundle
from ats_utilities.option.ioption_parser import IOptionManager
from ats_utilities.exceptions.ats_value_error import ATSValueError
from dist_py_module.dist_py_module_bundle import DistPyModuleBundle
from dist_py_module.domain.ports.itemplate_provider import ITemplateProvider
from dist_py_module.infrastructure.template_provider import TemplateProvider
from dist_py_module.domain.ports.ifile_writer import IFileWriter
from dist_py_module.infrastructure.file_writer import FileWriter
from dist_py_module.domain.ports.ifile_gen import IFileGen
from dist_py_module.application.service import FileGen
from dist_py_module.application.service_bundle import ServiceBundle
from dist_py_module.infrastructure.icli_command import ICLICommand
from dist_py_module.infrastructure.cli_bundle import CLIBundle
from dist_py_module.infrastructure.gen_setup_command import GenSetupCommand
from dist_py_module.infrastructure.icli import ICLI
from dist_py_module.infrastructure.cli import CLI

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/dist_py_module'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/dist_py_module/blob/dev/LICENSE'
__version__: str = '3.1.1'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Development'


class DistPyModule(Base):
    '''
        Engine orchestrating the initialization and execution of DistPyModule.

        It defines:

            :attributes:
                | _info_file - Path to the info file.
                | _cli - Adapter for command line user interface.
            :methods:
                | __init__ - Initializes the DistPyModule engine with adapters and services.
                | process - Starts DistPyModule via CLI adapter.
    '''

    _info_file: str = 'infrastructure/config/dist_py_module.cfg'

    def __init__(self, component_bundle: DistPyModuleBundle | None = None) -> None:
        '''
            Initializes the DistPyModule engine with adapters and services.

            :param component_bundle: DistPyModule bundle containing adapters and services | None.
            :type component_bundle: <DistPyModuleBundle | None>
            :exceptions: None.
        '''
        current_dir: str = dirname(realpath(__file__))
        super().__init__(BaseComponentBundle(info_file=f'{current_dir}/{self._info_file}'))

        try:
            if not self._is_initialized:
                raise ATSValueError(f'failed to initialize engine with {current_dir}/{self._info_file}')

            # Mark as not initialized (waiting for other components to be initialized)
            self._is_initialized = False

            # Use provided component bundle or use default adapters
            bundle: DistPyModuleBundle = component_bundle or DistPyModuleBundle()

            # Initialization of secondary adapters (Infrastructure)
            template_provider: ITemplateProvider = bundle.template_provider or TemplateProvider()
            file_writer: IFileWriter = bundle.file_writer or FileWriter()

            # Initialization of option manager adapter (Adapter for options parsing)
            parser: IOptionManager = bundle.parser or self._options_parser

            # Injecting adapters into the application service (Orchestration)
            service_bundle: ServiceBundle = ServiceBundle(
                template_provider=template_provider, file_writer=file_writer
            )
            service: IFileGen = bundle.service or FileGen(service_bundle)

            # Setting up CLI command strategies (Command strategies for CLI)
            commands: list[ICLICommand] = [GenSetupCommand()]

            # Setting up primary adapter (CLI interface)
            cli_bundle: CLIBundle = CLIBundle(service=service, parser=parser, commands=commands)
            self._cli: ICLI = bundle.cli or CLI(cli_bundle)

            # Mark as initialized (all components initialized)
            self._is_initialized = all([
               component.is_initialized() for component in [template_provider, file_writer, service, self._cli] if component
            ])
            self._reporter.success(["✅ dist_py_module: engine initialized successfully."])

        except (ATSValueError, ValueError) as exc:
            self._reporter.error([f'❌ dist_py_module: {exc}'])
        except Exception as exc:
            self._reporter.error([f'❌ dist_py_module unexpected exception: {exc}'])

    @override
    def process(self) -> None:
        '''
            Starts DistPyModule via CLI adapter.

            :exceptions: None.
        '''
        result: dict[str, Any] = {}

        try:
            if self.is_initialized():
                self._reporter.success(["🔥 Starting execution command..."])
                result = self._cli.run()
                self._reporter.success(["✅ Execution finished!"])

                if result.get("returncode") != 0:
                    self._reporter.error([f'❌ dist_py_module: {result.get("stderr")}'])
                    self._reporter.error([f'❌ dist_py_module: exiting with error.'])
                else:
                    self._reporter.success([f'✅ dist_py_module: {result.get("stdout") or 'done!'}'])
                    self._reporter.success([f'✅ dist_py_module: exiting successfully.'])
            else:
                self._reporter.error([f'❌ dist_py_module: engine not initialized.'])

        except (ATSValueError, ValueError) as exc:
            self._reporter.error([f'❌ dist_py_module: {exc}'])
        except Exception as exc:
            self._reporter.error([f'❌ dist_py_module unexpected exception: {exc}'])
