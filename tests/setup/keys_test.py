# -*- coding: UTF-8 -*-

'''
Module
    keys_test.py
Info
    Unit tests for ARMPicomBundleKeys class.
'''

from __future__ import annotations

import unittest
from types import MappingProxyType

from dist_py_module.setup.keys import DistPyModuleBundleKeys


class TestDistPyModuleBundleKeys(unittest.TestCase):

    def test_get_dependency_to_type(self) -> None:
        deps = DistPyModuleBundleKeys.get_dependency_to_type()
        self.assertIsInstance(deps, MappingProxyType)
        self.assertIn(DistPyModuleBundleKeys.DEPENDENCY_BASE, deps)
        self.assertIn(DistPyModuleBundleKeys.DEPENDENCY_SERVICE, deps)
        self.assertIn(DistPyModuleBundleKeys.DEPENDENCY_SUBPROCESSOR, deps)
        self.assertIn(DistPyModuleBundleKeys.DEPENDENCY_CLI, deps)

    def test_get_option_to_type(self) -> None:
        opts = DistPyModuleBundleKeys.get_option_to_type()
        self.assertIsInstance(opts, MappingProxyType)
        self.assertIn(DistPyModuleBundleKeys.OPTION_INFO_FILE, opts)
