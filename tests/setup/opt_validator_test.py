# -*- coding: UTF-8 -*-

'''
Module
    opt_validator_test.py
Info
    Unit tests for ARMPicomBundleOptionsValidator class.
'''

from __future__ import annotations

import unittest

from dist_py_module.setup.opt_validator import DistPyModuleBundleOptionsValidator


class TestDistPyModuleBundleOptionsValidator(unittest.TestCase):

    def test_validate_success(self) -> None:
        options = {'info_file': 'some_path'}
        DistPyModuleBundleOptionsValidator.validate(options)

    def test_validate_none(self) -> None:
        with self.assertRaises(Exception):
            DistPyModuleBundleOptionsValidator.validate(None)

    def test_validate_invalid_type(self) -> None:
        with self.assertRaises(Exception):
            DistPyModuleBundleOptionsValidator.validate("not_a_mapping")

    def test_validate_invalid_option_type(self) -> None:
        with self.assertRaises(Exception):
            options = {'info_file': 123}
            DistPyModuleBundleOptionsValidator.validate(options)
