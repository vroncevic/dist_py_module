# -*- coding: UTF-8 -*-

'''
Module
    dist_py_module_command_definition.py
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
    Defines DistPyModuleCommandDefinition class.
'''

from __future__ import annotations

from collections.abc import Sequence

from ats_utilities.option.command.data import OptionData
from ats_utilities.utils.reflection import to_str

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2026, https://vroncevic.github.io/dist_py_module'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/dist_py_module/blob/dev/LICENSE'
__version__ = '3.1.1'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class DistPyModuleCommandDefinition:
    '''
        CLI subcommand metadata definition for dist_py_module setup generation.

        It defines:

            :methods:
                | name - Returns the command name.
                | help_text - Returns the command help text.
                | options - Returns the sequence of command options.
                | __str__ - Returns the command definition as string representation.
    '''

    @property
    def name(self) -> str:
        '''
            Returns the command name.

            :return: The command name.
        '''
        return 'setup'

    @property
    def help_text(self) -> str:
        '''
            Returns the command help text.

            :return: The command help text.
        '''
        return 'Generate setup files'

    @property
    def options(self) -> Sequence[OptionData]:
        '''
            Returns the command options.

            :return: Sequence of command options.
        '''
        return [
            OptionData(
                name="--package-name",
                help_text="Package name",
                action=None,
                default=None,
                required=True,
                choices=None,
                nargs=None
            ),
            OptionData(
                name="--version",
                help_text="Application version",
                action=None,
                default=None,
                required=True,
                choices=None,
                nargs=None
            ),
            OptionData(
                name="--description",
                help_text="Application description",
                action=None,
                default=None,
                required=True,
                choices=None,
                nargs=None
            ),
            OptionData(
                name="--author",
                help_text="Author name",
                action=None,
                default=None,
                required=True,
                choices=None,
                nargs=None
            ),
            OptionData(
                name="--email",
                help_text="Author email",
                action=None,
                default=None,
                required=True,
                choices=None,
                nargs=None
            ),
            OptionData(
                name="--github",
                help_text="GitHub username",
                action=None,
                default="vroncevic",
                required=False,
                choices=None,
                nargs=None
            ),
            OptionData(
                name="--license",
                help_text="License",
                action=None,
                default="GNU General Public License (GPL)",
                required=False,
                choices=None,
                nargs=None
            ),
            OptionData(
                name="--output",
                help_text="Path to the output directory",
                action=None,
                default="./",
                required=False,
                choices=None,
                nargs=None
            )
        ]

    def __str__(self) -> str:
        '''
            Returns the command definition as string representation.

            :return: The command definition as string representation.
        '''
        return to_str(self)
