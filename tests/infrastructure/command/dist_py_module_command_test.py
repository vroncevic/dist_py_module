# -*- coding: UTF-8 -*-

'''
Module
    dist_py_module_command_test.py
Info
    Unit tests for DistPyModuleCommandDefinition and DistPyModuleCommandExecutor.
'''

from __future__ import annotations

import unittest
from unittest.mock import Mock

from dist_py_module.core.service.iservice import IService
from dist_py_module.infrastructure.command.dist_py_module_command_definition import DistPyModuleCommandDefinition
from dist_py_module.infrastructure.command.dist_py_module_command_executor import DistPyModuleCommandExecutor


class TestDistPyModuleCommand(unittest.TestCase):

    def test_definition(self) -> None:
        definition = DistPyModuleCommandDefinition()
        self.assertEqual(definition.name, 'setup')
        self.assertEqual(definition.help_text, 'Generate setup files')
        self.assertEqual(len(definition.options), 8)
        self.assertTrue(isinstance(str(definition), str))

    def test_executor_execute_success(self) -> None:
        definition = DistPyModuleCommandDefinition()
        executor = DistPyModuleCommandExecutor(definition)
        
        mock_service = Mock(spec=IService)
        mock_service.is_initialized.return_value = True
        mock_service.execute.return_value = {'returncode': 0}
        
        params = {
            'package_name': 'test',
            'version': '1.0.0',
            'description': 'test description',
            'author': 'test author',
            'email': 'test@example.com',
            'output': '.'
        }
        result = executor.execute(params=params, service=mock_service)
        
        self.assertEqual(result['returncode'], 0)
        mock_service.execute.assert_called_once_with(params=params)

    def test_executor_execute_not_initialized(self) -> None:
        definition = DistPyModuleCommandDefinition()
        executor = DistPyModuleCommandExecutor(definition)
        
        mock_service = Mock(spec=IService)
        mock_service.is_initialized.return_value = False
        
        result = executor.execute(params={}, service=mock_service)
        self.assertEqual(result['returncode'], 1)
        self.assertIn('service not initialized', result['stderr'])

    def test_executor_str_representation(self) -> None:
        definition = DistPyModuleCommandDefinition()
        executor = DistPyModuleCommandExecutor(definition)
        self.assertTrue(isinstance(str(executor), str))

    def test_executor_get_definition(self) -> None:
        definition = DistPyModuleCommandDefinition()
        executor = DistPyModuleCommandExecutor(definition)
        self.assertEqual(executor.get_definition(), definition)