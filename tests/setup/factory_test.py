# -*- coding: UTF-8 -*-

'''
Module
    factory_test.py
Info
    Unit tests for DistPyModuleBundleFactory class.
'''

from __future__ import annotations

import unittest

from dist_py_module.setup.bundle import DistPyModuleBundle
from dist_py_module.setup.factory import DistPyModuleBundleFactory


class TestDistPyModuleBundleFactory(unittest.TestCase):

    def test_create_bundle_default(self) -> None:
        bundle = DistPyModuleBundleFactory.create_bundle()
        self.assertIsInstance(bundle, DistPyModuleBundle)

    def test_create_bundle_with_options(self) -> None:
        options = {'info_file': 'dist_py_module/infrastructure/config/dist_py_module.cfg'}
        bundle = DistPyModuleBundleFactory.create_bundle(options)
        self.assertIsInstance(bundle, DistPyModuleBundle)

    def test_create_bundle_invalid_options(self) -> None:
        options = {'info_file': 123}
        with self.assertRaises(Exception):
            DistPyModuleBundleFactory.create_bundle(options)

    def test_get_version(self) -> None:
        self.assertEqual(DistPyModuleBundleFactory.get_version(), '3.1.3')
