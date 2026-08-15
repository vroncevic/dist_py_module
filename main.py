# -*- coding: UTF-8 -*-

'''
Module
    main.py
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
    Main entry point for Task Code Generator CLI.
'''

from __future__ import annotations

from sys import exit

from dist_py_module.engine import DistPyModule
from dist_py_module.setup.factory import DistPyModuleBundleFactory

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2026, https://vroncevic.github.io/dist_py_module'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/dist_py_module/blob/dev/LICENSE'
__version__ = '3.1.3'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


def main() -> bool:
    '''
        Bootstraps and runs the dist_py_module with required adapters.

        :return: True if successful, False otherwise.
        :exceptions: None
    '''
    dist_py_module: DistPyModule = DistPyModule(DistPyModuleBundleFactory.create_bundle())

    return dist_py_module.process()


if __name__ == '__main__':
    '''
        Entry point for dist_py_module execution.

        :exit code: 0 if successful, 1 otherwise.
        :exceptions: None
    '''
    exit(0 if main() else 1)
