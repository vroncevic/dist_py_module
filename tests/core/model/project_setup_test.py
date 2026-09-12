# -*- coding: UTF-8 -*-

'''
Module
    project_setup_test.py
Info
    Unit tests for ProjectSetup class.
'''

from __future__ import annotations

import unittest

from dist_py_module.core.model.project_setup import ProjectSetup


class TestProjectSetup(unittest.TestCase):
    def test_project_setup_initialization(self) -> None:
        dist_config = {'key': 'value'}
        setup = ProjectSetup(dist_config=dist_config)
        self.assertEqual(setup.dist_config, dist_config)
