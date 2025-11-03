#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
Module
    dist_py_module_run.py
Copyright
    Copyright (C) 2017 - 2025 Vladimir Roncevic <elektron.ronca@gmail.com>
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
    Main entry point for tool dist_py_module.
'''

import sys
from typing import List

try:
    from dist_py_module import DistPyModule
except ImportError as ats_error_message:  # pragma: no cover
    # Force exit python #######################################################
    sys.exit(f'\n{__file__}\n{ats_error_message}\n')  # pragma: no cover

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2025, https://vroncevic.github.io/dist_py_module'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/dist_py_module/blob/dev/LICENSE'
__version__: str = '3.0.8'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'

if __name__ == '__main__':
    TOOL: DistPyModule = DistPyModule(verbose=False)
    TOOL.process(verbose=False)
