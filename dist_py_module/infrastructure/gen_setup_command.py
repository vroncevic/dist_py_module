# -*- coding: UTF-8 -*-

'''
Module
    gen_setup_command.py
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
    Defines GenSetupCommand class implementing ICLICommand strategy.
'''

from typing import Any, override
from datetime import date
from ats_utilities.option.command_option import CommandOption
from ats_utilities.factory_class import format_instance_to_string
from dist_py_module.infrastructure.icli_command import ICLICommand
from dist_py_module.domain.ports.ifile_gen import IFileGen

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/dist_py_module'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/dist_py_module/blob/dev/LICENSE'
__version__: str = '3.1.0'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Development'


class GenSetupCommand(ICLICommand):
    '''
        CLI subcommand for generating setup files.

        It defines:

            :attributes: None.
            :methods:
                | name - Returns the command name key.
                | help_text - Returns the command help text.
                | options - Returns the command options.
                | execute - Executes the configuration file generation logic.
                | __str__ - Returns GenSetupCommand instance as string representation.
    '''

    @property
    @override
    def name(self) -> str:
        '''
            Returns the command name key.

            :return: The command name key.
            :rtype: <str>
            :exceptions: None.
        '''
        return "setup"

    @property
    @override
    def help_text(self) -> str:
        '''
            Returns the command help text.

            :return: The command help text.
            :rtype: <str>
            :exceptions: None.
        '''
        return "Generate setup files"

    @property
    @override
    def options(self) -> list[CommandOption]:
        '''
            Returns the command options.

            :return: List of command options.
            :rtype: <List[CommandOption]>
            :exceptions: None.
        '''
        return [
            CommandOption(
                name="--package-name",
                help_text="Package name",
                required=True
            ),
            CommandOption(
                name="--version",
                help_text="Application version",
                required=True
            ),
            CommandOption(
                name="--description",
                help_text="Application description",
                required=True
            ),
            CommandOption(
                name="--author",
                help_text="Author name",
                required=True
            ),
            CommandOption(
                name="--email",
                help_text="Author email",
                required=True
            ),
            CommandOption(
                name="--github",
                help_text="GitHub username",
                default="vroncevic"
            ),
            CommandOption(
                name="--license",
                help_text="License",
                default="GNU General Public License (GPL)"
            )
        ]

    @override
    def execute(self, params: dict[str, Any], service: IFileGen) -> dict[str, Any]:
        '''
            Executes the configuration file generation logic.

            :param params: Subcommand parameters from CLI parser.
            :type params: <dict[str, Any]>
            :param service: Generation orchestrator service instance.
            :type service: <IFileGen>
            :return: Return code, stdout and stderr messages.
            :return type: <dict[str, Any]>
            :exceptions: None.
        '''
        target_filename = params.pop("filename", "setup.py")
        params["year"] = str(date.today().year)

        return service.execute(
            template_name="setup",
            target_filename=target_filename,
            cli_params=params
        )

    @override
    def __str__(self) -> str:
        '''
            Returns GenSetupCommand instance as string representation.

            :return: GenSetupCommand instance as string representation.
            :rtype: <str>
            :exceptions: None.
        '''
        return format_instance_to_string(self)
